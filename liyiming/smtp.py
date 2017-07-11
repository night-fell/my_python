# -*- coding:utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText

if __name__ == "__main__":
    print ("发送文本邮件示例")

    #邮件发送者
    sender = "deep_test@126.com"
    #邮件接收者
    receivers = "q15110185703@126.com"
    # 发送内容构建
    # text标识发送内容为文本格式
    msg = MIMEText("测试", "plain", "utf-8")
    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    #构建邮件标题
    msg["Subject"] = Header("回归通过", "utf-8")

    #smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    #发件人用户名
    username = "deep_test"

    #发件人密码
    password = "123456a"

    #构建smtp对象
    smtp = smtplib.SMTP()

    #连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    print ("连接结果：", con)

    #登录smtp服务
    log = smtp.login(username, password)
    print ("登录结果：", log)

    #发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果：", res)

    #退出qq
    smtp.quit()
    print("send email finish")

