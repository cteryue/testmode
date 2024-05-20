import configparser

from config.conf import cm

HOST = 'HOST'

class ReadConfig(object):
    # 初始化
    def __init__(self):
        # 读取解析原始的配置文件
        self.config = configparser.RawConfigParser()
        self.config.read(cm.ini_file,encoding="utf-8")

    def _get(self,section,option):
        # 获取配置文件信息，section表示标题，option表示key
        return self.config.get(section,option)

    def _set(self,section,option,value):
        # 设置配置文件信息，section表示标题，option表示key，value表示value
        """
        注意：其中section无法追加，只能追加已有section中的option和value
        """
        self.config.set(section,option,value)
        # 写入文件
        with open(cm.ini_file,'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST,HOST)

    # @property
    def set_url(self,section,option,value):
        return self._set(section,option,value)

ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
    # ini.set_url(HOST,"PATH","https://www.bilibili.com")