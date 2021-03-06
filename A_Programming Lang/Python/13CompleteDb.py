import mysql.connector
import re
import smtplib
import os

class vendor: 
    username = "bhavin.otp2021@gmail.com" 
    password = "Bh@vin12Op" 
    
    mydb = mysql.connector.connect(host = "localhost",user = 'root',password = "1234@",database='vendor')
    cur = mydb.cursor() 


    def del_all_rec(this):
        print("\t\tDELETE ALL RECORDS\n")
        username = input("\tUSERNAME :")
        password = input("\tPASSWORD :")
        if(username == "admin" and password == "admin"):
            op = input("\t\Aare you sure delete all record ?(y/n)")
            if(op == "y" | "Y"):
                this.cur.execute("truncate table info")
                this.mydb.commit()
            else:
                return False                
        else:
            os.system('cls')
            print("\tPlease enter currect username and password or  :(")
            this.del_all_rec()
    

    def is_email_true(this,email):
        #use regular expresion
        match = re.match("[a-zA-Z0-9]+@[a-zA-Z]+[.]+[a-zA-Z]",email)
        if match:
            return True
        else:
            return False
    

    def sendMail(this,to,sub,msg):
        #print(f"\t\temail to {to} send with subject is:{sub} and Message {msg}")
        print("\t\temail sending ...")
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(this.username,this.password)
        s.sendmail(this.username,to,f"subject: {sub}\n\n{msg}")
        s.quit()
    

    def add_new_vendor(this):
        print("\t\t===============ADD NEW VENDOR===============")        
        name  = input("\tEnter Name :")
        ct    = input("\tEnter city :")
        email = input("\tEnter email :")
        phno  = input("\tEnter phone no :")

        if(this.is_email_true(email)):
            data = (name,ct,email,phno)
            this.cur.execute("insert into info(name,ct,email,phno) values(%s,%s,%s,%s)",data)
            this.mydb.commit()
            this.sendMail(email,"signup complete",f"hello mr {name} you registrastion complete\n Your information check \n\tname={name}\n\tcity={ct}\n\tphone no={phno}")
            print("\t\tRegister successfuly : "+name)    
        else:
            print("Email id is wrong try again")
            this.add_new_vendor() # recursion
        
        
    def update_vendor(this):
        print("\t\t===============UPDATE VENDOR===============")
        no = input("\t\tEnter id :")
        
        confirm = input("\t\tDo you want to update name :?y/n")        
        if(confirm == "y"):
            name = input("\t\tEnter Name :")
            this.cur.execute("update info set name='"+name+"' where id='"+no+"'")
            this.mydb.commit()
        confirm = input("\t\tDo you want to update ct :?y/n")
        
        if(confirm == "y"):
            ct = input("\t\tEnter city :")
            this.cur.execute("update info set ct='"+ct+"' where id='"+no+"'")
            this.mydb.commit()
        confirm = input("\t\tDo you want to update email :?y/n")
        
        if(confirm == "y"):
            email = input("\t\tEnter email :")
            this.cur.execute("update info set email='"+email+"' where id='"+no+"'")
            this.mydb.commit()
        confirm = input("\t\tdo you want to update phone no :?y/n")
        
        if(confirm == "y"):
            phno = input("\t\tenter phone no :")
            this.cur.execute("update info set phno='"+phno+"' where id='"+no+"'")
            this.mydb.commit()
        print("\t\tupdate record ",no)


    def delete_vendor(this):
        print("\t\t===============DELETE VENDOR===============")
        no = int(input("\t\tEnter Id :"))
        this.cur.execute(f"delete from info where id={no}") # use f string
        this.mydb.commit();
        print("\t\tdelete successsfuly id is ",no)


    def show_vendor(this):
        print("\t\t===============ALL VENDOR===============")
        cur = this.mydb.cursor()
        cur.execute("select * from info")  
        print("\t\tid      name      city      email      phoneno")
        for rec in cur:
            print("\t\t",rec[0],"   ",rec[1],"   ",rec[2],"   ",rec[3],"   ",rec[4])
    

    def show_specific_rec(this):
        print("\t\t===============VENDOR INFO===============")
        no = input("\t\tEnter id :")
        cur = this.mydb.cursor()
        cur.execute("select * from info where id = '"+no+"'")

        for rec in cur:
            #print(rec[0],"\t",rec[1],"\t",rec[2],"\t",rec[3],"\t",rec[4])
            print("\t\tvendor id :",rec[0])
            print("\t\tname :",rec[1])
            print("\t\tcity :",rec[2])
            print("\t\temail :",rec[3])
            print("\t\tphone no :",rec[4])

        
    def sendmsg(this):
        to  = input("\t\tEnetr Mail :")
        sub = input("\t\tEnter Sub :")
        msg = input("\t\tEnter Your Message :")
        this.sendMail(to,sub,msg)
        print(f"\t\tmessage is sending -> {to}")


    def show_option(this):
        print("\n\n")
        print("\t\t===============ALL OPTIONS===============")
        print("\t1.Add new vendor")
        print("\t2.Delete vendor")
        print("\t3.Show vendor")
        print("\t4.Update vendor")
        print("\t5.Display specific vendor")
        print("\t6.Delete all record ( !!!please read again!!!)")
        print("\t7.Send message to other")
        print("\t0.Exit")
        print("\n")

'''
class admin(vendor):
    def login(this):
        username = input("Username :")
        password = input("Password :")
        cur = super().mydb.cursor()
        usr = cur.execute("select * from admin")        
        for x in cur:
            if(x[0]==username and x[1]==password):
                return True
            else:
                return False             
        super().mydb.commit()    
obj = admin()
'''
ven = vendor() # create obj

#if obj.login():
while True:
    os.system('cls')
    ven.show_option()
    op = int(input("\t\tselect :"))
    if(op == 1):
        ven.add_new_vendor()
        input()
    elif(op == 2):
        ven.delete_vendor()
        input()
    elif(op == 3):
        ven.show_vendor()
        input()
    elif(op == 4):
        ven.update_vendor()
        input()
    elif(op == 5):
        ven.show_specific_rec()
        input()
    elif(op == 6):
        ven.del_all_rec()
        input()
    elif(op == 7):
        ven.sendmsg()
        input()
    elif(op == 0):
        break
    else:
        print("\t\tPlease enter valid choice")