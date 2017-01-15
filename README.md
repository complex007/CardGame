# Python 网络编程入门练习题
python基本语法入门请阅读：[python快速教程](http://www.cnblogs.com/vamei/archive/2012/09/13/2682778.html)
## 1. 找出100——999种所有的水仙花数
水仙花数是指：一个三位数，其各位数字立方和等于该数本身。例如：370=33+73+00.这就说明370是一个水仙花数。【考察循环的使用】

## 2. 冒泡排序
实现一个函数bubbleSort(lst)，返回从大到小排序后的list。【考察使用python的list和函数】
测试数据：
```
[2, 31,2,52,1,52,1,23,4,6,88,4,45,27,54,43,745,23,68 ,345,2,6,45,8,8,7,5,334,2346,323]
```


## 3. 帮奇奇整理实验数据文件
奇奇是一个勤奋好学的研究生，在学校负责做眼动仪实验，每次实验都会产生若干个文件。在做了很多次实验之后，她准备处理实验数据。但是她发现自己在做实验的时候没有仔细把实验数据分类，有的实验文件被多次保存，放在了不同的文件夹下。因为不希望一次实验数据被多次统计，她希望把data文件夹下所有的重名文件只提取一次出来。哥哥已经帮她把data文件夹下所有数据文件放到了一个python list里面：
```
[
'data/jack/result1_2015_08_11.dat',
'data/jack/result2_2015_08_11.dat',
'data/jack/result3_2015_08_11.dat',
'data/jack/result4_2015_08_11.dat',
'data/jack/result5_2015_08_11.dat',
'data/jack/result6_2015_08_11.dat',
'data/jack/result7_2015_08_11.dat',
'data/jack/result8_2015_08_11.dat',
'data/jack/result9_2015_08_11.dat',
'data/jack/result10_2015_08_11.dat',
'data/jack/result12_2015_08_11.dat',
'data/jack/result11_2015_08_11.dat',
'data/jack/result13_2015_08_11.dat',
'data/jack/result16_2015_08_11.dat',
'data/jack/calibrated/result1_2015_08_11.dat',
'data/jack/calibrated/result2_2015_08_11.dat',
'data/jack/calibrated/result3_2015_08_11.dat',
'data/jack/calibrated/result4_2015_08_11.dat',
'data/jack/calibrated/result5_2015_08_11.dat',
'data/jack/calibrated/result6_2015_08_11.dat',
'data/jack/calibrated/result7_2015_08_11.dat',
'data/jack/calibrated/result8_2015_08_11.dat',
'data/jack/calibrated/result9_2015_08_11.dat',
'data/jack/calibrated/result10_2015_08_22.dat',
'data/jack/calibrated/result12_2015_08_22.dat',
'data/jack/calibrated/result11_2015_08_22.dat',
'data/jack/calibrated/result13_2015_08_22.dat',
'data/jack/calibrated/result14_2015_08_2.dat',
'data/jack/calibrated/result15_2015_08_22.dat',
'data/Amy/calibrated/result1_2015_08_22.dat',
'data/Amy/calibrated/result2_2015_08_22.dat',
'data/Amy/calibrated/result3_2015_08_22.dat',
'data/Amy/calibrated/result4_2015_08_22.dat',
'data/Amy/calibrated/result5_2015_08_22.dat',
'data/Amy/calibrated/result6_2015_08_11.dat',
'data/Amy/calibrated/result7_2015_08_11.dat',
'data/Amy/calibrated/result8_2015_08_11.dat',
'data/Amy/calibrated/result9_2015_08_11.dat',
'data/Amy/calibrated/result10_2015_08_11.dat',
'data/Amy/calibrated/result12_2015_08_11.dat',
'data/Amy/jack/calibrated/result11_2015_08_11.dat',
'data/Amy/jack/calibrated/result13_2015_08_11.dat',
'data/Amy/jack/calibrated/result14_2015_08_11.dat',
'data/Amy/jack/calibrated/result15_2015_08_11.dat'
]
```

写一个程序，打印不重复的文件的路径。【考察字典】
提示程序：
```
//get the extension of one file
a = 'data/Amy/jack/calibrated/result15_2015_08_11.dat'
print a.split('.')[-1]
```

## 4. 文件IO
第三题中，哥哥并没有把文件的list写好，而是把文件路径放在了一个叫dat_files.txt的文件里。写程序读取这个文件，存入python的list。【考察文件IO】


## 5. 斗地主（一）
妹妹要设计一款斗地主在线游戏，哥哥帮她在网上下载了扑克牌的图片库，并且写了一个名为card_mapping.json的文件。写程序实现以下步骤：

a). 使用python的json库，把card_mapping.json转换成python的一个dict；

b). 实现一个名叫Card的类，类图如下：

|Card                                    |
|----------------------------------------|
|id: String (json的key）                 |
|name: utf-8 String  (中文名)            |
|image: String (图片文件名)              |
|value: int (每一张牌有一个值，用作比大小)|
|-------------------------------------|
|toDict()  （把card变成dict）		|

c). 根据card_mapping.json里面的内容，生成54张牌的Card Object，例如：
10_c对应的card object是id="10_c", name="梅花10"，image="10_of_clubs.png",value="10"
各个牌的value如下表：

|name|value|
|----|-----|
|3   |3  |
|4   |4  |
|5   |5  |
|6   |6  |
|7   |7  |
|8   |8  |
|9   |9  |
|10  |10 |
|J   |11 |
|Q   |12 |
|K   |13 |
|A   |15 |
|2   |20 |
|小王|50 |
|大王|100|


【翻译: ♣Clubs, ♦Diamonds，♥Hearts， ♠Spades】
	
d). 将54个card objects生成json，存储到cards.json文件里，格式如下：

```
{
	"10_c": {"id"："10_c", "name":"梅花10"，"image"："10_of_clubs.png","value"："10"},
	…….
}
```
e). 洗牌：将card_mapping.json所有的keys放到一个list里面，打乱顺序

f). 建立一个class叫CardBundle:


|CardBundle|
|----------|
|cards: list of cards|
|----------|
|__init__(cardList)|

g).  建立一个class叫Player:

|Player|
|----------|
|id: String (以后数据库里面的id）|
|name: utf-8 String  (昵称)|
|wealth: int （财富值）|
|avatar: String (头像图片文件)|


	
h). 建立class叫GameRole：

|GameRole
|----------|
|player: Player|
|cards: list of cards  手牌|
|lastDiscard: cardBuddle 最后一次出的牌|
|----------|
|__init__(player, cardList)|
|cardCount() :int  手上剩多少张牌|
|discard(cardList): CardBundle  出牌|

建立Farmer和LandLord这两个class，都继承自GameRole

i). 建立Dispipe class，牌冢

|Dispipe|
|----------|
|cards: list of cards|
|----------|
|__init__()|
|receive(cardBundle)  放入牌冢|
|cardCount() :int  牌冢有多少张牌|

j). 建立Game class

|Game|
|farmer1: Farmer|
|farmer2: Farmer|
|landLord: LandLord|
|dispipe: Dispipe|
|__init__(player1, player2, player3)|




## 6. SQLite
阅读教程：[python标准库14：数据库（sqlite3）](http://www.cnblogs.com/vamei/p/3794388.html)，实现以下功能：
a). 在doudizhu.db文件中，新建table叫 player

|id| Int primary key, auto increase|
|--------------|-------------------|
|Name|text|
|wealth|int|
|avatar|text|



b). createPlayer(player)

c). getPlayerById(id): Player

d). updatePlayer(player): Player

e). deletePlayerById(id)


## 7. REST CURD
阅读[flask官网教程](http://docs.jinkan.org/docs/flask/quickstart.html)，实现以下http REST API：

base_url=localhost:8000

a). POST /api/player

b). GET /api/player

c). GET /api/player/:id

d). PUT /api/player/:id

e). DELETE /api/player/:id

## 8. Jquery: master-detail page
使用Jquery调用第七题里面的api，实现：

a). 显示player list页面，当点击list其中某一行时候，进入detail页面
b). 显示detail页面，可以更改这个player的信息
c). 在list页面加入Add player按钮，实现新建player
d). 在list的每一行末尾加入delete按钮

## 9. SQL or JSON?
新建一个名为player.json的文件，请使用这个文件替代第6和第7题中的sqlite数据库


## 10. Go NoSQL
安装mongodb和python的[mongodb library](https://docs.mongodb.com/ecosystem/drivers/python/)，使用mongodb替代第9题中的player.json文件。

## 11. 斗地主（二）
a). 参考这个[项目](http://vineetgarg90.github.io/playing-cards/) ，源码[在这里](https://github.com/vineetgarg90/playing-cards)
任意形式在浏览器显示54张牌的图片（不是css做出来的卡片，使用png图片）
b). 将牌分成两组，单击任意一张卡片，都会让这张卡片显示到另外一组。【复习codecademy上面的jquery】




