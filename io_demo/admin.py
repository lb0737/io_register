#admin.py
from django.contrib import admin
from .models import io_register_model

class io_register_Admin(admin.ModelAdmin):
    list_display=('id','name','sex','phone','cid','addr','add_time')#admin后台显示的字段
    list_filter=('sex','add_time')#筛选
    search_fields=('name','phone','cid','addr')#搜索
    fieldsets=(
        ('人员信息-姓名',{'fields':['name','sex','cid']}),
        ('人员信息-联络方式',{'fields':['phone','addr']}),
    )
admin.site.register(io_register_model,io_register_Admin)
