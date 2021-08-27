# encoding: utf-8
# Author    : clz
# Datetime  : 2021/8/24 21:27
# User      : Administrator
# Product   : PyCharm
# Project   : CityNameInWordService
# File      : ResultUtil.py
# explain   : 文件说明


class ResultUtil:

    def __init__(self, code, info):
        self.code = code
        self.info = info

    def toDict(self):
        result ={}
        result.update({"code":self.code})
        result.update({"info":self.info})
        print(result)

    @staticmethod
    def getSuccessResult():
        return ResultUtil(1,None)

    @staticmethod
    def getErrorResult(info):
        return ResultUtil(-1, info)
