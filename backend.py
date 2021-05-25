import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user=os.environ.get("user"),
    passwd=os.environ.get("passwd"),
    database="libarysystem"
)

def createTable():
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS BookInformation (id int PRIMARY KEY AUTO_INCREMENT, memType VARCHAR(30), title VARCHAR(100), firstName VARCHAR(30), lastName VARCHAR(30), phone VARCHAR(10), bookID VARCHAR(20), author VARCHAR(50), dateBorrowed DATE, dateDue DATE )")
    mydb.commit()

def insertInfo(data):
    mycursor = mydb.cursor()
    try:
        sql_insert = "INSERT INTO BookInformation VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql_insert,data)
        mydb.commit()
    except:
        return 1

def displayInfo():
    mycursor = mydb.cursor()
    sql_info = "SELECT * FROM BookInformation"
    mycursor.execute(sql_info)
    result = mycursor.fetchall()
    return result 