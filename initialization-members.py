import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="lib"
)

mycursor = mydb.cursor()

with open("LibMems.txt") as f:
    lines = f.readlines()[1:]

    for i in lines:
        line = i.split(",")
        
        val = tuple()
        for i in line:
            val += (i.strip(),)
        
        sql = "INSERT INTO Members (`Membership ID`, Name, Faculty, Phone, Email) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql, val)

mydb.commit()
print("DONE")