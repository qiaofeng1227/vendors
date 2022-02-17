#!/usr/bin/env python2
#!/usr/bin/env python3
#coding: utf-8

import os, io, sys, platform, shutil, urllib3, time, json


def ReadLists(filename):
    if os.path.getsize(filename) == 0:
        print("\n清单中没有项目！")
        sys.exit()
    else:
        with open("./"+filename,mode='r',newline='') as f:
          templists=list(f)
          rlist=[]
          for templist in templists:
              rlist.append(templist.replace('\n',''))
          return rlist
      
mylists=ReadLists("lists")

# 批量处理，创建项目文件夹，issue
for mylist in mylists:
    os.system("mkdir "+mylist)
    print("处理 "+mylist+" ...\n")
    path=os.getcwd()+"/"+mylist+"/README.md"
    if not os.path.exists(path):
      os.system("jinja2 README.jinja2 -D name="+mylist+" > "+mylist+"/README.md")
    os.system("echo '' > lists")

print("\n执行完成，并清空列表")
