from selenium import webdriver

from common.readconfig import ini
from utils.times import sleep


def test01():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(ini.url)
    sleep(5)