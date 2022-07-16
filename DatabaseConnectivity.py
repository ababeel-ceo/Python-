import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(host="localhost", user="root", password="", database="student")


class DataBaseConnectivity:
    def insert(self, name, age, dep):
        con = connection.cursor()
        param = (name, age, dep)
        sql = "insert into stud1 (name,age,dep) values (%s,%s,%s)"
        con.execute(sql, param)
        print("Successfully Inserted")

    def select(self):
        con = connection.cursor()
        sql = "select id, name, age, dep from stud1"
        con.execute(sql)
        result = con.fetchall()
        print(tabulate(result, headers=["ID", "NAME", "AGE", "DEPARTMENT"]))

    def delete(self, id):
        con = connection.cursor()
        sql = "delete from stud1 where id =%s"
        param = (id,)
        con.execute(sql, param)
        print("Successfully Deleted")

    def update(self, name, age, dep, id):
        con = connection.cursor()
        sql = "update stud1 set name=%s, age=%s, dep=%s where id=%s"
        param = (name, age, dep, id)
        con.execute(sql, param)
        print("Updated Succesfully")

    def info(self):
        print("1.Insert")
        print("2.Update")
        print("3.Delete")
        print("4.Select")
        print("5.Exit")

        while True:
            choice = int(input("Enter Your Choice "))
            if choice == 1:
                name = input("Enter the Name :")
                age = int(input("Enter the Age :"))
                dep = input("Enter the Department :")
                self.insert(name, age, dep)
            elif choice == 2:
                id2 = int(input("Enter Your ID :"))
                n = input("Enter your Name :")
                a = int(input("Enter your Age :"))
                d = input("Enter Your Department :")
                self.update(n, a, d, id2)
            elif choice == 3:
                id1 = int(input("Enter the ID :"))
                self.delete(id1)
            elif choice == 4:
                self.select()
            elif choice == 5:
                quit()
            else:
                print("Plz Enter Correct Choices")


db = DataBaseConnectivity()
db.info()
