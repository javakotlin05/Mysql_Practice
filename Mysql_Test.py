import pymysql as sql
from prettytable import PrettyTable
x = sql.connect(host='localhost',
                port=3306,
                user='root',
                db='homework',
                password='')

c = x.cursor()

b = input('(0)=離開程式 \n (1)=顯示會員列表 \n (2)=新增會員資料 \n (3)=更新會員資料 \n (4)=刪除會員資料 \n 指令:')
a = PrettyTable(['編號','姓名','生日','地址'])

while True:
    if int(b) == 0:
        break
    elif int(b) == 1:
        c.execute("select * from `member`")
        d = c.fetchall()
        for i in d:
            a.add_row(i)
        print(a)
        b = input('(0)=離開程式 \n (1)=顯示會員列表 \n (2)=新增會員資料 \n (3)=更新會員資料 \n (4)=刪除會員資料 \n 指令:')
    elif int(b) == 2:
        # 這種寫法要記一下..有時候不能單寫%的寫法，要配上字典，而且這種字典後面都是%()s 都是s 沒有d
        data = {}
        data['name'] = input('請輸入會員姓名:')
        data['birthday'] = input('請輸入會員生日:')
        data['address'] = input('請輸入會員地址:')
        c.execute("insert into `member`(`name`,`birthday`,`address`) values(%(name)s,%(birthday)s,%(address)s)",data)
        b = input('(0)=離開程式 \n (1)=顯示會員列表 \n (2)=新增會員資料 \n (3)=更新會員資料 \n (4)=刪除會員資料 \n 指令:')
    elif int(b) == 3:
        se = {}
        se['p'] = int(input('請選擇要修改的資料編號:'))
        se['n'] = input('請輸入會員姓名:')
        se['b'] = input('請輸入會員生日:')
        se['a'] = input('請輸入會員地址:')
        c.execute("UPDATE `member` SET `name`=%(n)s ,`birthday`=%(b)s ,`address`=%(a)s where `id`=%(p)s",se)
        b = input('(0)=離開程式 \n (1)=顯示會員列表 \n (2)=新增會員資料 \n (3)=更新會員資料 \n (4)=刪除會員資料 \n 指令:')
    elif int(b) == 4:
        q = int(input('請選擇你要刪除的資料編號:'))
        c.execute("delete from `member` WHERE `id`=%d" %(q))
        b = input('(0)=離開程式 \n (1)=顯示會員列表 \n (2)=新增會員資料 \n (3)=更新會員資料 \n (4)=刪除會員資料 \n 指令:')
x.commit()
x.close()
c.close()