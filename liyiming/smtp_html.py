# -*- coding:utf-8 -*-

import smtplib

from email.mime.text import MIMEText
from email.header import Header

sender = "q15110185703@126.com"

receivers = "liqing@wecash.net"

msg = MIMEText("<p>测试邮件发送</p><a href='http://www.testingunion.com'>开源优测社区</a>","html","utf-8")
msg["From"] = "q15110185703@126.com"
msg["To"] = receivers

msg["Subject"] = Header("测试网页格式邮件发送", "utf-8")

smtpserver = "smtp.126.com"
smtpport = 25

username = "q15110185703"
password = "123qwe"

smtp = smtplib.SMTP()

con = smtp.connect(smtpserver, smtpport)
log = smtp.login(username, password)
res = smtp.sendmail(sender, receivers, msg.as_string())

smtp.quit()
print ("send email finish")