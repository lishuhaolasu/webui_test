from copy import deepcopy
from common_utils import conf
login_success = [
    {
        'user_id': conf.get('common', 'user_id'),
        'user_pw': conf.get('common', 'user_pw'),
        'expected': 'https://www.ketangpai.com/Main/index.html'
    }
]
login_failed = [
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
    {'user_id': "yg12hg0h2",'user_pw': conf.get('common', 'user_pw'),'expected': '用户不存在'},
     {
        'user_id': conf.get('common', 'user_id'),
        'user_pw': conf.get('common', 'user_pw').lower(),
        'expected': '密码错误'
    }, {
        'user_id': '',
        'user_pw': '',
        'expected': '账号不能为空'
    }, {
        'user_id': conf.get('common', 'user_id'),
        'user_pw': '123',
        'expected': '密码有效长度是6到30个字符'
    }
]
