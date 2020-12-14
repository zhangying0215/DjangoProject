from django.http import HttpResponse
from django.shortcuts import render

#第一个‘hello world’



def index(Request):
    return HttpResponse('hello world')


