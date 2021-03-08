#coding=utf8
from pylib.mysqlConnect import MysqlConnect
from config import dbinfo,database
import time

if __name__=="__main__":
 str="create table zy_test1( id int(10),name char(12));"

 db = MysqlConnect(dbinfo, database)

 for i in range(10000):
    a="CREATE TABLE test%s(id int(11) NOT NULL,name  varchar(128) NOT NULL, street varchar(10) NOT NULL,email  varchar(10) NOT NULL,phone  varchar(128) DEFAULT NULL,PRIMARY KEY (`id`),KEY `NIHAO` (`name`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;"% i
    b="INSERT INTO test%s(`id`, `name`, `street`, `email`, `phone`) VALUES (1, '李白', '3', '10010', '123456'),(2, '梨花', '3', '10011', '123456'),(3, '黄忠', '3', '10012', '123456'),(4, '孙尚香', '3', '10013', '123456'),(5, '杨立华', '3', '10014', '123456'),(6, '23', '23', '23', '23');"% i
    # print(a)
    # print(b)

    db.execute(a)

    db.execute(b)
 db.close()







