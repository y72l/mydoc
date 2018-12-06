#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import tkinter.messagebox
from tkinter import *

class f_cls:
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
class data:
       def __init__(self):
            self.f=f_cls()
       def get_order(self):
            L=[]
            d=self.f.read_all(u"\\订单.txt")[0:-1]
            for r in d:
                  self.err(r)
                  d1=self.f.read_line(u"\\数据\\data.txt",r[0])
                  if d1==[]:
                        messagebox.showerror("错误：",str(r[0])+":产品不存在!")
                  d2=self.f.read_line(u"\\数据\\d.txt",d1[-1])
                  if d2==[]:
                        messagebox.showerror("错误：",str(d1[-1])+":产品类别不存在!")
                  L.append(r+d1[1:]+d2[1:])
            return L
       def get_spc(self):
            d=self.f.read_all(u"\\订单.txt")
            return d[-1]            
       def err(self,L):
            if len(L)<>3:
                  messagebox.showerror("错误：",str(L)+"数据个数错了!")
            if not isinstance(L[0],str):
                  messagebox.showerror("错误：",str(L[0])+":产品名错误！")
            if not isinstance(L[1],int):
                  messagebox.showerror("错误：",str(L[1])+":箱数错误")                 
            if not isinstance(L[2],(int,float)):
                  messagebox.showerror("错误：",str(L[2])+":价格错误") 