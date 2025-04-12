from DrissionPage import ChromiumPage,ChromiumOptions
from fake_useragent import UserAgent
import argparse
parser = argparse.ArgumentParser(description="UserPwd?")
    
# 添加命令行参数
parser.add_argument('--username', type=str, required=True, help="The username")
parser.add_argument('--password', type=str, required=True, help="The password")
    
# 解析命令行参数
args = parser.parse_args()

ua = UserAgent()

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
]
options = ChromiumOptions()
for argument in arguments:
    options.set_argument(argument)
    
options.incognito() #隐私
options.headless() #无头
# 创建对象
page = ChromiumPage(addr_or_opts=options)
page.listen.start()
# 访问网页
page.get('https://minekuai.com/')
#点击登录按钮
page.run_js("document.querySelector('button[class=\"loginbutton\"]').click()")
#输入账户密码
page.actions.move_to('@name=username').click().type(args.username) 
page.actions.move_to('@name=password').click().type(args.password) 
#真要登录了
page.run_js("document.querySelectorAll('button').forEach(btn => btn.className.includes('from-blue-500/10') && btn.className.includes('to-purple-500/10') && btn.click());")
print("succ")#懒得写校验了
#稍等加载结束
page.wait.load_start()
# 写入
with open("u.a", "w") as file_a:
    file_a.write(page.user_agent)

with open("local.s", "w") as file_l:
    file_l.write(page.local_storage("Admin-Token"))

page.quit()