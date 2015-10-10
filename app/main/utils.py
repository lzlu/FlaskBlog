# -*- coding:utf-8 -*-
from datetime import datetime

__author__ = 'lulizhou'


def fromtimestamp2year(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y')

def fromtimestamp2date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%m-%d')

print(datetime.t)