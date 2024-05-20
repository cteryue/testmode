import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from config.conf import cm
from utils.loggers import log
from utils.times import sleep


class WebPage(object):
    # 初始化
    def __init__(self,driver):
        # driver = webdriver.Chrome()
        self.driver = driver
        # 设置等待时间
        self.timeout = 20
        # 显式等待
        self.wait = WebDriverWait(self.driver,self.timeout)

    # 进入网址
    def get_url(self,url):
        # self.driver.maximize_window()
        # 设置页面加载最大等待时间60s，超过报错
        # self.driver.set_page_load_timeout(10)
        try:
            self.driver.get(url)
            # 隐式等待
            self.driver.implicitly_wait(10)
            log.info(f"打开网站:{url}")
        except TimeoutError:
            raise TimeoutError(f"打开{url}超时，请检查网络或网址服务器")

    # @staticmethod表示静态方法
    @staticmethod
    def element_locator(func,locator):
        """元素定位器"""
        name,value = locator
        # 这里func传入的参数等同于func(By.?,"?")
        return func(cm.LOCATE_MODE[name],value)

    def find_element(self,locator):
        """寻找单个元素"""
        # lambda *args: self.wait.until(EC.presence_of_element_located(args))
        # 匿名函数，等待匹配到第一个元素为止
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self,locator):
        """寻找多个元素"""
        # lambda *args: self.wait.until(EC.presence_of_all_element_located(args))
        # 匿名函数，等待匹配到所有元素为止
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def element_num(self,locator):
        """获取元素数量"""
        num = len(self.find_elements(locator))
        log.info(f"相同元素：{locator}{num}")
        return num

    def input_text(self,locator,text):
        """在输入框中输入"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(text)
        log.info(f"在元素{locator}输入：{text}")

    def is_click(self,locator):
        """单击事件"""
        ele = self.find_element(locator)
        ele.click()
        sleep()
        log.info(f"点击元素：{locator}")

    def get_text(self,locator):
        """获取定位到的元素的文本"""
        _text = self.find_element(locator).text
        log.info(f"获取文本：{_text}")
        return _text

    # @property将类的方法转换为属性，使得我们可以像访问普通属性一样访问和设置这些方法。
    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)