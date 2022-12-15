import pymysql
#连接数据库
conn = pymysql.connect(
    host="localhost",
    user="root",
    passwd="123456",
    db='lyc',
    charset='utf8',
    #autocomint=True,
)
#创建游标对象,用来给数据库发送sql语句
#c创建游标对象
cur = conn.cursor()
#对数据库增删改查

#创建数据表
# try:
#     create_sql = "create table author (id int,name varchar(30));"
#     cur.execute(create_sql)
# except Exception as e:
#     print("创建数据表失败: ",e)
# else:
#     print("创建数据表成功: ")

#插入数据
# try:
#     insert_sql = "insert into author values(2,'jxy');"
#     cur.execute(insert_sql)
# except Exception as e:
#     print("插入数据失败: ",e)
# else:
#     #插入数据一定要提交数据，不然数据库中找不到插入的数据
#     conn.commit()
#     print("插入数据插入成功: ")

#查询
# select_sql = "select * from author;"
# result = cur.execute(select_sql)
# print(result)
# print(cur.fetchone()) #获取下一个查询结果集
# print(cur.fetchmany(2))  #获取指定个数个查询结果集;
# info = cur.fetchall()  #获取的查询结果;
# print(info)
#关闭游标
# cur.close()
#关闭连接
# conn.close()