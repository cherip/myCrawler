# copy big images to another dir
import os
import shutil

sdir = "../save"
for root, dirs, files in os.walk(sdir):
    for name in files:
        #print name
        #print root
        fullname = os.path.join(root, name)
        if os.stat(fullname).st_size < 10000:
            print fullname
            #os.remove(fullname)
            #os.rename(fullname, os.path.join(root, name + '.rm'))
