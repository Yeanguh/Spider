import  requests
import json
import bs4
import re
index = 1
for i in range(1,14):

    url = "https://www.douyu.com/gapi/rknc/directory/yzRec/" + str(i)
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
    }

    resp = requests.get(url,headers=headers)

    if int(resp.status_code) != 200:
        print("连接失败")
    else:
        print("连接成功正在下载第" + str(i) + "页")
    response = json.loads(resp.content)
    ret = response["data"]["rl"]
    for v in ret:
        print(index)
        temp = v["rs16"]

        buff = temp.split("/")[len(temp.split("/"))-1].split(".")[1]

        image = requests.get(temp,headers=headers)
        with open("./pic/" + str(index) + "." + buff, 'wb') as f:
            f.write(image.content)
        index += 1


# print(image.content)