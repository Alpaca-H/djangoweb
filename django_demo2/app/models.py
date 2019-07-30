from django.db import models

# Create your models here.


class FormModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)

    class Meta():
        verbose_name = "表单字段"
        verbose_name_plural = verbose_name
        db_table = "formModel"