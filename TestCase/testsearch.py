import re

import pytest
from selenium import webdriver

from common.readconfig import ini
from page_object.searchpage import SearchPage
from utils.loggers import log


class TestSearch:
    @pytest.fixture(scope="function",autouse=True)
    def open_baidu(self,drivers):
        search = SearchPage(drivers)
        search.get_url(ini.url)

    def test01(self,drivers):
        search = SearchPage(drivers)
        search.input_search("selenium")
        search.click_search()
        result = re.search(r"selenium",search.get_source)
        log.info(result)
        assert result

    def test02(self,drivers):
        search = SearchPage(drivers)
        search.input_search("selenium")
        log.info(list(search.imagine))
        assert all(["selenium" in i for i in search.imagine])

if __name__ == '__main__':
    pytest.main()