import requests
import json
# 以下为手机版的百度翻译
# 需要在network下抓包，看哪个响应有翻译结果，得到那响应的url
url = "https://fanyi.baidu.com/basetrans"
translation = input("请输入要翻译的内容：")
# 把data里的from和to的值互换，可英译中
# 因为是post请求，所以需要传入参数，这个参数在headers中的from data
data = {"from": "zh",
        "to": "en",
        "query": translation}
headers = {"Referer": "https://fanyi.baidu.com/?aldtype=16047",
           "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)"
                         " AppleWebKit/604.1.38 (KHTML, like Gecko)"
                         " Version/11.0 Mobile/15A372 Safari/604.1"}
response = requests.post(url, data=data, headers=headers)
# 返回的是json字符串，需要把json字符串转化成字典，再提取数据
# print(response.content.decode())
html_str = response.content.decode()
# 把json转化成字典后，因为翻译的内容在"trans"下，再取列表第一个值，再取"dst"键的值。
ret = json.loads(html_str)["trans"][0]["dst"]
print(ret)
