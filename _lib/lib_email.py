import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from email import encoders
import os

class EmailSender:
    def __init__(self, smtp_host, smtp_port, smtp_username, smtp_password, mail_from = "", mail_to = ""):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.mail_from = mail_from
        self.mail_to = mail_to

    def send_mail(self, subject="主旨", content="內容", attach_img=""):
        msg = MIMEMultipart()
        msg["subject"] = subject
        msg["from"] = self.mail_from
        msg["to"] = self.mail_to

        text = MIMEText(content)  # 创建邮件正文
        msg.attach(text)  # 将邮件正文添加到消息

        if attach_img != "" and os.path.exists(attach_img):
            img_data = open(attach_img, 'rb').read()
            image = MIMEImage(img_data)
            msg.attach(image)

        with smtplib.SMTP(host=self.smtp_host, port=self.smtp_port) as smtp:
            try:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(self.smtp_username, self.smtp_password)
                smtp.send_message(msg)
                print("Send Complete!")
            except Exception as e:
                print("Send Error message: ", e)        