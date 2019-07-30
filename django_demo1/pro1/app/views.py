from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from time import time
# Create your views here.


def display_view(request):
    now_time = time()
    return render(request,'index.html',{'hello':now_time})
    

class MyView(View):
    def get(self,request):
        now_time = time()
        string = "基于类的view视图"
        now_time = str(now_time)+string
        return render(request,'index.html',{'hello':now_time})
