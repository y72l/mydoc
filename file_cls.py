#!/usr/bin/python
# coding:utf-8
import os
class file_cls:
       def __init__(self):
             self.path=os.path.dirname(os.path.realpath(__file__))
       def read(self,path):
             with open(self.path+path) as f:
                  for line in f:
                       line=line.split(",") 
                       line=self.filter(line)
                       yield line
       def is_number(self,s):
           try:
              float(s)
              return True
           except ValueError:
              pass
           try:
              import unicodedata
              unicodedata.numeric(s)
              return True
           except (TypeError, ValueError):
              pass
           return False
       def filter(self,L):
             d=[]
             for r in L:
                 r=r.replace("\n","")
                 r=r.replace("\xef\xbb\xbf","")
                 r=r.strip()
                 r=r.lower()
                 if self.is_number(r):
                      r=eval(r)
                 d.append(r)
             return d
       def read_all(self,path):
             d=[]
             for r in self.read(path):
                 d.append(r)
             return d
       def read_line(self,path,s):
             d=[]
             for r in self.read(path):
                   if s in r:
                       d=r
                       break
             return d
       def write(self,filename,s):
             fo = open(self.path+filename, "w")
             fo.write('\xEF\xBB\xBF'+s)
             fo.close()
       def add(self,filename,s):
             fo = open(self.path+filename, "a")
             fo.write("\n"+s)
             fo.close() 