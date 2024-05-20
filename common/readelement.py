import os

import yaml

from config.conf import cm


class Element(object):
    def __init__(self,name):
        self.file_name = "{}.yaml".format(name)
        self.element_path = os.path.join(cm.ELEMENT_PATH,self.file_name)
        if not os.path.exists(self.element_path):
            os.makedirs(self.element_path)
        with open(self.element_path,encoding="utf-8") as f:
            self.data = yaml.load(f,Loader=yaml.FullLoader)

    def __getitem__(self, item):
        data = self.data.get(item)
        if data:
            key,value = data.split("==")
            return key,value
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name,item))

if __name__ == '__main__':
    element = Element("search")
    print(element["搜索框"])