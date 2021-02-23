import jieba,parsel
import requests,imageio,wordcloud

class MovieWordCloud():

    def getData(self):

        urlN = 'https://movie.douban.com/subject/34841067/comments?start={page}&limit=20&status=P&sort=new_score'
        urls = [urlN.format(page = x*20) for x in range(10)]

        headers = {
            'User-Agent': 
         'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }

        for url in urls:
            response = requests.get(url = url,headers = headers).text

        selector = parsel.Selector(response)
        commentlist = selector.xpath('//span[@class="short"]/text()').getall()

        try:
            with open('你好,李焕英.txt','a',encoding='utf-8') as f:
                for comment in commentlist:
                    f.write(comment.replace('\n',''))
                    f.write('\n')
                print('影评爬取完成')
        except Exception as msg:
            print(f'影评爬取失败{msg}')

    def makeWord(self):
        with open('你好,李焕英.txt','r',encoding='utf-8') as f:
            details = f.read()
        detailslist = jieba.lcut(details)
        detailstring = ' '.join(detailslist)

        img = imageio.imread('D:/Coding-Always/Read-Search-Ask/【1】Python/爬虫/你好,李焕英影评爬取词云图制作/贾玲.png')  #词云图的轮廓

        # 词云图的设置
        wc = wordcloud.WordCloud(
            width = 1000,  #图片宽度
            height = 800,  #图片高度
            font_path = 'msyh.ttc',  #微软雅黑 系统自带
            mask = img,  #词云图所用的图片
            scale = 15,
            stopwords = set([line.strip() for line in open('cnStopwords.txt','r',encoding='utf-8')])
        )

        wc.generate(detailstring)
        wc.to_file('wordcloud.png')
        
if __name__ == '__main__':
    mwc = MovieWordCloud()
    mwc.getData()
    mwc.makeWord()