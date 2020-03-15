#views.py
from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import io_register_model
from .forms import io_register_Form


class index(View):
    template_name='index.html'#定义变量存储模版
    def get_context(self):
        context={
            'contexts':io_register_model.get_all()
        }
        return context
    def post(self,request):
        form=io_register_Form(request.POST)
        if form.is_valid():
            form.save()#保存数据
            return HttpResponseRedirect(reverse('index'))
        else:
            context=self.get_context()
            context.update({'form':io_register_Form()})
            errors = form.errors
            return render(request,self.template_name,context=context)
    def get(self,request):
        context=self.get_context()
        context.update({'form':io_register_Form()})
        return render(request,self.template_name,context=context)
