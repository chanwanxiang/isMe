import os
import parsel
import requests



os.makedirs('./imgs/')

urlOri = r'https://tieba.baidu.com/f?kw=%D4%BC%BB%E1&fr=ala0&tpl=5'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

response = requests.get(url=urlOri, headers=headers).text

# 转换数据类型
selector = parsel.Selector(response)
hreflist = selector.xpath(
    '//ul[@class="threadlist_bright j_threadlist_bright"]/li//div[@class="t_con cleafix"]//div[@class="threadlist_lz clearfix"]/div/a/@href').getall()

print(hreflist)

for href in hreflist:
    allUrl = 'https://tieba.baidu.com' + href
    print('当前帖子链接:', allUrl)

    responseSecond = requests.get(url=allUrl, headers=headers).text

    selectorSecond = parsel.Selector(responseSecond)

    # imgslist = selectorSecond.xpath('//cc/div/img/[@class="BDE_Image"]/@src').getall()

    imgslist = selectorSecond.xpath('//cc/div//img[@class="BDE_Image"]/@src').getall()

    print(imgslist)

    for imgs in imgslist:
        imgdata = requests.get(url=imgs,headers=headers).content

        fileName = imgs.split('/')[-1]
        with open('imgs\\' + fileName,'wb') as f:
            f.write(imgdata)

