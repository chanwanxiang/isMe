import time


def willdo():
    print('我爱你中国')

while True:
    # 刷新
    nowTime = time.strftime('%H:%M', time.localtime())
    # 设置要执行的时间
    if nowTime == '08:00':
        willdo()
        # 停止执行60秒，防止反复运行程序
        time.sleep(65)
    elif nowTime == '22:00':
        willdo()
        time.sleep(65)
