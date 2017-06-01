# coding:utf-8
import requests
import json

# HTTP请求类型
# get
r = requests.get('https://developer.github.com/v3/activity/events/#list-public-events')
#post
r = requests.post('http://www.ctrip.com/post')
# put
r = requests.put("http://www.ctrip.com/put")
# delete
r = requests.delete("http://www.ctrip.com/delete")
# head
r = requests.head("http://www.ctrip.com/head")
#options
r = requests.options("http://www.ctrip.com/get")

# 获取响应内容
# 字节形式显示，中文显示为字符
print r.content
# 文本方式显示
print r.text

# URL传递参数
payload = {'keyword':'日本','salecityid':'2'}
r = requests.get("http://m.ctrip.com/webapp/tourvisa/visa_list",params=payload)
print r.url

# 获取/修改网页编码
r = requests.get('https://developer.github.com/v3/activity/events/#list-public-events')
print r.encoding
r.encoding = 'uft-8'

#json处理
r = requests.get('https://developer.github.com/v3/activity/events/#list-public-events')
print r.json()

#定制请求头
url = 'http://www.ctrip.com'
headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
r = requests.post(url,headers=headers)
print r.request.headers

# 复杂post请求
url = 'http://www.ctrip.com'
payload = {'some':'data'}
#如果传递的payload是string而不是dict,需先调用dumps方法格式化
r = requests.post(url, data=json.dumps(payload))

#post多部分编码文件
url = 'http://www.ctrip.com'
files = {'file':open('report.xls','rb')}
r = requests.post(url, files=files)

#响应状态码
r = requests.get('http://www.ctrip.com')
print r.status_code

#响应头
r = requests.get('http://www.ctrip.com')
print r.headers
# 访问响应头部分内容的两种方式
print r.headers['Content-type']
print r.headers.get('content-type')

# cookies读取cookie
url = 'http://example.com/some/cookies/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']

url = 'http://www.ctrip.com/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url,cookies=cookies)

# 设置超时时间
r = requests.get('http://www.ctrip.com/cookies',timeout=0.001)

#设置访问代理
proxies = {
            "http":"http://10.10.10.10:8888",
            "https":"http://10.10.10.100:4444",
}
r = requests.get('http://www.ctrip.com',proxies=proxies)
