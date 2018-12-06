#!/usr/bin/python
# -*- coding: UTF-8 -*-
from f_cls import data
import os
import sys
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm, Inches, Pt
import jinja2
import time
import tkinter.messagebox
from tkinter import *
if sys.getdefaultencoding() != 'gbk': 
	reload(sys) 
	sys.setdefaultencoding('gbk')
class A:
     def __init__(self):
           self.obj=data()      
     def get(self):
          c=self.obj.get_order()
          for r in c:
                 r[3]=r[3]*r[4]*r[5]
                 del(r[4:6])
                 r.append(r[2]*r[1]*r[6])
                 r.append(r[3]*r[1])
                 r.append(r[4]*r[1])
                 r.append(r[5]*r[1])
                 r.append(r[6]*r[1])
          return c
class B:
     def __init__(self):
           d=A()
           self.data=d.get()
     def found(self,str):
            a1=a2=a3=a4=a5=a6=0
            for r in self.data:
                  if str==r[7]:
                       a1=a1+r[1]#箱数
                       a2=a2+r[10]#价格
                       a3=a3+r[11]#体积
                       a4=a4+r[12]#毛重
                       a5=a5+r[13]#净重
                       a6=a6+r[14]#数量
                       a7=r[7]#中文类别名
                       a8=r[8]#报关号
                       a9=r[9]#英文类别名
            return [a1,a2,a3,a4,a5,a6,a7,a8,a9]
     def li(self):
            d=set()
            for r in self.data:
                d.add(r[7])
            return d
     def get(self):
            d=[]
            l=self.li()
            for k in l:
                  d.append(self.found(k))
            return d
class C:
     def __init__(self):
           b=B()
           self.data=b.get()        
     def get(self):
            a0=a1=a2=a3=a4=a5=0
            for r in self.data:
                a0=a0+r[0]#箱数
                a1=a1+r[1]#价格
                a2=a2+r[2]#体积
                a3=a3+r[3]#毛重
                a4=a4+r[4]#净重
                a5=a5+r[5]#数量
            return [a0,a1,a2,a3,a4,a5]
class D:
      def get(self):
            obj=data()
            return obj.get_spc()  
 
ycl={}                    
a=A()
ycl["A"]=a.get()
b=B()
ycl["B"]=b.get()
c=C()
ycl["C"]=c.get()
d=D()
ycl["D"]=d.get()

for o in ycl["A"]:
     o.append("")

def exe1(filename): 
        try:
           tpl=DocxTemplate(os.path.dirname(os.path.realpath(__file__))+u"\\模板\\"+filename)
           for i in ycl["A"]:
                  if not os.path.exists(os.path.dirname(os.path.realpath(__file__))+u'\\数据\\'+i[0]+'.jpg'):
                      messagebox.showerror("错误：",i[0]+".jpg"+":图片不存在！")
                  i[-1]=InlineImage(tpl,os.path.dirname(os.path.realpath(__file__))+u'\\数据\\'+i[0]+'.jpg',Mm(20))
           tpl.render(ycl)
           tpl.save(os.path.dirname(os.path.realpath(__file__))+u"\\输出\\"+filename)
        except:
           messagebox.showerror("错误：",filename.encode('utf-8')+":文件错误")
for filename in os.listdir(os.path.dirname(os.path.realpath(__file__))+u"\\模板\\"):
       exe1(filename)