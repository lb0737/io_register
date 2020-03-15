from django.contrib import admin
from django.urls import path
from io_demo.views import index
urlpatterns = [
    path('',index.as_view()),
    path('index',index.as_view(),name='index'),
    path('admin/', admin.site.urls),
]
