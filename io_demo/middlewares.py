#middlewares.py
import time
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeitMiddleware(MiddlewareMixin):
    def process_request(self,request):
        self.start_time=time.time()
        return
    def process_view(self,request,func,*args,**kwargs):
        if request.path !=reverse('index'):
            return None
        start=time.time()
        response=func(request)
        costed=time.time()-start
        print('process view:{:.2f}s'.format(costed))
        return response
    def process_exception(self,request,exception):
        pass
    def process_template_esponse(self,request,response):
        return response
    def process_response(self,request,response):
        costed=time.time()-self.start_time
        print('request to response cose:{:.2f}s'.format(costed))
        return response
'''
*process_request:这是请求来到middleware中时进入的第一个方法 。
*process_view:这个方法是在process_request方法之后执行的,参数如上面代码
所示,其中func就是我们将要执行的view方法。因此,如果要统计一个view 的执行
时间,可以在这里做.它的返回值跟process_request一样,是HttpResponse或者
None,其逻辑也一样.如果返回None,那么Django会帮你执行vies函数,从而得到最终的response.
*process_template_response:执行完上面的方法,并且Django帮我们执行完View,
拿到最终的response后,如果使用了模板的response就会来到这个方法中.在这个方法中,我们
可以对response做一下操作,比如Content Type 设置,或者其他header的修改|增加.
*process_response:当所有流程都处理完毕后,就来到了这个方法.这个方法的逻辑跟process_template_response 
是完全一样的,只是后者是针对带有模板的response的处理。
*process_exception:上面的处理方法是按顺序介绍的,而这个方法不太一样.只有在发生异常时,
才会进入这个方法,哪个阶段发生的异常呢？可以简单理解为在将要调用的View中出现异常
（就是在process_view的func函数中）或者返回的模板response在渲染时发生的异常.但是需要
注意的是,如果你在process view中手动调用了func,就像我们上面做的那样,就不会触发 process_exception了.
这个方法接收到异常之后,可以选择处理异常,然后返回一个含有异常信息的HttpResponse,或者直
接返回None不处理,这种情况下Django 会使用自己的异常模板.
'''