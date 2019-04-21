
import re
import time
import requests
import random
from threading import Thread
import gevent


from gevent import monkey
monkey.patch_all()

import os


class Spider():

    def __init__(self,key_word):
        self.url = "https://www.pexels.com/search/"+ key_word
        self.User_Agent = [
            "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
            "MQQBrowser/25 (Linux; U; 2.3.3; zh-cn; HTC Desire S Build/GRI40;480*800)",
            "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1 /110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
            "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2",
            "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
        ]

        self.headers = {
            'User-Agent': random.choice(self.User_Agent)
        }
        self.num = 0

    def get_response(self,page):

        # url = self.url + "?page=" + str(page
        params = {"page":page}
        response = requests.get(self.url,headers=self.headers,params=params,timeout=10)
        # time.sleep(3)
        # print(response.status_code)
        if int(response.status_code) != 200:
            print("connect api error !!!!")
        else:
            return response

    def get_photos(self,page):

        # 建立正则规则
        pattern = re.compile(r'src="https://images.pexels.com/photos/(\d+)/(.*?)\?.*"', re.M)
        response = self.get_response(page)
        # print(response.text)
        items = re.findall(pattern, response.text)
        print(items)
        for item in items:
            self.num = self.num + 1
            try:
                photo_url = 'https://static.pexels.com/photos/' + str(item[0]) + '/' + str(item[1])
                # 把图片链接中的images，改成了static

                self.save_photo(photo_url,item)
            except:
                continue

    def save_photo(self,photo_url,item):

        file_path = 'E:\Program Files\develop\python\spider\图片\\' + str(self.num) + str(".") + str(item[1].split('.')[1])

        print('正在下载第'+ str(self.num) + '张图片......')
        # print(photo_url)
        result = requests.get(photo_url,headers=self.headers)
        # print(result.content)
        with open(file_path, 'wb') as f:
            f.write(result.content)
        if result != 'wrong':
            print('下载成功！')
        else:
            print('失败')


if __name__ == '__main__':

    key_word = input("输入关键词（英文）：")
    page = int(input("输入爬取的页数（数字）："))
    test_sp = Spider(key_word)

    for i in range(1,page):
        test_sp.get_photos(i)