# -*- coding:utf-8 -*-
from datetime import datetime
from app import logger
import os

__author__ = 'lulizhou'


def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        logger.info('create dir {}'.format(dir))
    return dir


def mkdirbydate(parent, date=None):
    date_dir = datetime.today().strftime("%y-%m-%d") if not date else date.strftime("%y-%m-%d")
    dir = os.path.join(parent, date_dir)
    return mkdir(dir), date_dir

this_dir = mkdirbydate("../static/uploads/")