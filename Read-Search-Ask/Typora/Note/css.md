# 1、什么是CSS？

如何学习

1. css是什么
2. css怎么用（快速入门）
3. css选择器（重点+难点）
4. 美化网页（文字，阴影，超链接，列表，渐变...）
5. 盒子模型
6. 浮动
7. 定位
8. 网页动画（特效）



## 1.1、什么是CSS

Cascading Style Sheel 层叠级联样式表

CSS：表现（美化网页）

字体，颜色，边距，高度，宽度，背景图片，网页定位，网页浮动

![image-20210121093621053](CSS.assets/image-20210121093621053.png)



## 1.2、发展史

css1.0

css2.0	DIV（块）+css ，HTML与css结构分离的思想，网页变得简单，SEO

css2.1	浮动、定位

css3.0	圆角，阴影，动画。。。浏览器兼容性~



## 1.3、快速入门

style

**基本入门**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
<!--    规范  <style>可以编写css的代码，每一个声明最好使用分号结尾
    语法：
        选择器{
            声明1；
            声明2；
            声明3；
        }

-->
    <style>
        h1{
            color:red;
        }
    </style>
</head>
<body>
<h1>我是标题</h1>
</body>
</html>
```



建议使用这种规范

![image-20210121095052193](CSS.assets/image-20210121095052193.png)



**css的优势：**

1. 内容和表现分离
2. 网页结构表现统一，可以实现复用
3. 样式十分的丰富
4. 建议使用独立于html的css文件
5. 利于SEO，容易被搜索引擎收录



## 1.4、CSS的3种导入方式

优先级：就近原则

```html
<!--行内样式：-->
<h1 style="color:red">我是标题</h1>

<!--内部样式-->：
    <style>
        h1{
            color: green;
        }
    </style>

<!-- 外部样式：

同级目录下创建CSS文件夹，然后里面创建stylesheet文件：-->
<link rel="stylesheet" href="css/style.css">
<!--stylesheet:-->
h1{
    color: red;
}
```



# 2、选择器

> 作用:选择页面上的某一个或者某一类元素



## 2.1 基本原则其

1. 标签选择器:选择一类标签  标签名{}

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>Title</title>
       <style>
           /*标签选择器，会选择到页面上所有的这个标签的元素*/
           h1{
               color: #0d8ddb;
               background: #1E0FBE;
               border-radius: 20px;
           }
           p{
               font-size: 50px;
           }
       </style>
   </head>
   <body>
   <h1>学Java</h1>
   <p>听狂神说</p>
   </body>
   </html>
   ```

   

2. 类选择器 class:选择所有属性一致的标签,跨标签  .类名{}

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
<!--    类选择器的格式 .类的名称-->
    <style>
        .dyk{
            color: #cc0000;
        }
        .tzt{
            color: #0e9aef;
        }
    </style>
</head>
<body>
<h1 class="dyk">标题1</h1>
<h1 class="tzt">标题2</h1>
<h1 class="dyk">标题3</h1>
<p class="tzt">P标签</p>
</body>
</html>
```

3. id选择器:全局唯一  #id名{}

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        /*
        id选择器   #id名{}      id必须保证全局唯一
        不遵循就近原则，固定的
        id选择器>class选择器>标签选择器
         */
        #dyk{
            color: red;
        }
        .tzt{
            color: #0d8ddb;
        }
    </style>
</head>
<body>
<h1 id="dyk">标题1</h1>
<h1 class="tzt">标题2</h1>
<h1 class="tzt">标题3</h1>
<h1>标题4</h1>
</body>
</html>
```



优先级:id>class>标签



## 2.2 层次选择器

1. 后台选择器：在某个元素的后面	祖爷爷 爷爷 爸爸 我

   ```html
   <style>
   /*后代选择器*/
   body p{
               background: red;
           }
   </style>
   ```

   

2. 子选择器,一代，儿子·

    ```html
   /*子选择器*/
           body>p{
               background: #0e9aef;
           }
   ```

   

3. 相邻兄弟选择器, 同辈

   ```html
           /*相邻兄弟选择器:只有一个且只对下*/
           .active + p{
               background: #c6ffc6;
           }
   ```

   

4. 通用选择器

```html
/*通用兄弟选择器,当前选中元素的向下的所有兄弟元素*/
        .active~p{
            background: yellow;
        }
```

​	

## 2.3 结构伪类选择器

伪类：条件

```html
    <style>
        /*ul得第一个子元素*/
        ul li:first-child{
            background: red;
        }
        /*ul得最后一个子元素*/
        ul li:last-child{
            background: #0d8ddb;
        /*选中P1:定位到父元素,选择当前得第一个元素.选择当前p元素得父级元素,选中父级元素得第一个,并且是当前元素才生效*/
        p:nth-child(2){
            background: #1ab394;
        }
        /*选中父元素,下得p元素得第二个,类型*/
        p:nth-of-type(2){
            background: yellow;
        }
        }
</style>
```



## 2.4、属性选择器（常用）

```html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .demo a{
            float: left;
            display: block;
            height: 50px;
            width: 50px;
            border-radius: 10px;
            background: #0e9aef;
            text-align: center;
            text-decoration: none;
            color: #9b9b9b;
            margin-right: 10px;
            font:bold 20px/50px Arial;
        }
        /*属性名,属性名=属性值(正则)
        =   绝对等于
        *=  包含这个元素
        ^=  以这个开头
        %=  以这个结尾
        存在id属性的元素 a[]{}
        */
        /*a[id]{*/
        /*    background: yellow;*/
        /*}*/
        /*a[id=first]{*/
        /*    background: #cc0000;*/
        /*}*/
        /*class中有links的元素*/
        /*a[class*="links"]{*/
        /*    background: #cc0000*/
        /*}*/
        /*选中href中以http开头的元素*/
        /*a[href^=http]{*/
        /*    background: #c6ffc6;*/
        /*}*/
        /*选中href中以pdf结尾的元素*/
        a[href$=pdf]{
            background: #ca4440;
        }
    </style>
</head>
<body>
<p class="demo">
    <a href="http://www.baidu.com" class="links item first" id="first" >1</a>
    <a href="http://xxx.com" class="links item active" target="_blank" title="test">2</a>
    <a href="images/11.html" class="links item">3</a>
    <a href="images/13.png" class="links item">4</a>
    <a href="abc" class="links item">5</a>
    <a href="/a.pdf" class="links item">6</a>
    <a href="/abc.pdf" class="links item last">7</a>
</p>
</body>
</html>
```

![image-20210121165156860](CSS.assets/image-20210121165156860.png)



```html
=
*=
^=
$=
```



# 3、美化网页元素

## 3.1、为什么要美化网页

1. 有效的传递页面信息
2. 美化网页，页面漂亮才能吸引用户
3. 凸显页面的主题
4. 提高用户的体验



span标签：重点要突出的字，使用span套起来

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        #title1{
            font-size: 50px;
        }
    </style>
</head>
<body>

欢迎学习<span id="title1">Java</span>
</body>
</html>
```

## 3.2、字体样式

```html
    <!--
    font-family:字体
    font-size:字体大小
    font-weight:字体的粗细
    color:字体颜色
    -->
    <style>
        body{
            font-family: "Arial Black",楷体;
            color: #0e9aef;
        }
        h1{
            font-size: 50px;
        }
        .p1{
            font-weight: 200;
        }
```



## 3.3、文本样式

1. 颜色	color rgb rgba
2. **文本对齐方式      text-align:centor**
3. **首行缩进     text-indent:2em;**
4. **行高    line-height:**    单行文字上下居中！ 等于height
5. 装饰    text-decoration:
6. 文本图片水平对齐   vertical-align:middle

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!--
    颜色:
        单词
        RGB     0~F
        RGBA
    text-align:排版，居中
    text-indent:2em ；段落首行缩进

    height: 300px;
    line-height: 300px;
        行高，和 块的高度一致，就可以上下居中
    /*下划线*/
    text-decoration: underline;

    /*中划线*/
    text-decoration: line-through;

    /*下划线*/
    text-decoration: overline;
    
    /*超链接去下划线*/
    text-decoration: none;
    -->
    <style>
        h1{
            color: #ca4440;
            text-align: center;
        }
        .p1{
            text-indent: 2em;
        }
        .p3{
            background: #0e9aef;
            height: 300px;
            line-height: 300px;
        }
        .l1{
            /*下划线*/
            text-decoration: underline;
        }
        .l2{
            /*中划线*/
            text-decoration: line-through;
        }
        .l3{
            /*下划线*/
            text-decoration: overline;
        }
        a{
            /*超链接去下划线*/
            text-decoration: none;
        }
    </style>
</head>
<body>
<a href="">123</a>
<p class="l1">12321312</p>
<p class="l2">12321312</p>
<p class="l3">12321312</p>
<h1>故事介绍</h1>
<p class="p1">平静安详的元泱境界，每隔333年，总会有一个神秘而恐怖的异常生物重生，它就是魁拔！魁拔的每一次出现，都会给元泱境界带来巨大的灾难！即便是天界的神族，也在劫难逃。在天地两界各种力量的全力打击下，魁拔一次次被消灭，但又总是按333年的周期重新出现。魁拔纪元1664年，天神经过精确测算后，在魁拔苏醒前一刻对其进行毁灭性打击。但谁都没有想到，由于一个差错导致新一代魁拔成功地逃脱了致命一击。很快，天界魁拔司和地界神圣联盟均探测到了魁拔依然生还的迹象。因此，找到魁拔，彻底消灭魁拔，再一次成了各地热血勇士的终极目标。</p>
<p>在偏远的兽国窝窝乡，蛮大人和蛮吉每天为取得象征成功和光荣的妖侠纹耀而刻苦修炼，却把他们生活的村庄搅得鸡犬不宁。村民们绞尽脑汁把他们赶走。一天，消灭魁拔的征兵令突然传到窝窝乡，村长趁机怂恿蛮大人和蛮吉从军参战。然而，在这个一切都凭纹耀说话的世界，仅凭蛮大人现有的一块冒牌纹耀，不要说参军，就连住店的资格都没有。受尽歧视的蛮吉和蛮大人决定，混上那艘即将启程去消灭魁拔的巨型战舰，直接挑战魁拔，用热血换取至高的荣誉。 [1]</p>
<p class="p3">I have searched a thousand years,
　 And I have cried a thousand tears.
　 I found everything I need,
　 You are everything to me.</p>
</body>
</html>
```



## 3.4、阴影

![image-20210123170215700](CSS.assets/image-20210123170215700.png)

```css
/*text-shadow：阴影颜色，水平偏移，垂直偏移，阴影半径*/
#price{
    text-shadow: #000000 10px 0px 2px;
}
```





## 3.5、超链接伪类

正常情况下，a,a:hover

```css
/*默认的颜色*/
a{
    text-decoration: none;
    color: #000000;
}
/*鼠标悬浮的状态(只需要记住:hover)*/
a:hover{
    color: orange;
    font-size: 50px;
}
```



## 3.6、列表

![image-20210123182000210](CSS.assets/image-20210123182000210.png)

```css

#nav{
    width: 300px;
    background-color: #b4b4ae;


}
.title {
    background-color: red;
    font-size: 18px;
    font-weight: bold;
    text-indent: 1em;
    line-height: 35px;
    /*颜色，图片，图片位置，平铺方式*/
    background:red url("d.png") 270px 10px no-repeat;
}
/*
list-style:
none;去掉圆点
circle;空心圆
decimal 数字
square  正方形

*/
ul li{
    background:#b4b4ae url("r.png") 220px 13px no-repeat;
    height: 50px;
    list-style: none;
    text-indent: 1em;
}
a{
    text-decoration: none;
    font-size: 14px;
    color: #000000;
}
a:hover{
    color: orange;
    /*text-decoration: underline;*/
}
```



## 3.7、背景

```css
div{
    width: 1000px;
    height: 700px;
    border: 1px solid red;
    background-image: url("images/a.jpg");
    /*    默认是全部平铺的*/
}
.div1{
    background-repeat: repeat-x;
}
.div2{
    background-repeat: repeat-y;
}
.div3{
    background-repeat: no-repeat;
}
```



## 3.8、渐变

```css
background-color: #00DBDE;
background-image: linear-gradient(90deg, #00DBDE 0%, #FC00FF 100%);
```



# 4、盒子模型

## 4.1、什么是盒子

![image-20210127091840249](CSS.assets/image-20210127091840249.png)

margin：外边距

padding：内边距

border：边框



## 4.2、边框

1. 边框的粗细
2. 边框的样式
3. 边框的颜色

```html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        /*body总有一个默认的外边距margin：0*/
        h1, ul, li, a, body {
            margin: 0;
            padding: 0;
            text-decoration: none;
        }

        /*border：粗细，样式，颜色*/
        #box {
            width: 300px;
            border: 1px solid red;
        }
        h2{
            font-size: 16px;
            background: #1ab394;
            line-height: 30px;
            margin: 0;
            color: white;
            text-align:center;
        }

        form {
            background: #1ab394;
        }

        div:nth-of-type(1) input {
            border: 3px solid black;
        }

        div:nth-of-type(2) input {
            border: 2px dashed green;
        }
    </style>
</head>
<body>
<div id="box">
    <h2>会员登录</h2>
    <form action="#">
        <div>
            <span>用户名：</span>
            <input type="text">
        </div>

        <div>
            <span>密码：</span>
            <input type="text">
        </div>

        <div>
            <span>邮箱：</span>
            <input type="text">
        </div>
    </form>
</div>
</body>
</html>
```



## 4.3、内外边距

```html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
<!--    外边距的妙用:居中元素-->
    <style>

        /*border：粗细，样式，颜色*/
        #box {
            width: 300px;
            border: 1px solid red;
            margin:0 auto;
        }
        h2{
            font-size: 16px;
            background: #1ab394;
            line-height: 30px;
            margin: 0;
            color: white;
            text-align:center;
        }

        form {
            background: #1ab394;
        }
        input{
            border: 1px solid black;
        }
    </style>
</head>
<body>
<div id="box">
    <h2>会员登录</h2>
    <form action="#">
        <div>
            <span>用户名：</span>
            <input type="text">
        </div>

        <div>
            <span>密码：</span>
            <input type="text">
        </div>

        <div>
            <span>邮箱：</span>
            <input type="text">
        </div>
    </form>
</div>
</body>
</html>
```

盒子的计算方式：你知道个元素到底多大？

![image-20210127100041858](CSS.assets/image-20210127100041858.png)



## 4.4、圆角边框

```html
    <style>
        div{
            width: 100px;
            height: 100px;
            border: 10px solid red;
            /*圆角边框*/
            border-radius: 100px;
        }
    </style>
</head>
<body>
<div>

</div>
</body>
```



## 4.5、阴影

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        div {
            width: 100px;
            height: 100px;
            border: 10px solid red;
            box-shadow:10px 10px 100px yellow;

        }
    </style>
</head>
<body>
<div>

</div>
</body> 
</html>
```



# 5、浮动

标准文档流

![image-20210127134036709](CSS.assets/image-20210127134036709.png)



块级元素：独占一行

```html
h1-h6  	p	div	列表。。。
```

行内元素（内联元素）：不独占一行

```html
span	a	img	strong...
```

行内元素 可以被包含在块级元素中，反之，则不可以~！



## 5.2、display

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
<!--
block   块元素
inline  行内元素    
inline-block   是块元素，但是可以内联，在一行
none
-->
    <style>
        div{
            width:100px;
            height: 100px;
            border: 1px solid red;
            display: none;
        }
        span{
            width:100px;
            height: 100px;
            border: 1px solid red;
            display: inline-block;
        }
    </style>
</head>
<body>
<div>div块元素</div>
<span>span行内元素</span>
</body>
</html>
```

1、这个也是一种实现行内元素排列的方式，但是我们很多情况都是用float

## 5.3、float

1、左右浮动	float



## 5.4、父级边框塌陷问题

clear 

![image-20210127143604814](CSS.assets/image-20210127143604814.png)



解决方案：

1. 增加父级元素的高度

   ![image-20210127145945539](CSS.assets/image-20210127145945539.png)

2. 增加一个空的div标签吗，清除浮动

   ```html
   <div class="clear"></div>
   
   .clear{
   	clear:both;
   	margin:0;
   	padding:0;
   }
   ```

   

3. overflow

   ```html
   1.在父级元素中增加一个	overflow：hidden；
   ```

4. 父类添加一个伪类：after

   ```html
   #father:after{
   	content:'';
   	display:block;
   	clear:both;
   }
   ```



**小结**

1. 浮动元素后面增加空div

   简单，代码中尽量避免空div

2. 设置父元素的高度

   简单，元素假设有了固定的高度，就会被限制

3. overflow

   简单，下拉的一些场景避免使用

4. 父类添加一个伪类：推荐，写法稍微复杂一点，但是没有副作用



## 5.5、对比

- display
  - 方向不可控制
- float
  - 浮动起来的话会脱离标准文档流，所以要解决父级边框塌陷的问题



# 6、定位

## 6.1、相对定位

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
<!--
    相对定位
    相对于自己原来的位置进行偏移
-->
    <style>
        body{
            padding: 20px;
        }
        div{
            margin: 20px;
            padding: 5px;
            font-size: 12px;
            line-height: 25px;

        }
        #father{
            border: 1px solid #666;
            padding: 0;
        }
        #first{
            background: #a13d30;
            border: 1px dashed #664130;
            position: relative; /*相对定位：上下左右*/
            top:-20px;
            left: 20px;
        }
        #second{
            background:green;
            border: 1px dashed #662959;
        }
        #third{
            background: #c6ffc6;
            border: 1px dashed #1b6366;
            position: relative;
            bottom: 10px;
            right: 20px;
        }
    </style>
</head>
<body>
<div id="father">
    <div id="first">第一个盒子</div>
    <div id="second">第一个盒子</div>
    <div id="third">第一个盒子</div>
</div>
</body>
</html>
```

相对定位：

position：relative

相对于原来的位置，进行指定的偏移,相对定位的话，它任然在标准文档流中，原来的位置会被保留

```html
top
left
bottom
right
```

练习：

```html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        #box {
            width: 300px;
            height: 300px;
            padding: 10px;
            border: 2px solid red;
            text-align: center;
            line-height: 100px;
            display: inline-block;
        }

        a {
            width: 100px;
            height: 100px;
            background: fuchsia;
            text-align: center;
            line-height: 100px;
            display: block;
            text-decoration: none;
        }

        a:hover {
            background: #0e9aef;
        }

        .a2, .a4 {
            position: relative;
            left: 200px;
            top: -100px
        }

        .a5 {
            position: relative;
            left: 100px;
            top: -300px
        }

    </style>
</head>
<body>
<div id="box">
    <a class="a1" href="">链接1</a>
    <a class="a2" href="">链接2</a>
    <a class="a3" href="">链接3</a>
    <a class="a4" href="">链接4</a>
    <a class="a5" href="">链接5</a>
</div>
</body>
</html>
```



## 6.2、绝对定位

定位：基于xxx定位，上下左右~

1. 没有父级元素定位的前提下，相对于浏览器定位
2. 假设父级元素存在定位，我们通常会用相对父级元素进行偏移~
3. 在父级元素范围内移动

相对于父级或浏览器的位置，进行指定的偏移,相对定位的话，它不在标准文档流中，原来的位置不会被保留



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
<!--
    相对定位
    相对于自己原来的位置进行偏移
-->
    <style>
        body{
            padding: 20px;
        }
        div{
            margin: 20px;
            padding: 5px;
            font-size: 12px;
            line-height: 25px;

        }
        #father{
            border: 1px solid #666;
            padding: 0;
            position: relative;
        }
        #first{
            background: #a13d30;
            border: 1px dashed #664130;
        }
        #second{
            background:green;
            border: 1px dashed #662959;
            position: absolute;
            right: 20px;
        }
        #third{
            background: #c6ffc6;
            border: 1px dashed #1b6366;
        }
    </style>
</head>
<body>
<div id="father">
    <div id="first">第一个盒子</div>
    <div id="second">第二个盒子</div>
    <div id="third">第三个盒子</div>
</div>
</body>
</html>
```



## 6.3、z-index

![image-20210127164534812](CSS.assets/image-20210127164534812.png)

图层

z-index:默认是0，最高无限~999

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        #content {
            width: 380px;
            padding: 0px;
            margin: 0px;
            overflow: hidden;
            font-size: 12px;
            line-height: 25px;
            border:1px #000000 solid;
        }

        ul, li {
            padding: 0px;
            margin: 0px;
            list-style: none;
        }
        /*父级元素相对定位*/
        #content ul{
            position: relative;
        }
        .tipText,.tipBg{
            position: absolute;
            width: 380px;
            height: 25px;
            top:200px;
        }
        .tipText{
            color: white;
            z-index: 999;
            text-align: center;
        }
        .tipBg{
            background: black;
            opacity: 0.5;   /*背景透明度*/
        }
    </style>
</head>
<body>
<div id="content">
    <ul>
        <li>
            <img src="123.webp" alt="">
        <li class="tipText">学习使我快乐</li>
        <li class="tipBg"></li>
        <li>时间：2099-01-01</li>
        <li>地点：月球一号基地</li>
        </li>
    </ul>
</div>
</body>
</html>
```



# 7、动画

