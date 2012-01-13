# -*- coding: utf-8 -*-

# try to get key words from 
# the alt information

from pymmseg import mmseg
import os

def format_img_name(index):
    formatIndex = str(100000 + int(index))
    formatIndex = 'f' + formatIndex[1:]
    return formatIndex


def read_file(pfile, fullDir, dicts):
    line = pfile.readline() 
    while line:
        words = line.split()
        line = pfile.readline()

        #print words[0], words[1] 
        imgName = format_img_name(words[0])
        if words[1].find('n0') > 0:
            os.rename(os.path.join(fullDir, imgName), 
                      os.path.join(fullDir, imgName + '.jpg'))
            #dicts[words[1]] = os.path.join(fullDir, imgName)
        else:
            #print os.path.join(fullDir, imgName)
            #print os.path.join(fullDir, imgName + '.jpg')
            os.remove(os.path.join(fullDir, imgName))
            
            #os.rename(os.path.join(fullDir, imgName), 
            #      os.path.join(fullDir, imgName + '.jpg'))
#  for url in dicts.keys():
#      print dicts[url]
        #os.rename(dicts[url], dicts[url] + '.jpg')

sdir = "../save"
def read_dir():
    dicts = dict()
    for root, dirs, files in os.walk(sdir):
        for _dir in dirs:
            fullDir = os.path.join(root, _dir)  
            indexFile = os.path.join(fullDir, 'index')
            pfile = open(indexFile)
            read_file(pfile, fullDir, dicts)
            pfile.close()
    return dicts
    #print dicts

def start_with(src, dst):
    if src.find(dst) != 0:
        return 0
    else:
        return 1
def format_url(url):
    pos = url.find(':80')
    if pos != 0:
        newurl = url[0:pos] + url[pos + 3:]
        return newurl
    else:
        return url

altpath = '../fifoimage000000'
def read_alt_info():
    pfile = open(altpath)
    text = pfile.read()
    keyword = 'http://'
    pos = 0
    allpos = list()
    while True:
        pos = text.find(keyword, pos)
        if pos < 0:
            break
        allpos.append(pos)
        pos += len(keyword)
    allpos.append(len(text))

    dicts = dict()
    for i in xrange(len(allpos) - 1):
        infos = text[allpos[i]:allpos[i + 1] - 1].split()
        url = infos[0]
        url = format_url(url)
        info = ''
        for item in infos[1:]:
            info += item
        #print url, info
        dicts[url] = info
        #print dicts[url]

    return dicts

url2imgfile = read_dir()
#url2imginfo = read_alt_info()

#mmseg.dict_load_defaults()
#for url in url2imginfo.keys():
#  print url, len(url)
#print '***************'
#for url in url2imgfile.keys():
#  if url2imginfo.has_key(url) == True:
#      print '*************'
#      print url2imginfo[url]
#      segs = mmseg.Algorithm(url2imginfo[url])
#      for tok in segs:
#          print tok.text
#  else:
#      print url, len(url)
