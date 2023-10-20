import unittest
from _lib.lib_email import EmailSender
from _conf.server_setting import ServerSettings

# 创建 ServerSettings 实例
settings = ServerSettings()  # 切换到 'dev' 或 'prod'

# 获取 MongoDB 配置信息
mail_config = settings.get_mail_config()

# 测试用的 SMTP 配置信息
SMTP_HOST = mail_config.get('smtp_host', '')
SMTP_PORT = mail_config.get('smtp_port', 587)
SMTP_USERNAME = mail_config.get('smtp_address', '')
SMTP_PASSWORD = mail_config.get('smtp_pwd', '')

class TestEmailSender(unittest.TestCase):
    def setUp(self):
        # 在每个测试用例之前创建 EmailSender 实例
        self.email_sender = EmailSender(
            smtp_host=mail_config.get('smtp_host', ''),
            smtp_port=mail_config.get('smtp_port', 587),
            smtp_username=mail_config.get('smtp_address', ''),
            smtp_password=mail_config.get('smtp_pwd', ''),
            mail_from=mail_config.get('smtp_address', ''),
            mail_to=mail_config.get('smtp_address', '')
        )

    def tearDown(self):
        # 在每个测试用例之后清理资源
        pass

    def test_send_mail(self):
        # 测试发送邮件方法
        subject = "Test Subject"
        content = "Test Content"
        attach_img = ""  # 如果需要附件，请指定附件路径
        self.email_sender.send_mail(subject, content, attach_img)

        # 添加断言来验证邮件是否成功发送
        # 在此处添加适当的断言

if __name__ == "__main__":
    unittest.main()