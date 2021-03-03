import requests
import pprint

# HTTP工具类封装 每个请求需要做异常捕获,日志记录,协议转换,封装工具方便进行统一维护

class RequestUtil:
    def __init__(self):
        pass

    def request(self, url, method, headers=None, params=None, contentType=None):
        try:
            if method == 'get':
                result = requests.get(url=url, params=params, headers=headers).json()
                return result
            elif method == 'post':
                if contentType == 'application/json':
                    result = requests.post(url=url, json=params, headers=headers).json()
                    return result
                else:
                    result = requests.post(url=url, data=params, headers=headers).json()
                    return result
            else:
                print('HTTP MEATHOD NOT ALLOWED')

        except Exception as e:
            print('HTTP请求报错:{0}'.format(e))

if __name__ == "__main__":
    # url = 'https://api.xdclass.net/pub/api/v1/web/all_category'
    # r = RequestUtil()
    # result = r.request(url,'get')
    # pprint.pprint(result)

    url = 'https://api.xdclass.net/pub/api/v1/web/web_login'
    r = RequestUtil()
    # headers = {'Content-Type':'application/x-www-form-urlencoded'}
    data = {'phone':'13113777555','pwd':'1234567890'}
    result = r.request(url, 'post', params=data)
    pprint.pprint(result)