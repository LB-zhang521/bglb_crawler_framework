# -*- coding:utf-8  -*-
# @Time     : 2021-03-27 01:09
# @Author   : BGLB
# @Software : PyCharm
from functools import wraps
from  config import CODE_TEMPLATE


def singleton(cls):
    """
        单例装饰器 singleton
    :param cls:
    :return:
    """
    _singleton = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if not _singleton.get(cls):
            _singleton[cls] = cls(*args, **kwargs)
        return _singleton[cls]
    return wrapper


