from  django import forms

# url :https://docs.djangoproject.com/zh-hans/2.2/topics/forms/

# 通过django自带的forms类来构建form表单
class FormTemp(forms.Form):
    password = forms.CharField(max_length=1)
    name = forms.CharField(max_length=1)
    sex = forms.CharField(max_length=100,empty_value='不男不女')