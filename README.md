# 海绵联机/雨云/优丰互联/大东云/糖糕云/WeMC/量芯云/灰狼云/岸云数据/麦块联机 自动签到/续费

使用Github Action自动签到/续费海绵联机/雨云/优丰互联/大东云/糖糕云/WeMC/量芯云/灰狼云/岸云数据/麦块联机<br>

作者：**[XJHya](https://github.com/xjh2009)**<br>
B站，抖音，名字不一，转载请注明作者<br>
## 战绩可查
![糖糕云沃错了](https://github.com/user-attachments/assets/056e82a1-b24c-4f9b-850e-6634355cd9f7)
![v安慕希沃搓了](https://github.com/user-attachments/assets/40660395-2829-4738-ad8e-55a60cffb503)

## Tips

各厂商链接[海绵联机](https://www.yunmc.vip/)/[雨云](https://www.rainyun.com/)/[优丰互联](https://www.disxcloud.com/)/[WeMC](https://wemc.cc/)/[量芯云](https://idc.prolzy.com/)/[灰狼云](https://www.yun316.net/)/[岸云数据](https://www.anvps.cn/)/[麦块联机](https://minekuai.com/)

如果有免费面板服/可以续费的云厂商 可以联系我QQ：2012036686

我不需要XXX的签到/续费: <br>
进入Actions->左侧选择你不需要的->最右侧三个点->Disable workflow

## 使用方式

### Fork本项目
Fork本项目<br>
#### 启动Action
进入您自己的项目，点击Action，启用Github Action功能<br>

### 1.优丰互联/大东云/岸云数据


#### 添加续费任务
岸云因为源站垃圾所以暂时搞不了 <br>
sign.json文件，分别添加你的用户ID yfidc(优丰互联)/ddyidc(大东云)/anvps(岸云数据)<br>
示例，假设这三家IDC用户ID都为114514和123456就可以这样填
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
将你的Name输入HMLJ_USERPASSWD<br>
将你的Secret输入用户名密码<br>
例子
```
email=test1@test1.com&password=password1,email=test2@test2.com&password=password2
```
配置成环境变量

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

### 6.量芯云虚拟主机

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入LXVH_USERPASSWD<br>
将你的Secret输入账户密码<br>
例子
```
test1@test1.com:password1:产品ID1,test2@test2.com:password2:产品ID1
```
配置成环境变量

### 7.灰狼云虚拟主机

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入YUN316_USERPASSWD<br>
将你的Secret输入账户密码和主机ID<br>
例子
```
邮箱1:密码1:主机ID1,邮箱2:密码2:主机ID2
```
### 8.麦块联机

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret<br>
将你的Name输入MK_USERPASSWD<br>
将你的Secret输入账户密码和主机ID<br>
例子
```
用户ID1:服务器ID1:服务器单日续费价格1,用户ID2:服务器ID2:服务器单日续费价格2
```
配置成环境变量



### 定时执行
每日北京时间6点自动续费<br>
