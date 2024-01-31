
import mysql.connector as my
from typing import Any
class Database:
    con:Any=None
    @staticmethod
    def getConnection()->Any:    
        try:
            if Database.con==None :
                Database.con=my.connect(

                    user='root',
                    password='1234',
                    database='db_hosts',
                    host='db'
                )
        except :
            pass
        return Database.con
class IotDao:
    @staticmethod
    def getAllTemp():
        con=Database.getConnection()
        
        cursor=con.cursor()
        cursor.execute('SELECT * from iot_device')
        return cursor.fetchall()
    @staticmethod
    def add(device):
        con=Database.getConnection()
        cursor=con.cursor()
        cursor.execute('INSERT INTO iot_device values()')


