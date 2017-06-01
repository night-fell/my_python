# coding:utf-8
import requests
# 引入后可以去掉警告提示
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

# 打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
}

s = requests.session()
r = s.get(url,headers=headers,verify=False)
print s.cookies

# 添加登录需要的两个cookie
c = requests.cookies.RequestsCookieJar()

# 填写抓包内容
c.set('.CNBlogsCookie','3985ECC76A92E3CAEE7C71CA11DB1EF83BB81622CA96FE3069D4F0F72A96480EC7CCDF8FB43CD8DE1128E5E720E1C7222FD92FFA4B9A34E12B5F80CA7DFC00683015193E546943938B34D89F679FA652B2D9EA6B')
c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8Mmb5OBERd5FqtiQlKZZIG75MvY2IW7Y9QV1qp41q-gMqMtXO-8PERjuDCcsPO3ch77aqqcxZmeEcZ_ZF71O_SeewO7rUdGTgfFrjkqf8ZwuvGyLz73AcDIDT4tq7eyqCRKqkpsorXpDAJ6LIvHob7x4SYbR3Yi602FBPbgewoQz_Oe4NSO5kVLBdx9t6pLK1tgDpbjO4K7ej-isHPvPk0mYa3IMQwAwPegfA9To9DlHB0Ah7t6hev5WWL-YftYeDdeJMhJgNS5jEklyA6ee6IvDrCg7h2H70HfzYKmK2iNG')
s.cookies.update(c)
print s.cookies


'''
登录成功后保存编辑内容
url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE":"",
        "__VIEWSTATEGENERATOR":"FE27D343",
    "Editor$Edit$txbTitle":"这是绕过登录的标题：lq",
    "Editor$Edit$EditorBody":"<p>这里是中文内容：http://www.cnblogs.com/yoyoketang/</p>",
    "Editor$Edit$Advanced$ckbPublished":"on",
    "Editor$Edit$Advanced$chkDisplayHomePage":"on",
    "Editor$Edit$Advanced$chkComments":"on",
     "Editor$Edit$Advanced$chkMainSyndication":"on",
     "Editor$Edit$lkbDraft":u"存为草稿"
        }
r2 = s.post(url2,data=body,verify=False)
print r.content
'''