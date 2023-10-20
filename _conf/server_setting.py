class ServerSettings:
    def __init__(self, site_mode='dev'):
        self.site_mode = site_mode

        self.config = {
            "dev": {
                "mongo": {
                    "mongodb_url": "mongodb://user01:11qqaazz@120.109.48.253",
                    "db_name": "unitest",
                },
                "mysql": {
                    "url": "120.109.48.253",
                    "user": "user08",
                    "pwd": "11qqaazz"
                },
                "email":{
                    "smtp_host" : "smtp.gmail.com",
                    "smtp_port" : 587,
                    "smtp_address" : "lllason@gmail.com",
                    "smtp_pwd" : "ddmp tvvr evjn besl",
                }
            },
            "prod": {
                "mongo": {
                    "mongodb_url": "mongodb://user01:11qqaazz@120.109.48.253",
                    "db_name": "prod",
                },
                "mysql": {
                    "url": "120.109.48.253",
                    "user": "user08",
                    "pwd": "11qqaazz"
                },
                "email":{
                    "smtp_host" : "smtp.gmail.com",
                    "smtp_port" : 587,
                    "smtp_address" : "lllason@gmail.com",
                    "smtp_pwd" : "ddmp tvvr evjn besl",
                }
            }
        }

    def get_mongo_config(self):
        return self.config[self.site_mode]['mongo']

    def get_mysql_config(self):
        return self.config[self.site_mode]['mysql']

    def get_mail_config(self):
        return self.config[self.site_mode]['email']        