---
title: Django配置
date: 2019/07/26 19:25:00
tags: [Python,Django]
categories: Django
---
<!-- more -->


# Django各类配置


### 动作方法配置
#### action view

```Python
#  基于函数的视图方法
def my_view(request):
    if request.method == 'GET':
        return HttpResponse('result')

# 基于类的视图方法
from django.views.generic.base import View
class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')

# 关闭django 类视图的使用流程
https://docs.djangoproject.com/zh-hans/2.2/topics/class-based-views/intro/

```




---------------------------------------------


###  路由配置
#### 路由跳转配置
```Python

# pro
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
]

# app

from django.urls import path
from . import views
urlpatterns = [
    path('',views.display_view)
]


# 基于类的View视图方法
from myapp.views import MyView
urlpatterns = [
    path('mine/', MyView.as_view(), name='my-view'),
]

```

### 数据库模型配置
#### (Mode_py)Meta配置
https://docs.djangoproject.com/zh-hans/2.2/ref/models/options/#table-names
Meta配置都在class Meta下
```Python
class Meta:
# 创建数据库的时候 自定义数据库的名字
db_table = "xxx"
# 设置别名
verbose_name = "xxx"
# 使用别名
verbose_name_plural = verbose_name
```

#### (Mode_py)模型字段
https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/#model-field-types
自定义模型字段
https://docs.djangoproject.com/zh-hans/2.2/howto/custom-model-fields/

每一种字段类型都需要指定一些特定的参数，如CharField需要接受一个max_length参数

当然也有一些通用的参数,
null 如果设置为 True，当该字段为空时，Django 会将数据库中该字段设置为 NULL。默认为 False .

blank 如果设置为 True,该字段允许为空。注意该选项与 False 不同， null 选项仅仅是数据库层面的设置，然而 blank 是涉及表单验证方面。如果一个字段设置为 blank=True ，在进行表单验证时，接收的数据该字段值允许为空，而设置为 blank=False 时，不允许为空。

Choices

default

help_text

primary_key

unique

**自动设置主键**
默认情况下 ,django会有自己的序号(作为主键)
id = models.AutoField(permary_key=True)
如果你在自己创建的字段中使用了permary_key则不会在表中自动添加id列