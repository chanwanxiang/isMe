import os,lxml,requests
from queue import Queue
from threading import Thread
from bs4 import BeautifulSoup

# bs4 网页选择器
# Queue 特殊数据结构 临时存储数据
# threading 多线程
# lxml html解析库,将html代码转成pythoon对象

# 多线程类
class DownloadImages(Thread):
    # 重写初始化方法
    def __init__(self,queue,path):
        Thread.__init__(self)
        self.queue = queue
        self.path = path

        if not os.path.exists('./threadingimages/'):
            os.mkdir('/threadingimages/')

    # 重写run方法
    def run(self):
        while True:
            url = self.queue.get()
            try:
                downloadimage(url,self.path)
            except:
                print('下载失败')
            finally:
                # 对列告诉线程任务完成
                self.queue.task_done()

def downloadimage(url,path):
    # 1. 创建请求头
    headers = {
        'User-Agent:':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 2. 对网站进行请求
    response = requests.get(url,headers = headers)
    print(response.text)

    # 3. 页面解析
    soup = BeautifulSoup(response.text,'lxml')
    imagelist = soup.find_all('img',class_ = 'ui_image_lazy')

    for img in imagelist:
        imgurl = img['data-original']
        imgtitle = img['title']
        print(imgurl,imgtitle)

    # 4. 保存图片
    # 异常处理应为IO文件操作可能导致程序奔溃
    try:
        with open(path + imgtitle + os.path.splitext(imgurl)[-1],'wb') as f:
            # 图片是二进制文件,不能使用text方法去返回二进制文件
            image = requests.get(imgurl,headers = headers).content
            f.write(image)
            print('下载成功',imgtitle) 
    except:
        print('下载失败')

# url = 'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html'
# path = './'

# downloadimage(url,path)

if __name__ == '__main__':
    url = 'https://www.fabiaoqing.com/biaoqing/lists/page/{page}.html'
    urls = [url.format(page=page) for page in range(1,201)]

    queue = Queue()
    path = './threadingimages/'

    # 创建线程
    for x in range(10):
        worker = DownloadImages(queue,path)
        # 设定当前线程为守护线程
        worker.daemon = True
        worker.start()

    # 将网站连接压入队列中
    for url in urls:
        queue.put(url)
    
    # 等队列为空,则退出爬虫
    queue.join()
    print('下载完毕')