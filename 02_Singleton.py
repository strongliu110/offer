#!/usr/bin/env python
# coding=utf-8

from functools import wraps


class Singleton(object):
    _instance = []

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instance[cls]


"""装饰器"""
def single_ton(cls):
    _instance = []

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrapper


@single_ton
class SingleTon(object):
    def __init__(self, a):
        self.a = a