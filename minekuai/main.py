from DrissionPage import ChromiumPage, ChromiumOptions
from DrissionPage.common import Keys
from fake_useragent import UserAgent
import argparse, time, base64, requests, re
from google import genai
from google.genai import types
#重试次数 不建议多5此就行 一个api tokens一天30次多了就收费
max_retry = 3
GROUP_ID   = 1004540380 #群号 你自己设吧 机器人在那个群就用那个

retry_count = 0
parser = argparse.ArgumentParser(description="UserPwd?")
parser.add_argument('--username', type=str, required=True, help="The username")
parser.add_argument('--password', type=str, required=True, help="The password")
parser.add_argument('--onebot', type=str, required=True, help="The onebot api")
parser.add_argument('--onebotkey', type=str, required=True, help="The onebot apikey")
parser.add_argument('--gapi', type=str, required=True, help="The Google AI Studio API Key")
args = parser.parse_args()
ua = UserAgent()
ONEBOT_URL = args.onebot #ONEBOT API 地址
ONEBOT_KEY = args.onebotkey #ONEBOT API 地址
arguments = [
    "-no-first-run",
    "-force-color-profile=srgb",
    "-metrics-recording-only",
    "-password-store=basic",
    "-use-mock-keychain",
    "-export-tagged-pdf",
    "-no-default-browser-check",
    "-disable-background-mode",
    "-enable-features=NetworkService,NetworkServiceInProcess,LoadCryptoTokenExtension,PermuteTLSExtensions",
    "-disable-features=FlashDeprecationWarning,EnablePasswordsAccountStorage",
    "-deny-permission-prompts",
    "-disable-gpu",
    "-accept-lang=zh-CN",
    "--user-agent="+ua.chrome
    #"--user-agent=Minekuai-AutoSignin/2.0 (Devby:Huanxin) (https://github.com/xjh2009/all-sign-renew/tree/main/minekuai)"
]

options = ChromiumOptions()
for arg in arguments:
    options.set_argument(arg)
options.mute(True)
options.incognito() #隐私
options.headless() #无头
browser = ChromiumPage(addr_or_opts=options)
page = browser.get_tab(1)
page2 = browser.new_tab()
page.get('https://minekuai.com/index/login')

# 登录操作
page.actions.move_to('@name=username').click().type(args.username)
page.actions.move_to('@name=password').click().type(args.password)
page.listen.start('https://minekuai.com/auth/login')
page.actions.move_to('@type=submit').click()

res = page.listen.wait()
res.wait_extra_info(timeout=10)
if res.response:
    try:
        body = res.response.body
        if 'errors' in body and body['errors']:
            print("登录错误：", body['errors'][0].get('detail', '未知错误'))
            page.quit()
            exit(1)
    except Exception as e:
        print('解析响应失败:', e)
        exit(1)
else:
    print('登录无响应信息')
    exit(1)

page.wait.load_start()
page.get('https://minekuai.com/stars')


# 识别并计算验证码（使用 Gemini）
def get_captcha_result_via_ai(page,page2, args):
    page2.get('https://www.iloveimg.com/zh-cn/upscale-image')
    page.wait.load_start()

    # 点击弹出验证码
    page.run_js("document.querySelector('.group .absolute').click();")
    base64_str = page.ele('@alt=验证码').attr("src")
    if not base64_str:
        print("未获取到验证码图片")
        return None

    base64_data = base64_str.split(',')[-1]
    img_data = base64.b64decode(base64_data)
    timestamp = int(time.time())
    filename = f"temp-{timestamp}.png"
    with open(filename, 'wb') as f:
        f.write(img_data)

    # 上传放大处理
    page2('#pickfiles').click.to_upload(filename)
    page2.wait.load_start()
    page2.wait.ele_hidden("@class=item-loading")
    page2.listen.start('blob')
    page2.actions.move_to('@@data-value=4@@class=option__image__item').click(False)
    res2 = page2.listen.wait()
    res2.wait_extra_info(timeout=10)

    if not res2.response:
        print("放大处理失败")
        return None

    image_data2 = res2.response.body
    filename2 = f"temp-{timestamp}-max.png"
    with open(filename2, 'wb') as f:
        f.write(image_data2)

    # 使用 Gemini 处理识别与计算
    client = genai.Client(api_key=args.gapi)
    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(
                    mime_type="image/png",
                    data=image_data2
                ),
                types.Part.from_text(
                    text="""To calculate the mathematical formula for this photo, you only need to return the calculation result. If you cannot calculate it or fail, then return f."""
                )
            ]
        )
    ]
    generate_content_config = types.GenerateContentConfig(response_mime_type="text/plain")

    print("等待 AI 返回识别结果...")
    result = ""
    try:
        for chunk in client.models.generate_content_stream(model=model, contents=contents, config=generate_content_config):
            print(chunk.text)
            result += chunk.text
    except Exception as e:
        print("AI识别失败:", e)
        return None

    result = result.replace('\n', '').replace(' ', '').strip().lower()
    if result == 'f' or not result.isdigit():
        print(f"❌ AI 返回无效结果：{result}")
        return None
    return result

def sign_in(page, result):
    page.actions.move_to('@placeholder=图片验证码').click().type(Keys.CTRL_A).type(Keys.DEL)
    page.actions.move_to('@placeholder=图片验证码').click().type(result)
    page.actions.move_to('@text()=确认签到').click()
    page.listen.set_targets('system/sign')
    res = page.listen.wait(timeout=10)
    if not res or not res.response:
        print("无响应，可能请求未发送")
        return False

    try:
        body = res.response.body
        if body.get("code") == 200:
            print("✅ 签到成功：", body["msg"])
            return True

        msg = body.get("msg", "")
        print("❌ 签到失败：", msg)

        # 新增：自动解析并发送验证指令
        if (cmd := parse_verify_cmd(msg)):
            print("⚠️ 检测到需验证，自动发送指令 →", cmd)
            return send_group_msg(cmd)
    except Exception as e:
        print("响应解析失败:", e)
    return False
# ———————— OneBot 工具函数 ————————
def send_group_msg(msg: str):
    try:
        ONEBOT_KEY
        r = requests.post(
            f"{ONEBOT_URL}/send_group_msg?access_token={ONEBOT_KEY}",
            json={"group_id": GROUP_ID, "message": msg},
            timeout=5,
        )
        if r.status_code == 200 and r.json().get("status") == "ok":
            print(f"✅ 已向群 {GROUP_ID} 发送：{msg}")
            return True
        else:
            print("⚠️ 发送群消息失败：", r.text)
            return False
    except Exception as e:
        print("⚠️ OneBot 调用异常：", e)
def parse_verify_cmd(msg: str) -> str | None:

    if "请到官方QQ群发送命令" not in msg:
        return None
    m = re.search(r"[命令|command][：:]\s*(.+)$", msg)
    if not m:
        return None
    cmd = re.sub(r"\s+", "", m.group(1))
    return cmd if cmd.startswith(".") else None
# 主逻辑循环
while retry_count < max_retry:
    print(f"第 {retry_count + 1} 次尝试识别验证码并签到")
    result = get_captcha_result_via_ai(page,page2, args)
    if not result:
        retry_count += 1
        print("识别失败，重试中...\n")
        page.actions.move_to('@class=lg:flex-shrink-0 h-12 lg:h-10 lg:w-32 bg-gray-700 rounded-md cursor-pointer overflow-hidden').click()
        continue
    if sign_in(page, result):
        break
    retry_count += 1
    print("签到失败，重试中...\n")
    page.actions.move_to('@class=lg:flex-shrink-0 h-12 lg:h-10 lg:w-32 bg-gray-700 rounded-md cursor-pointer overflow-hidden').click()

if retry_count >= max_retry:
    print("❌ 达到最大重试次数，签到失败")
    browser.quit()
    
browser.quit()
