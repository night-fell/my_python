# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == "__main__":

    sender = "q15110185703@126.com"
    receiver = "liqing@wecash.net"

    msg = MIMEMultipart()
    msg["From"] = "q15110185703@126.com"
    msg["To"] = receiver
    msg["Subject"] = Header("测试附件邮件发送", "utf-8")
    msg.attach(MIMEText("附件如下：", "plain","utf-8"))

    attach1 = MIMEText(open("Report.xls", 'rb').read(), "base64", "utf-8")
    attach1["Content-Type"] = "application/octet-stream"
    attach1["Content-Disposition"] = "attrachment;filename=report.xls"

    msg.attach(attach1)

    smtpserver = "smtp.126.com"
    smtpport = 25

    username = "q15110185703"
    password = "123qwe"

    smtp = smtplib.SMTP()

    con = smtp.connect(smtpserver, smtpport)
    log = smtp.login(username, password)
    res = smtp.sendmail(sender, receiver, msg.as_string())

    smtp.quit()
    print("send email finish")