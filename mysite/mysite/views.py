# coding:utf-8
from django.shortcuts import render
 
 
def home(request):
    A={}
    A["hello"]="hello World!"
    return render(request, 'home.html',A)