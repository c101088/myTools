# encoding: utf-8
# Author    : clz
# Datetime  : 2021/8/24 21:03
# User      : Administrator
# Product   : PyCharm
# Project   : CityNameInWordService
# File      : FileSaveService.py
# explain   : 文件说明
from docx import Document
from flask import Blueprint
from flask import request
from src.utils.ResultUtil import ResultUtil
from src.config import FILE_PATH
import os

# 等同于原来在 manage.py里面的 app = Flask()


FileSaveService = Blueprint('fileSaveService', __name__)


@FileSaveService.route('/addFile', methods=['POST'])
def addFile():  # put application's code here
    loadedFile = request.files['file']
    if loadedFile == None:
        result = ResultUtil.getErrorResult("上传文件错误，请核实file参数")
        return result.toDict()
    fileName = loadedFile.filename
    if not os.path.exists(FILE_PATH):
        os.mkdir(FILE_PATH)
    if os.path.exists(FILE_PATH+'/'+fileName):
        os.remove(FILE_PATH + '/' + fileName)
    loadedFile.save(FILE_PATH+'/'+fileName)
    return ResultUtil.getSuccessResult().toDict()

@FileSaveService.route('/deleteFile', methods=['GET'])
def deleteFile():  # put application's code here
    fileName = request.files['fileName']
    if fileName == None:
        result = ResultUtil.getErrorResult("文件名错误，请核实fileName参数")
        return result.toDict()
    if os.path.exists(FILE_PATH+'/'+fileName):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(FILE_PATH+'/'+fileName)
        return ResultUtil.getSuccessResult().toDict()
        # os.unlink(path)
    else:
        result = ResultUtil.getErrorResult("文件不存在 "+ fileName)
        return result.toDict()


def getWordFileText(fileName):
    tempWord = Document(FILE_PATH+'/'+fileName)
    tempText = ""
    for paragraph in tempWord.paragraphs:
        tempText = tempText + paragraph.text
    return tempText
