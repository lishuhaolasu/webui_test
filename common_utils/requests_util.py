import requests,json,time,base64
from common_utils.getlogger import logger
class RequestsUtil:
    # 下面的类属性用来存放一些公用信息
    url = 'http://api.lemonban.com/futureloan/'
    defult_headers = {
        'Content-Type' : 'application/json',
        'X-Lemonban-Media-Type' : 'lemonban.v1',
    }
    auth_headers = {
            'Content-Type' : 'application/json',
            'X-Lemonban-Media-Type' : 'lemonban.{}',
            'Authorization' : 'Bearer {}',
        }
    # paths = {
    #     'register' : 'member/register',
    #     'login' : 'member/login',
    #     'recharge' : 'member/recharge',
    #     'withdraw' : 'member/withdraw', 
    #     'add' : '/load/add', 
    # }
    token = ''
    # 老师提供的公钥是pkcs8的，转换成pkcs1后使用
    rsa_public = '''-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBANAQ1C6OQt9l9zlO71nUumvN50Q7cXuCz7tvOuA+wyXb0tfxSg9i8gbw
LrTgKmsFDgWR+cmmeFa7aW9QHRZnIurqwGu24+is5zjb6AucV/KEkDB1kHpKpZ8O
Dttb6M17kqLUO1TvPy4XobH5uUQwajwOD5KQqVkVzwGvtIe1sva1AgMBAAE=
-----END RSA PUBLIC KEY-----''' 
    def __init__(self):
        self.session = requests.session()

    def new_session(self):
        self.session.close()
        self.session = requests.session()
    def encrypt_sign(self,token:str) -> list:
        '''
        传入token
        返回一个列表[int,str]，第一个参数是时间戳，第二个参数是sign
        '''
        try:
            import rsa
        except ImportError :
            return [-1,'']
        pubkey = rsa.PublicKey.load_pkcs1(self.rsa_public.encode())
        timestamp = str(int(time.time()))
        raw_sign = token.split(' ')[1][:50] +timestamp
        sign = rsa.encrypt(raw_sign.encode('utf-8'),pubkey)
        sign = base64.b64encode(sign).decode()
        return [int(timestamp),sign]
    def request(self,path:str,method:str,jsons:dict,headers:dict) -> dict:
        '''path：测试的项目
            method：请求的方法
            json：请求体
            headers：请求头
            返回值：请求结果
        '''
        url = self.url+path
        if not method.lower() in ['get','post','put','patch'] :
            return {'code':-1024,'msg':'不受支持的请求方法'}
        try:
            rep = self.session.request(method=method,url=url,json=jsons,headers=headers)
            # logger.error(json.dumps([method,url,jsons,headers]))
        except:
            return {'code':-1025,'msg':'请求失败'}
        try:
            return rep.json()
        except:
            return {'code':-1026,'msg':'解析结果失败！'}

    def __del__(self):
        self.session.close()

if __name__ == "__main__":
    r= RequestsUtil()
    c=r.encrypt_sign('eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjk1OTg1NzMsImV4cCI6MTU4MjgxMDkxMH0.z1CTMDxXB-1qScpA4rNysn-9sgVhxMokQld6KXdfySLVPXp2-1-g6eJ--PBRKncsRoqjVUL5IEIR-tKTeYWAJg')
    print(c)