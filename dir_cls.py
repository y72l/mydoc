#!/usr/bin/python
# coding:utf-8
import os
class dir_cls:
       def __init__(self):
             self.path=os.path.dirname(os.path.realpath(__file__))
       def get(self,path):
             return os.listdir(self.path+path)
       def file(self,path,s):
             L=[]
             d=self.get(path)
             for k in d:
                 arr=k.split(".")
                 if len(arr)==2:
                      if s=="*":
                         L.append(k)
                      if arr[1]==s:
                         L.append(k)
             return L
       def dir(self,path):
             L=[]
             d=self.get(path)
             for k in d:
                 arr=k.split(".")
                 if len(arr)==1:
                         L.append(k)
             return L