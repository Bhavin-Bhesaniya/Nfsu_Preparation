import mysql.connector  
# connectionObj = mysql.connector.connect(host='localhost',user='root', password='1234@')
# cursorObj.execute("create database usertest")

connectionObj = mysql.connector.connect(host='localhost',user='root', password='1234@', database='usertest')
cursorObj = connectionObj.cursor()
#cursorObj.execute("CREATE TABLE usertable(NAME VARCHAR(20) NOT NULL,Email VARCHAR(50))")
sql = "INSERT INTO usertable(Name, Email) VALUES (%s, %s)" #formate specifiers
val = ("Ram", "85")
cursorObj.execute(sql, val)

cursorObj.execute("select * from usertable")
for x in cursorObj.fetchall():
    print(x)

cursorObj.execute("Delete from usertable where name='Ram'")
connectionObj.commit()