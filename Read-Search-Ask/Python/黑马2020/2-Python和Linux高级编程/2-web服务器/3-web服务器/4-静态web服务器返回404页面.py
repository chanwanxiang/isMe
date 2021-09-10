# 1. 开发自己的静态web服务器
#     实现步骤
#         1. 编写一个TCP服务端程序
#         2. 获取浏览器发送的http请求报文数据
#         3. 读取固定页面数据,把页面数据组装成HTTP响应报文数据发送给浏览器
#         4. HTTP响应报文数据发送完成以后,关闭服务与客户端的套接字

# 2. 示例代码

import os,sys,socket

def main():
    # 创建TCP服务端套接字
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口号复用
    serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 绑定端口号
    serverSocket.bind(('',8000))
    # 设置监听
    serverSocket.listen(128)

    while True:
        # 等待接受客户端的连接请求
        newSocket,ipPort = serverSocket.accept()
        # 接受客户端的请求信息
        recvdata = newSocket.recv(4096)
        # 判断接受数据长度是否为0
        if len(recvdata) == 0:
            newSocket.close()
            return
        # 对二进制数据进行解码
        recvcont = recvdata.decode('utf-8')
        print(recvcont)
        # 对数据按照空格分割
        requestlist = recvcont.split(' ',maxsplit=2)
        # 获取请求资源路径
        requestpath = requestlist[1]
        print(requestpath)
        # 判断请求的是否是跟目录,如果是跟目录返回指定首页
        if requestpath == "/":
            requestpath = '/index.html'
        
        # TODO: 返回404界面
        # 方式一:os.path.exits
        # os.path.exits('static'+requestpath)
        
        try:
            # 打开文件读取文件中的数据
            with open('static'+requestpath,'rb') as f:
                filedata = f.read()
        # TODO: 返回404页面
        except Exception as e:
            # 代码执行到此,说明没有请求的文件,需要返回404页面
            # 404响应行
            responseline = 'HTTP/1.1 404 NOT FOUND\r\n'
            # 404响应头
            responseheader = 'SERVER: PWS\r\n'
            # 打开404指定页面文件内容
            with open('static/error.html','rb') as f:
                filedata = f.read()
            # 404响应体
            responsebody = filedata
            # 404响应内容
            response = (responseline + responseheader + '\r\n').encode('utf-8') + responsebody
            # 把数据封装成HTTP响应报文格式数据
            newSocket.send(response)
        else:
            # 代码执行到此,说明文件存在,返回200状态信息
            # 响应行
            responseline = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            responseheader = 'SERVER: PWS\r\n'
            # requestStr = "static\" + requestpath
            # 响应体二进制的数据
            responsebody = filedata
            # 响应行响应头转二进制
            response = (responseline + responseheader + '\r\n').encode('utf-8') + responsebody
            # 把数据封装成HTTP响应报文格式数据
            newSocket.send(response)
        finally:
            # 关闭服务于客户端套接字
            newSocket.close()

if __name__ == '__main__':
    main()