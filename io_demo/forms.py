from django import forms
from .models import io_register_model

class io_register_Form(forms.ModelForm):
    def clean_phone(self):
        data=self.cleaned_data['phone']
        if not data.isdigit() and len(data)!=11:
            raise forms.ValidationError('电话必须是数字且长度为11位！')
        return int(data)
    def clean_cid(self):
        data=self.cleaned_data['cid']
        if not ((len(data)==15)|(len(data)==18)):
            raise forms.ValidationError('身份证号码长度不正确,15位或18位,当前长度{}！'.format(len(data)))
        return data
    class Meta:
        model=io_register_model
        fields=('name','sex','phone','cid','addr')


