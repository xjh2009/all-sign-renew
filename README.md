# 海绵联机/雨云/优丰互联/大东云/糖糕云/WeMC/量芯云/灰狼云/岸云数据/麦块联机/辰隙互联/鱼乐云 自动签到/续费

使用Github Action自动签到/续费海绵联机/雨云/优丰互联/大东云/糖糕云/WeMC/量芯云/灰狼云/岸云数据/麦块联机/辰隙互联/鱼乐云<br>

本项目由幻心互联[2mc.shop](https://app.2mc.shop/_XJHya)自己开发自己赞助 

作者：**[XJHya](https://github.com/xjh2009)**<br>

## 战绩可查
<details>

<summary>此部分已折叠</summary>


![QQ20250122-012610](https://github.com/user-attachments/assets/43c7c1d5-b185-4648-b65a-c7b0c49e4ebe)
![糖糕云沃错了](https://github.com/user-attachments/assets/056e82a1-b24c-4f9b-850e-6634355cd9f7)
![v安慕希沃搓了](https://github.com/user-attachments/assets/40660395-2829-4738-ad8e-55a60cffb503)
![迈快恋姬倭厝叻](https://github.com/user-attachments/assets/ba0367f2-e0f7-4d56-bef9-bc60305583ad)
![eb01a45950b6b71cdb4b01a4dc1da757](https://github.com/user-attachments/assets/61337054-3f1c-4683-97e0-b62ce11b9dcc)
</details>


<details>
<summary>超级战绩</summary>

Wemc双毕业
麦块联机双毕业
海绵联机B站毕业
糖糕云账户毕业


</details>

## Tips

各厂商链接[海绵联机](https://www.yunmc.vip/)/[雨云](https://www.rainyun.com/)/[优丰互联](https://www.disxcloud.com/)/[WeMC](https://wemc.cc/)/[量芯云](https://idc.prolzy.com/)/[灰狼云](https://www.yun316.net/)/[岸云数据](https://www.anvps.cn/)/[麦块联机](https://minekuai.com/)/[辰隙互联](https://www.singsi.cn/)/[鱼乐云](https://www.ueidc.cn/)

如果有免费面板服/可以续费的云厂商 可以联系我QQ：2012036686

~~已修复~~ https://xjh2009.github.io/mkfl/ 获取麦块联机文件的直链

我不需要XXX的签到/续费: <br>
进入Actions->左侧选择你不需要的->最右侧三个点->Disable workflow

## 使用方式

### Fork本项目
Fork本项目<br>
#### 启动Action
进入您自己的项目，点击Action，启用Github Action功能<br>


<details>

<summary>部分遗弃签到</summary>


### 3.糖糕云（十分不推荐使用）

#### 配置环境变量
糖糕云目前玩不起了，正好年底了直接跑路吧<br>
进入Settings->Secret and variables->Actions->New Repository secret <br>
将你的Name输入TGYUN_USERPASSWD<br>
将你的Secret输入用户名密码<br>
例子
```
email=test1@test1.com&password=password1,email=test2@test2.com&password=password2
```
配置成环境变量

### 4.雨云

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入RAINYUN_APIKEYS<br>
将你的Secret输入APIKEY<br>
例子
```
APIKEY1,APIKEY2,APIKEY3
```
配置成环境变量

### 5.WeMC

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入WEMC_USERPASSWD<br>
将你的Secret输入账户密码<br>
例子
```
test1@test1.com:password1,test2@test2.com:password2
```
配置成环境变量

</details>


### 1.优丰互联/大东云/岸云数据


#### 添加续费任务
岸云因为源站垃圾所以暂时搞不了 <br>
sign.json文件，分别添加你的用户ID yfidc(优丰互联)/ddyidc(大东云)/anvps(岸云数据)<br>
示例，假设这三家IDC用户ID都为`114514`和`123456`就可以这样填
<br>
```json
{
    "ddyidc": [114514,123456],    
    "yfidc": [114514,123456],
    "anvps": [114514,123456]
}
```
文件提交后，自动进入Github Action构建

### 2.海绵联机

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入`HMLJ_USERPASSWD`<br>
将你的Secret输入用户名密码<br>
例子
```
email=test1@test1.com&password=password1,email=test2@test2.com&password=password2
```
配置成环境变量


### 3.量芯云虚拟主机

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入`LXVH_USERPASSWD`<br>
将你的Secret输入账户密码<br>
例子
```
test1@test1.com:password1:产品ID1,test2@test2.com:password2:产品ID1
```
配置成环境变量

### 4.灰狼云虚拟主机

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入`YUN316_USERPASSWD`<br>
将你的Secret输入账户密码和主机ID<br>
例子
```
邮箱1:密码1:主机ID1,邮箱2:密码2:主机ID2
```
### 5.麦块联机

#### 配置环境变量
### 麦块你还是别开了 从网站切到机器人您是这个👍👍👍👍
因为网络问题直接使用海外IP部署NapCat会导致你的QQ出现无法登录风控等问题
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入`MK_TOKENS`<br>
将你的Secret输入用户名密码<br>
将你的Name输入`MK_ONEBOT`<br>
将你的Secret输入OneBOT地址 如果没有我推荐使用[NapCat](https://napcat.napneko.icu/)搭建 目前看应该是可以单个QQ签到多个账户的
<br>将你的Name输入`MK_ONEBOT_KEY`<br>
将你的Secret输入OneBOT的APIkey<br>
将你的Name输入`GOOGLE_AISTUDIO`<br>
将你的Secret输入[AI Studio](https://aistudio.google.com/apikey)的APIKEY<br>
MK_TOKENS例子
```
用户名1:密码1,用户名2:密码2
```
### 6.辰隙互联

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入`SS_USERPASSWD`<br>
将你的Secret输入账户密码和服务器ID<br>
将你的Name输入`GOOGLE_AISTUDIO`<br>
将你的Secret输入[AI Studio](https://aistudio.google.com/apikey)的APIKEY<br>
例子
```
手机号1|密码1|服务器IP地址2,手机号2|密码2|服务器IP地址2
```
配置成环境变量

### 7.鱼乐云

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入`UEIDC_USERPASSWD`<br>
将你的Secret输入账户密码<br>
Tips:因为他们续费服务器的接口还是太丑了 所以只做签到
例子
```
用户名1|密码1,用户名2|密码2
```
配置成环境变量

### 定时执行
每日北京时间6点自动续费<br>
