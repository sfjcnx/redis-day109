

#################   丐版    ##############
# import redis
#
# conn = redis.Redis(host='10.0.0.210',port=6379,password=123456)
#
# conn.set("x1","111",ex=5)
# val = conn.get('x1')
#
# print(val)



#################   毛坯板    ##############

#  连接池
'''
host ip; port  端口;
password  密码
max_connections  最大连接数
'''
# import redis
# pool = redis.ConnectionPool(host='10.211.55.4',port=6379,password="123456",max_connections=1000)
# conn = redis.Redis(connection_pool=pool)
#
# conn.set('foo',"bar")

#################  精装修    ##############

import redis
from redis_pool import POOL
while True:
    key=input('请输入key:')
    value=input('请输入value')

    # 去连接池中获取连接
    conn=redis.Redis(connection_pool=POOL)
    ## 设置值
    conn.set(key,value)

