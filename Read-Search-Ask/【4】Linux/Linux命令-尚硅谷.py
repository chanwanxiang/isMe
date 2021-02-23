## linux系统简介
## linux远程工具Xshell
## linux文件属性与管理
## linux用户与组管理
## linux文件编辑器
## linux常用系统设置
## linux安装软件
## linux docker容器

## 第一章 Linux基础篇

#    linux是有linus响应GNU计划从unix而开发出来的内核

# 1. 文件系统目录结构

# 树状目录结构
# 经典语录在linux世界中,一切皆为文件 <--> 把设备映射成文件来管理
# /bin[重点] 是binary的缩写,这个目录存放着最经常使用的命令
# /home[重点] 存放普通用户的主目录,在linux中每个用户都有一个自己的目录,一般该目录名是以用户的账号命名的
# /root[重点] 该目录为系统管理员,也称为超级权限者的用户主目录
# /boot[重点] 存放的是启动linux时一些核心文件,包括一些链接文件和镜像文件

## 第二章 Linux实操篇

## 常用命令

# 文件目录类

# pwd  显示当前工作目录绝对路径

# ls [-选项] [目录或是文件]

# cd   目录切换指令

# mkdir  [-选项 | -p 递归创建文件夹] 参数  创建文件夹

# rmdir [-选项 | -rf 删除文件夹] 参数  删除空的文件夹

# touch 文件名称  创建个空文件  可以一次性创建多个文件

# cp [选项 | -r 递归复制文件夹] source dest \cp 当发现目标路径下有相同文件时会提示是否覆盖该指令强制覆盖

# rm [选项 | -r 递归删除整个文件 | -f 强制删除不再提示] 要删除的文件或目录

# mv  移动文件与目录或者重命名
#     mv oldfileName newfileName  重命名
#     mv /temp/movefile /targetFolder  移动目录

# cat [选项 | -n 显示行号] 要查看的文件  是以只读形式打开
#     cat -n /etc/profile | more

# more  是一个基于vim编辑器的文本过滤器,是以全屏幕的方式按页显示文本文件的内容.
#     more 要查看的文件
#     功能键 sapce -> 代表向下翻一页 enter -> 代表向下翻[一行] q ->代表立刻离开more,不再显示改文件内容
#     功能键 Ctrl+F 向下滚动一屏 Ctrl+B 返回上一屏 

# less  用来分屏查看文件内容,功能与more类似,但是比more指令更加强大,支持各种显示终端.less指令在显示文件内容时,并不是将整个文件加载之后才显示,而是根据显示需要加载内容,对于显示大型文件具有较高效率.
#     less 要查看的文件
#     功能键 space -> 向下翻动一页 enter -> 代表向下翻[一行] [pageup] -> 向上翻动一页 [pagedown] -> 向下翻动一页

# > 输出重定向 和 >> 追加
#     ll > a.txt  列表的内容写入文件中(覆盖写)
#     ll >> a.txt  列表的内容追加到文件a.txt的末尾

# cat 文件1 > 文件2  文件1覆盖到文件2
# echo `内容` >> 文件  内容写入文件

## 开机重启注销命令

# shutdown
#     shutdown -h now  立即关机
#     shutdown -h 1  1分钟后关机
#     shutdown -r now  立即重启

# halt  直接使用,效果等价关机

# reboot    重启系统

# sync  把内存的数据同步到磁盘(关机或者重启需要执行,防止数据丢失)

# 用户登录注销命令

# logout   在提示符界面下注销当前用户

# 用户与组管理

# /home/  目录下有各个创建的用户对应的家目录,当会用登录是,会自动的进入到自己的家目录中

# useradd  [模式] 用户名
#     useradd isMe  添加用户  root用户操作
#     useradd -g 用户组 用户名  添加用户并且指定组名  root用户操作

# passwd isMe  指定账户密码  root用户操作

# userdel isMe  删除用户isMe

# userdel -r isMe  删除用户isMe以及用户的主目录  root用户操作   删除是否保留家目录  删除用户时一般会保留家目录,保持文档的延续

# id root  返回用户id,组id,组名


# su - 切换用户
#     su - isMe  root高权限切换到低权限用户无需输入用户密码

# exit  退出isMe用户,回到root用户

# whoami  查看当前用户

## 用户组类似于角色,系统可以对有共性的多个角色进行统一的管理

# groupadd 组名  创建组

# groupdel 组名  删除组

# useradd -g 用户组 用户名  添加用户并且指定组名  root用户操作

# usermod -g 用户组 用户名  修改用户到指定的组名  root用户操作

## 用户和组相关文件

# 用户配置文件,用户信息  /etc/passwd

# 组配置的文件,组的信息  /etc/group

# 口令配置文件,密码和登录信息  /etc/shadow

## vim
# 命令模式
# 编辑模式
# 末行模式