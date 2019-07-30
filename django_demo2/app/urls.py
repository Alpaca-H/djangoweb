from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('formOne/', views.NameForm),  # 基于函数的
    path('formTwoView/',views.formTwoView.as_view()), # 基于类的
    path('formPyView/',views.formPyView.as_view()), # 基于django自带的表单验证
]