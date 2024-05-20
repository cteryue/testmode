import os

from selenium.webdriver.common.by import By

from utils.times import dt_strftime


class ConfigManager(object):
    # 获取当前目录位置
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR,'page_element')
    # 报告目录
    REPORT_FILE = os.path.join(BASE_DIR,'report.html')

    # 定位模式
    LOCATE_MODE = {
        'css':By.CSS_SELECTOR,
        'xpath':By.XPATH,
        'id':By.ID,
        'class':By.CLASS_NAME,
        'name':By.NAME
    }

    # 邮件信息
    EMAIL_INFO = {
        'username':"2016201028@qq.com",
        "password":"邮箱授权码",
        'smtp_host':'smtp.qq.com',
        'smtp_port':465
    }

    # 收件人
    ADDRESSEE = [
        '2016201028@qq.com'
    ]

    @property
    def log_file(self):
        # 拼接路径
        log_dir = os.path.join(self.BASE_DIR,'logs')
        # 判断路径是否存在
        if not os.path.exists(log_dir):
            # 不存在则创建
            os.makedirs(log_dir)
        # 返回根据当前时间拼接的日志文件路径
        return os.path.join(log_dir,'{}.log'.format(dt_strftime()))

    @property
    def ini_file(self):
        ini_path = os.path.join(self.BASE_DIR,'config','config.ini')
        if not os.path.exists(ini_path):
            raise FileNotFoundError(f"配置文件{ini_path}不存在！")
        return ini_path
cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)
    print(cm.ELEMENT_PATH)
    cm.ini_file