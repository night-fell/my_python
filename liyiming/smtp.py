# -*- coding:utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText

if __name__ == "__main__":
    print ("发送文本邮件示例")

    #邮件发送者
    sender = "q15110185703@126.com"
    #邮件接收者
    receivers = "liqing@wecash.net"
    # 发送内容构建
    # text标识发送内容为文本格式
    msg = MIMEText("测试文本", "plain", "utf-8")
    msg["From"] = "q15110185703@126.com"
    msg["To"] = receivers

    #构建邮件标题
    msg["Subject"] = Header("回归通过", "utf-8")

    #smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    #发件人用户名
    username = "q15110185703"

    #发件人密码
    password = "123qwe"

    #构建smtp对象
    smtp = smtplib.SMTP()

    #连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    print ("connectresult", con)

    #登录smtp服务
    log = smtp.login(username, password)
    print ("loginresult", log)

    #发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("sendresult:", res)

    #退出qq
    smtp.quit()
    print("send email finish")

