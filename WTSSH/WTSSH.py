# encoding: utf-8
# Author    : clz
# Datetime  : 2020/6/13 18:22
# User      : Administrator
# Product   : PyCharm
# Project   : WTSSH
# File      : WTSSH.py
# explain   : 文件说明

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect
from pip._vendor.distlib.compat import raw_input


class frstphp:
    def __init__(self):
        self.config = {
            '0': {'host': '192.168.53.239', 'user': 'clz', 'password': '\\', 'port': 22}
        }

    def send_command(self, child, cmd):
        child.sendline(cmd)
        child.expect('#')
        print
        child.before
        child.sendline('ls -lh /')
        child.interact()

    def connect(self):
        print(
            '''
            [0] 测试服务器1
            [1] 测试服务器2
            [2] 测试服务器3
            '''
        )
        idKey = raw_input(" 请选择服务器:")

        user = self.config[idKey]['user']
        host = self.config[idKey]['host']
        password = self.config[idKey]['password']
        port = self.config[idKey]['port']

        connStr = 'ssh ' + user + '@' + host + ' -p ' + str(port)
        child = pexpect.spawn(connStr)
        res = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if res == 0:
            print
            "[-] Error 2"
            return
        elif res == 1:
            child.sendline(password)

        child.expect('#')

        return child


if __name__ == '__main__':
    try:
        fp = frstphp()
        child = fp.connect()
        fp.send_command(child, 'w')

    except KeyboardInterrupt:
        print('stopped by 狂奔的螞蟻')