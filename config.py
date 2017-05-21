#coding:utf-8
from easydict import EasyDict as edict
import os.path as osp

__C = edict()
cfg = __C

__C.BOOK_ROOT = './bookLib'
__C.BOOK_NAME = u'蛊真人.txt'
__C.BOOK_PATH = u'{}/{}'.format(__C.BOOK_ROOT,__C.BOOK_NAME)
