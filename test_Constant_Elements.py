import configparser

class Constants():

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('C:\\users\\waqas.adil\\Doris_POM\\resources\\credentials.ini')
        self.EMAIL = self.config['parameters']['email']
        self.PASSWORD = self.config['parameters']['password']

        self.URL = "https://doris-tst.npe.evisions.com/"
        self.WAIT_TIME = 30
        self.SHORT_WAIT = 5
        self.LONG_WAIT = 300
        self.FIREFOX = executable_path = r'C:\\geckodriver.exe'
        # CHROME = executable_path=r'C:\\Drivers\chromedriver.exe'
        self.CHROME = executable_path = r'C:\\Users\waqas.adil\Doris_POM\Drivers\chromedriver.exe'
        self.CSV_DATASOURCE = 'Library Branch Data Source'
        self.CSV_QUERY = 'SELECT branchid, recordactivitydate, branchname, branchstatusraw, branchstatus, iscentralormainbranch, isipedsreportable FROM $$CSV_TABLE_NAME'
        self.HOST_NAME = "192.168.20.231"
        self.PORT = 1523
        self.SID = "demo17.Evisions.com"
        self.USER_NAME = "APP_DBO"
        self.USER_PSWRD = "app_db0"

