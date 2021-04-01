### 1. 什么是Python虚拟环境

一种采用协作式隔离的运行时环境,允许Python用户和应用程序在安装和升级Python分发包时不会干扰到同一系统上运行的其他Python应用程序的行为.

### 2. 虚拟环境相关工具区分

### 3. venv基本使用和原理

查看venv命令参数

> python -m venv -h

![image-20210401215357140](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401215357140.png)

创建虚拟环境

> python -m venv venvdemo

![image-20210401215831406](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401215831406.png)

虚拟环境原理

> 修改环境变量,把虚拟环境的Python路径加入环境变量最前,环境变量使用原则近者优先.

![image-20210401220456638](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401220456638.png)

### 4. 虚拟环境的必要性

### 5. 在IDE中使用虚拟环境

### 6.保存和复制虚拟环境

虚拟环境依赖导出

> pip freeze > requirement.txt

![image-20210401220936652](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401220936652.png)