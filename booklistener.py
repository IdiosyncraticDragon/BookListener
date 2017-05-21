# coding:utf-8
from config import cfg
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pyttsx

if __name__ == '__main__':
  engine = pyttsx.init()
  _file = open(cfg.BOOK_PATH)
  numLinePrefetch = 100000
  while True:
    lines = _file.readlines(numLinePrefetch)
    if not lines:
      break
    for line in lines:
       print line
       engine.say(line)
       engine.runAndWait()
    engine.endLoop()
