import logging

from config.conf import cm


class log:
    def __init__(self):
        # 获取日志对象
        self.logger = logging.getLogger()
        # 判断日志是否有handler
        if not self.logger.handlers:
            # 设置日志等级为DEBUG
            self.logger.setLevel(logging.DEBUG)

        # 创建一个handle写入文件
        fh = logging.FileHandler(cm.log_file,encoding="utf-8")
        fh.setLevel(logging.INFO)

        # 创建一个handle输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 设置日志格式
        formatter = logging.Formatter(self.fmt)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 添加到handler中
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    # @property注解表示该方法只有返回值，它可以像属性一样被访问，而不需要使用括号调用
    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'

log = log().logger

if __name__ == '__main__':
    log.info("测试日志")