# 蓝天云/海绵联机/雨云/优丰互联/山海云 自动签到/续费

使用Github Action自动签到/续费蓝天云/海绵联机/雨云/优丰云/山海云<br>

作者：**[XJHya](https://github.com/xjh2009)**<br>
B站，抖音，名字不一，转载请注明作者<br>

## Tips

各厂商链接[蓝天云](https://lantian.pro/)/[海绵联机](https://www.hmmc.pro/)/[雨云](https://www.rainyun.com/)/[优丰互联](https://www.disxcloud.com/)/[山海云](https://www.vpsvr.com/)

如果有免费面板服/可以续费的云厂商 可以联系我QQ：2012036686

我不需要XXX的签到/续费: <br>
进入Actions->左侧选择你不需要的->最右侧三个点->Disable workflow

## 使用方式

### Fork本项目
Fork本项目<br>
#### 启动Action
进入您自己的项目，点击Action，启用Github Action功能<br>

### 1.蓝天云

因为一些外界力量导致无法使用GithubAction进行自动续费<br>
所以你需要前往[lty.hxhl.bf](https://lty.hxhl.bf)添加队列任务<br>
当然如果你想继续使用也可以寻找我们购买API 1元/月/60次

### 2.海绵联机/优丰互联/山海云


#### 添加续费任务
yfidc.json(优丰互联)/hmmc.json(海绵联机)/shyidc.json(山海云)文件，分别添加你的用户ID
<br>
```json
[
  "114514",
  "1919810"
]
```
文件提交后，自动进入Github Action构建


### 3.雨云

#### 配置环境变量
进入Settings->Secret and variables->Actions->New Repository secret
将你的Name输入RAINYUN_APIKEYS<br>
将你的Secret输入APIKEY<br>
例子
```
APIKEY1,APIKEY2,APIKEY3
```
配置成环境变量

### 定时执行
每日北京时间6点自动续费<br>

## 相关项目
[海绵联机自动签到](https://github.com/xjh2009/hmmc-renew)<br>
[蓝天云自动续费](https://github.com/xjh2009/lty-renew)<br>
[雨云自动续费](https://github.com/xjh2009/rainyun-renew)<br>
