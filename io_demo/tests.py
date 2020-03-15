#test.py
from django.test import TestCase,Client
from .models import io_register_model

class io_register_TestCase(TestCase):
    def setUp(self):
        io_register_model.objects.create(
            name='小脑斧',
            sex=1,
            phone='11223344551',
            cid='112233445566778899',
            addr='大深林',
        )
    def test_create_and_sex_show(self):
        io_register=io_register_model.objects.create(
            name='小松许',
            sex=1,
            phone='11223344552',
            cid='112233445566778811',
            addr='大深林',
        )
        self.assertEqual(io_register.get_sex_display,'男','性别字段和内容不一致')
    def test_filter(self):
        io_register_model.objects.create(
            name='小松许',
            sex=1,
            phone='11223344552',
            cid='112233445566778811',
            addr='大深林',
        )    
        name='小脑斧'
        io_registers=io_register_model.objects.filter(name=name)
        self.assertEqual(io_registers.count(),1,'存在重复记录名字{}'.format(name))
    
    #view层的测试
    def test_get_index(self):
        client=Client()
        response=client.get('/')
        self.assertEqual(response.status_code,200,'status code 200!')
    def test_post_io_register(self):
        client=Client()
        data=dict(
            name='test_post',
            sex=1,
            phone='11223344552',
            cid='112233445566778811',
            addr='大深林',
        )
        response=client.post('/',data)
        self.assertEqual(response.status_code,302,'statuc code 302!')
        response=client.get('/')
        self.assertTrue(b'test_post' in response.content,'response content must contain "test_post')

#test_create_and_sex_show 用来测试数据创建以及sex字段的正确展示,test_filter测试查询是否可用。
#配置了choices参数的字段,Django提供了get_xxxx_display方法用于替换show_xxx
