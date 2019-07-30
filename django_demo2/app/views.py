from django.shortcuts import render
from django.views import View
from django.views.generic.base import View,TemplateView
from .models import FormModel
from django.http import HttpResponse
from  .form import FormTemp
# Create your views here.

def index(request):
    print("跳转首页")
    return render(request,'formindex.html')


def NameForm(request):
    """
    基于函数方法的form表单传递
    :param request:
    :return: response
    """
    if request.method == 'POST':
        name = request.POST.get('name','')
        passwd = request.POST.get('password','')
        sex = request.POST.get('sex','')
        message = "榜单提交成功{0}{1}{2}".format(name,passwd,sex)
    else:
        message = "提交失败"
        print(message)
    return render(request,'hasthing.html',{'message':message})

# 基于类的form表单传递
class formTwoView(View):

    def get(self,request):
        return HttpResponse("这是get,基于类的form表单传递")

    def post(self,request):
        return HttpResponse("这是post,基于类的form表单传递")

# 基于django自带的表单验证
# 表单错误：https://docs.djangoproject.com/zh-hans/2.2/topics/forms/
# 使用基于类的视图处理表单：https://docs.djangoproject.com/zh-hans/2.2/topics/class-based-views/generic-editing/
class formPyView(View):
    def post(self,request):
        form = FormTemp(request.POST)
        if form.is_valid():
            # form.cleaned_data['name'] # 不知道干嘛的。。
            message = "表单验证成功,基于django自带的表单验证"
            return render(request,'formindex.html',{'message':message})
        else:
            print(type(form.errors))
            message = form.errors
            return render(request, 'hasthing.html', {'message': message})
