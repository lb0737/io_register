#models
from django.db import models

class io_register_model(models.Model):
    sex_choices = [
        (1 ,'男' ),
        (2 ,'女'),
        ( 0 ,'未知')
    ]
    name=models.CharField(max_length=32,verbose_name='姓名')
    sex=models.IntegerField(choices=sex_choices,verbose_name='性别')
    phone=models.CharField(max_length=16,verbose_name='电话')
    cid=models.CharField(max_length=18,verbose_name='身份证号')
    addr=models.CharField(max_length=128,verbose_name='住址')
    add_time=models.DateTimeField(auto_now=True,verbose_name='登记时间')
    @classmethod
    def get_all(cls):
        return cls.objects.all()
    #用于测试sex字段
    @property
    def sex_show(self):
        return dict(self.sex_choices)[self.sex]
    def __str__(self):
        return '出入人员<{}>'.format(self.name)
    class Meta:
        verbose_name=verbose_name_plural="出入登记"


