import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="lib"
)

mycursor = mydb.cursor()


with open("LibBooks.txt") as f:
    lines = f.readlines()[1:]
    
    for i in lines:
        line = i.split(",")
        temp = []
        counter = 0
        while counter < len(line):
            if not line[counter]:
                temp.append("-")
                counter += 1
            else:
                if line[counter][0] != '"':
                    temp.append(line[counter].strip())
                    counter += 1
                else:
                    temp2 = line[counter]
                    counter += 1
                    while line[counter][-1] != '"':
                        temp2 += f", {line[counter]}"
                        counter += 1
                    temp2 += f", {line[counter]}"
                    counter += 1
                    temp.append(temp2)
        
        sql = "INSERT INTO `Book Details` (ISBN, Title, Author_1, Author_2, Author_3, Publisher, `Publication Year`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        temp_details = list()
        temp_details.append(temp[5])
        temp_details += temp[1:5]
        temp_details += temp[-2:]
        val = tuple(temp_details)
        mycursor.execute(sql, val)

        sql1 = "INSERT INTO `Books` (`Accession Number`, ISBN) VALUES (%s, %s)"
        temp_books = list()
        temp_books.append(temp[0])
        temp_books.append(temp[5])
        val1 = tuple(temp_books)
        mycursor.execute(sql1, val1)
mydb.commit()
print("DONE")

        