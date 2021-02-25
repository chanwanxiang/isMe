## TCP客户端程序开发

# 1. TCP客户端程序开发示例代码

# 导入socket模块
import socket

if __name__ == '__main__':
    # 创建TCP客户端套接字
    # 1.AF_INET:表示ipv4
    # 2. SOCK_STEAM:tcp传输协议
    ClientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

