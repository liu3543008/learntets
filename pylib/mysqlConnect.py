import pymysql
from config import dbinfo,database
class MysqlConnect():
    def __init__(self,db_cof,database):
        self.db_cof=db_cof
        self.db= pymysql.connect(database=database,cursorclass=pymysql.cursors.DictCursor,**db_cof)
        self.cursor=self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #        WHERE INCOME > %s" % (1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
           # 执行SQL语句
           self.cursor.execute(sql)
           # 提交修改
           self.db.commit()
        except:
           # 发生错误时回滚
           self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()
# if __name__=="__main__":
#     one =MysqlConnect(dbinfo,database)
#     one.execute('CREATE TABLE test0(id int(11) NOT NULL,name  varchar(128) NOT NULL, street varchar(10) NOT NULL,email  varchar(10) NOT NULL,phone  varchar(128) DEFAULT NULL,PRIMARY KEY (`id`),KEY `NIHAO` (`name`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;')
#  #   one.execute("CREATE TABLE test1(id int(11) NOT NULL,name  varchar(128) NOT NULL, street varchar(10) NOT NULL,email  varchar(10) NOT NULL,phone  varchar(128) DEFAULT NULL,PRIMARY KEY (`id`),KEY `NIHAO` (`name`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
#     one.execute("INSERT INTO `test0`(`id`, `name`, `street`, `email`, `phone`) VALUES (1, '李白', '3', '10010', '123456'),(2, '梨花', '3', '10011', '123456'),(3, '黄忠', '3', '10012', '123456'),(4, '孙尚香', '3', '10013', '123456'),(5, '杨立华', '3', '10014', '123456'),(6, '23', '23', '23', '23');")
#     one.close()
