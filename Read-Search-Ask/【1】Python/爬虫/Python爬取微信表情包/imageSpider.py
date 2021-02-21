import os,requests
# 网页选择器
from bs4 import BeautifulSoup
# 队列
from queue import Queue
# 多线程包
from threading import Thread

def imgdow(url,path):
    # 创建请求头
    headers = {
        'User-Agent': 
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 对网站进行请求
    response = requests.get(url,headers = headers)
    print(response.text,type(response.text))  #<class 'str'>

    # 解析响应
    soup = BeautifulSoup(response.text,'lxml')
    # print(soup,type(soup))  #<class 'bs4.BeautifulSoup'>

url = r'https://fabiaoqing.com/biaoqing/lists/page/1.html'
# path = 

imgdow(url,path=None)