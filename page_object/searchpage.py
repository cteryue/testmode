from common.readelement import Element
from page.webpage import WebPage

# 实例化yaml对象
search = Element("search")

class SearchPage(WebPage):
    """搜索输入框输入指定text"""
    def input_search(self,text):
        self.input_text(search["搜索框"],text = text)

    @property
    def imagine(self):
        """在输入框搜索数据后，查询出来的文本列表"""
        return [f.text for f in self.find_elements(search["搜索联想"])]

    def click_search(self):
        """点击搜索按钮"""
        self.is_click(search["搜索按钮"])