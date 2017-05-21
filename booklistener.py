# coding:utf-8
from config import cfg
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pyttsx
import io
import linecache
import pdb

if __name__ == '__main__':
  engine = pyttsx.init()
  _file = io.open(cfg.BOOK_PATH,'rU',encoding='utf-8')
  numLinePrefetch = cfg.PREFETCH_NUM
  startReadPoint = cfg.READ_RATIO

  # count the total lines
  totalLines = len(_file.readlines())#readlines could accept a parameters to indicate the sizeint to read! not the lines!
  print u"本文一共{}行".format(totalLines)
  _file.close()

  # start reading
  if startReadPoint<1:
      print u'从{}%的地方开始阅读'.format(startReadPoint * 100)
      startReadPoint = int(totalLines*startReadPoint)
  else:
      print u'从{}%的地方开始阅读'.format(startReadPoint * 100./totalLines)

  print u"从第{}行开始阅读".format(startReadPoint)
  processedLines=0
  while True:
    line =  linecache.getline(cfg.BOOK_PATH,startReadPoint+processedLines)
    if not line:
      break
    print '{}%[{}->{}]:{}'.format((startReadPoint+processedLines)*100./totalLines, startReadPoint, processedLines, line)
    engine.say(line)
    engine.runAndWait()
    processedLines += 1