import csv
import time
from selenium import webdriver

# 搜索商品
def getProduct(key):
    pass

# 控制下拉页面
def dropDown():
    # 控制下拉次数 5次
    for x in range(1,11,2):
        time.sleep(0.5)
        j = x/10  # 取十分位,页面长度的百分比
        js = f'document.documentElement.scrollTop = document.documentElement.scrollHeight * {j}'
        webCrome.execute_script(js)

# 解析保存数据
def parseData():
    # 全部商品标签
    wares = webCrome.find_elements_by_css_selector('.gl-item')

    for ware in wares:
        try:
            # 商品名称
            name = ware.find_element_by_css_selector('.gl-item div.p-name a em').text
            name = name.replace('\n','')
            # 商品价格
            price = ware.find_element_by_css_selector('.gl-item div.p-price strong i').text
            # 商品评论
            comment = ware.find_element_by_css_selector('.gl-item div.p-commit strong a').text
            # 商品店铺
            mallName = ware.find_element_by_css_selector('.gl-item div.p-shop span a').text
            print(name,price,comment,mallName)
        except:
            continue

        # 数据保存
        with open('京东数据.csv',mode='a',encoding='utf-8',newline='') as f:
            csvWrite = csv.writer(f)
            csvWrite.writerow([name,price,comment,mallName])

# 点下一页
def getNext():
    webCrome.find_element_by_css_selector('.p-wrap > span.p-num > a.pn-next > em').click()


# 创建浏览驱动对象
webCrome = webdriver.Chrome()

# 使用驱动对象请求网页
webCrome.get('https://www.jd.com/')

# 需要查询的关键字
keyword = '手机'

# 搜索框中输入keyword
webCrome.find_element_by_css_selector('#key').send_keys(keyword)

# 点击搜索按钮
webCrome.find_element_by_css_selector('#search > div > div.form > button').click()

# 隐式等待页面加载完成
webCrome.implicitly_wait(10)

# 最大化浏览器
webCrome.maximize_window()

for page in range(1,10):
    # 下拉
    dropDown()
    # 解析
    parseData()
    # 点下一页
    getNext()

# 关闭驱动对象
# webCrome.quit()