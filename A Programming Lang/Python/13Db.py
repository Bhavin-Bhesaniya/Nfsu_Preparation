'''
#Using Connection Class :-
from mysql.connector import connection
connectionObj2 = connection.MySQLConnection(host='localhost',user='root', password='1234@')
print(connectionObj2)
'''


import mysql.connector  
connectionObj = mysql.connector.connect(host='localhost',user='root', password='1234@')
#connectionObj = mysql.connector.connect(host='localhost',user='root', password='1234@',database='bhavin') #Used with database connection


#Create Cursor :-
cursorObj = connectionObj.cursor()

#Create Database :-
cursorObj.execute('create database bhavin')
print("Table Created")


#Create Table :- 
#cursorObj.execute("CREATE TABLE StudId (NAME VARCHAR(20) NOT NULL,Email VARCHAR(50))")

sql = "INSERT INTO StudId (Name, Email) VALUES (%s, %s)" #formate specifiers
val = ("Ram", "85")
valMulti = [("bhavin","21"),("bhesaniya"),("22")]  
cursorObj.execute(sql, val)            #Containe query, list of values
#cursorObj.executeMany(sql, valMulti)   #insert multiple values at once
#cursorObj.execute("Update StudId set name='AHAVIN' where Email = 85")


cursorObj.execute("select * from studid")
for x in cursorObj.fetchall():
    print(x)

print("\nFetchMany : ")    
for x in cursorObj.fetchmany(size=3):
    print(x)

# for x in cursorObj.fetchone():
#     print(x)

print("\nUsing Limit :\n")
cursorObj.execute("select * from studid limit 2")
for x in cursorObj.fetchall():
    print(x)

print("\nUsing Order By :\n")
cursorObj.execute("select * from studid ORDER BY name AESC")
for x in cursorObj.fetchall():
    print(x)

#print(cursorObj.rowCount())

cursorObj.execute("Delete from studid where name='AHAVIN'")
cursorObj.execute("Drop table if exists studid")

connectionObj.commit()
connectionObj.close()