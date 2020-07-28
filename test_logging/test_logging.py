import logging


# logging模块使用
def get_logger_object():
    # 生成logger对象
    logger = logging.getLogger('dx.log')
    logger.setLevel(logging.INFO)
    # 获取文件handler对象
    file_handler = logging.FileHandler('dx.log')
    file_handler.setLevel(logging.INFO)
    # 生成formatter对象
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - '
                                       '%(levelname)s - %(message)s ')
    # 把formatter绑定到handler对象中
    file_handler.setFormatter(file_formatter)
    # 把handler对象绑定到logger对象中
    logger.addHandler(file_handler)
    return logger


def write_log(msg):
    logger = get_logger_object()
    logger.info(msg)
    logger.handlers.pop()


if __name__ == '__main__':
    while True:
        msg = input('输入日志信息').strip()
        write_log(msg)