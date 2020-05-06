import pymysql
import threading
from decimal import Decimal
class MysqlUtils:
    # 创建锁
    _instance_lock = threading.Lock()
    # 修改new方法，使本类变成单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with MysqlUtils._instance_lock:
                if not hasattr(cls, '_instance'):
                    MysqlUtils._instance = super().__new__(cls)
        return MysqlUtils._instance
    def __init__(self,host_ip:str,host_user:str,host_pwd:str,db_name:str,host_port=3306):
        '''host_ip：数据库地址
            host_user：数据库账号
            host_pwd：数据库密码
            db_name：数据库名
            port：数据库端口，默认3306
            初始化完成后，可通过cursor来执行sql
        '''
        self.db = pymysql.connect(
            host=host_ip,
            user=host_user,
            password=host_pwd,
            db=db_name,
            port=host_port )
        self.cursor = self.db.cursor()
    def check_phone(self,phone:str) -> bool:
        '''检测手机号是否存在的快捷方法
        '''
        sql = f'select * from member where mobile_phone={phone}'
        self.cursor.execute(sql)
        ret = self.cursor.fetchall()
        if len(ret)>=1 :
            return False
        else:
            return True
    def get_exist(self) -> str:
        '''获得已存在用户的快捷方法
        '''
        sql = 'select mobile_phone from member limit 1'
        self.cursor.execute(sql)
        ret = self.cursor.fetchone()
        return str(ret[0])
    def check_amount(self,memberid:int) -> Decimal:
        '''传入用户memberid
        返回decimal类型的数据，比较时会准确
        '''
        sql = f'select leave_amount from member where id={memberid}'
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]
    def excute_other(self,sql_dict:dict) ->list:
        '''执行更多sql
        '''
        sql = str(sql_dict['sql'])
        need_commit = bool(sql_dict['commit'])
        fetch_count = str(sql_dict['fetch_count'])
        self.cursor.execute(sql)
        if need_commit:
            self.db.commit()
        ret_list = []
        if fetch_count.isalnum():
            for _ in range(int(fetch_count)):
                ret_list.append(self.cursor.fetchone())
        elif fetch_count == 'ALL':
            ret_list = [info for info in self.cursor.fetchall()]
        elif fetch_count == 'ONE':
            ret_list.append(self.cursor.fetchone())
        return ret_list
    def __del__(self):
        '''析构时必须关闭连接，避免连接数过多
        '''
        # print(dir(self))
        self.cursor.close()
        self.db.close()
