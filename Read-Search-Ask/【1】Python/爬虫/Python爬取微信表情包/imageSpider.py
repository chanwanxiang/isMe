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
    # print(response.text,type(response.text))  #<class 'str'>

    # 解析响应
    soup = BeautifulSoup(response.text,'lxml')
    # print(soup,type(soup))  #<class 'bs4.BeautifulSoup'>
    imglist = soup.find_all('img',attrs = {'class':'ui image lazy'})
    # print(imglist,type(imglist))  #[.,.,.] <class 'bs4.element.ResultSet'>

    # 遍历数据,提取价值数据
    for img in imglist:
        imgName = img.get('title')
        imgUrl = img.get('data-original')
        print(imgName,imgUrl)

        # 保存数据
        try:
            # os.path.splitext 分离文件名和扩展名
            # response.text 返回的是一个unicode型的文本数据
            # response.content 返回的是bytes型的二进制数据

            with open(path + imgName + os.path.splitext(imgUrl)[-1],'wb') as f:
                img = requests.get(imgUrl,headers = headers).content
                f.write(img)
                print(f'下载成功,{imgName}')
        except Exception as msg:
            print(f'下载失败,{msg}')

if __name__ == '__main__':
    urlName = 'https://fabiaoqing.com/biaoqing/lists/page/{pageNum}.html'
    urls = [urlName.format(pageNum = pageNum) for pageNum in range(1,2)]
    # print(urls)

    path = 'D:/wxchans/imgdow/'

    for url in urls:
        imgdow(url,path)