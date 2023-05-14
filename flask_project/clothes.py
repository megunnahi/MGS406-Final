import mysql.connector as sql

conn = sql.connect(host = 'localhost', user = 'James', password = 'bob14228')
cur = conn.cursor()

print(conn)

cmd = "CREATE DATABASE clothing_store"
cur.execute(cmd)

conn.close()

conn2 = sql.connect(host = 'localhost', user = 'James', password = 'bob14228', database = 'clothing_store')
cur2 = conn2.cursor()

tbl = "CREATE TABLE customer (CustID varchar(30) PRIMARY KEY, CustName varchar(30), CustGender varchar(30), CustPhone varchar(30), CustOrder varchar(30), arrivalDate varchar(30))"
cur2.execute(tbl)

conn2.close()
