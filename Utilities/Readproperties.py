import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class Readconfig():

    @staticmethod
    def getLoginUrl():
        LoginUrl = config.get('Common-info', 'BaseUrl')
        return LoginUrl

    @staticmethod
    def getUsername():
        Username = config.get('Common-info', 'Username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('user_info', 'Password')
        return Password






