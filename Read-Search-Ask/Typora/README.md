## Typora+Github+jsDeliver搭建图床 

### 一. 简介

#### 1. 什么是图床?

图床一般是指储存图片的服务器,有国内和国外之分.国外的图床由于有空间距离等因素决定访问速度很慢影响图片显示速度.国内也分为单线空间、多线空间和cdn加速三种.
注意:github支持的就是cdn加速

#### 2.什么是jsDelive

jsDelive是一个免费的CDN解决方案,用于帮助开发者和站长.

> [jsDelive官网](https://www.jsdelivr.com/)

#### 3.为什么要搭建图床

使用图床将图片保存到服务器中,使用时通过URL获取引用

### 二. Github和PicGo配置

如图:
![image-20210331002814546](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210331002814546.png)

> 自定义域名:https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting

### 三.jsDelive加载资源

使用方法

> https://cdn.jsdelivr.net/gh/你的用户名/你的仓库名/文件路径
>    //加载js
>    https://cdn.jsdelivr.net/gh/chanwanxiang/js/jquery.js
>    //加载图片
>    https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/image/1.png



