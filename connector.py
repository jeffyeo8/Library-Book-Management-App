import mysql.connector
import sys
from datetime import datetime

class Connection:
    def __init__(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="bucks1212!",
            database="library"
        )
        self.mydb = mydb

    def checkNumBooks(self, isbn):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM Books WHERE `ISBN` = '%s'" % isbn
        mycursor.execute(sql,)
        result = len(mycursor.fetchall())
        self.mydb.commit()
        self.mydb.close()
        return result

    def searchBook(self, acc):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM Books WHERE `Accession Number` = '%s'" % acc
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result
    
    def getBookDetails(self, isbn):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM `Book Details` WHERE ISBN = '%s'" % isbn
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result
    
    def searchMember(self, id):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM Members WHERE `Membership ID` = '%s'" % id
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def checkFine(self, id):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM `Outstanding Fine` WHERE `Membership ID` = '%s'" % id
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def checkReservation(self, id):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM `Book Reservation` WHERE `Membership ID` = '%s'" % id
        mycursor.execute(sql,)
        result = mycursor.fetchall()
        self.mydb.commit()
        self.mydb.close()
        return result

    def checkLoans(self, id):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM `Book Loan` WHERE `Membership ID` = '%s' AND `Return Date` IS NULL" % id
        mycursor.execute(sql,)
        result = mycursor.fetchall()
        self.mydb.commit()
        self.mydb.close()
        return result
    
    def checkLoansBook(self, acc):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM `Book Loan` WHERE `Accession Number` = '%s' AND `Return Date` IS NULL" % acc
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def checkReservationsBook(self, acc):
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM `Book Reservation` WHERE `Accession Number` = '%s'" % acc
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def newMember(self, id, name, fac, phone, email):
        mycursor = self.mydb.cursor()
        val = (id, name, fac, phone, email)
        sql = "INSERT INTO Members (`Membership ID`, Name, Faculty, Phone, Email) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql, val)
        self.mydb.commit()
        self.mydb.close()

    def deleteMember(self, id):
        mycursor = self.mydb.cursor()
        sql = 'DELETE FROM Members WHERE `Membership ID` = "%s"' % id
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()

    def updateMember(self, id, name, fac, phone, email):
        mycursor = self.mydb.cursor()
        sql = f"UPDATE Members SET Name = '{name}', Faculty = '{fac}', Phone = '{phone}', Email = '{email}' WHERE `Membership ID` = '{id}'"
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()

    def updateBorrow(self, id, n):
        mycursor = self.mydb.cursor()
        if n:
            sql = f"UPDATE Members SET Borrowable = Borrowable - 1 WHERE `Membership ID` = '{id}'"
        else:
            sql = f"UPDATE Members SET Borrowable = Borrowable + 1 WHERE `Membership ID` = '{id}'"
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()

    def updateReservation(self, id, n):
        mycursor = self.mydb.cursor()
        if n:
            sql = f"UPDATE Members SET Reservable = Reservable - 1 WHERE `Membership ID` = '{id}'"
        else:
            sql = f"UPDATE Members SET Reservable = Reservable + 1 WHERE `Membership ID` = '{id}'"
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()
    
    def getBorrowable(self, id):
        mycursor = self.mydb.cursor()
        sql = f"SELECT `Borrowable` FROM Members WHERE `Membership ID` = '{id}'"
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result
    
    def getReservable(self, id):
        mycursor = self.mydb.cursor()
        sql = f"SELECT `Reservable` FROM Members WHERE `Membership ID` = '{id}'"
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def acqDuplicate(self, acc, isbn):
        mycursor = self.mydb.cursor()
        sql = f"INSERT INTO Books (`Accession Number`, ISBN) VALUES ('{acc}', '{isbn}')"
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()



    def acqBook(self, acc, title, a1, a2, a3, isbn, p, pyear):
        if not a2:
            a2 = "-"
        if not a3:
            a3 = "-"
        
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO `Book Details` (ISBN, Title, Author_1, Author_2, Author_3, Publisher, `Publication Year`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (isbn, title, a1, a2, a3, p, pyear)
        mycursor.execute(sql, val)
        sql = f"INSERT INTO Books (`Accession Number`, ISBN) VALUES ('{acc}', '{isbn}')"
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()

    def withdrawBook(self, acc, isbn, n):
        mycursor = self.mydb.cursor()
        if n > 1:
            sql = 'DELETE FROM Books WHERE `Accession Number` = "%s"' % acc
        else :
            sql = "DELETE FROM `Book Details` WHERE `ISBN` = '%s'" % isbn
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()

    def checkLoanCount(self, id, date):
        mycursor = self.mydb.cursor()
        sql = f'SELECT * FROM `Book Loan` WHERE `Membership ID` = "{id}" AND `Return Date` IS NULL'
        mycursor.execute(sql,)
        result = mycursor.fetchall()
        self.mydb.commit()
        self.mydb.close()

        if len(result) >= 2:
            return False
        return True

    def actuallyBorrow(self, acc, date, memid, duedate):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO `Book Loan` (`Membership ID`, `Borrow Date`, `Due Date`, `Accession Number`) VALUES (%s, %s, %s, %s)"
        val = (memid, date, duedate, acc)
        mycursor.execute(sql, val)
        self.mydb.commit()
        self.mydb.close()

    def checkReservationBorrow(self, acc, memid):
        mycursor = self.mydb.cursor()
        sql = f'SELECT * FROM `Book Reservation` WHERE `Accession Number` = "{acc}" AND `Membership ID` = "{memid}"'  
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        if result:
            self.mydb.commit()
            self.mydb.close()
            return True
        else:
            self.mydb.commit()
            self.mydb.close()
            return False

    def getLoanDetails(self, acc):
        mycursor = self.mydb.cursor()
        sql = f"SELECT * FROM `Book Loan` WHERE `Accession Number` = '{acc}' AND `Return Date` IS NULL"
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def actuallyReturn(self, memid, loan_id, fine, return_date):
        mycursor = self.mydb.cursor()
        if fine > 0:
            sql = f"UPDATE `Book Loan` SET `Return Date` = '{return_date}' WHERE `Loan ID` = {loan_id}"
            mycursor.execute(sql,)
            sql = f"INSERT INTO `Outstanding Fine` (`Membership ID`, `Fine Amount`) VALUES ('{memid}', {fine})"
            mycursor.execute(sql,)
        else :
            sql = f"UPDATE `Book Loan` SET `Return Date` = '{return_date}' WHERE `Loan ID` = {loan_id}"
            mycursor.execute(sql,)
        
        self.mydb.commit()
        self.mydb.close()

    def checkNumReservations(self, memid):
        res = self.checkReservation(memid)
        if res and len(res) >= 2:
            return False
        return True

    def makeReservation(self, acc, memid, date):
        mycursor = self.mydb.cursor()
        sql = f"INSERT INTO `Book Reservation` (`Accession Number`, `Membership ID`, `Reserve Date`) VALUES ('{acc}', '{memid}', '{date}')"
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()
    
    def checkReservationsExist(self, acc, memid):
        mycursor = self.mydb.cursor()
        sql = f"SELECT * FROM `Book Reservation` WHERE `Accession Number` = '{acc}' AND `Membership ID` = '{memid}'"
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def deleteReservation(self, acc, memid):
        mycursor = self.mydb.cursor()
        sql = f"DELETE FROM `Book Reservation` WHERE `Accession Number` = '{acc}' AND `Membership ID` = '{memid}'"
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()

    def deleteFine(self, memid):
        mycursor = self.mydb.cursor()
        sql = f"DELETE FROM `Outstanding Fine` WHERE `Membership ID` = '{memid}'"
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()
    
    def searchAuthors(self, a):
        a = a[0]
        mycursor = self.mydb.cursor()
        case1 = f"[^a-zA-Z\d]{a}[^a-zA-Z\d]"
        case2 = f"^{a}[^a-zA-Z\d]"
        case3 = f"[^a-zA-Z\d]{a}$"

        sql = f"SELECT * FROM `Book Details` WHERE CONCAT(`Author_1`, ' ', `Author_2`, ' ', `Author_3`) REGEXP '{case1}' OR CONCAT(`Author_1`, ' ', `Author_2`, ' ', `Author_3`) REGEXP '{case2}' OR CONCAT(`Author_1`, ' ', `Author_2`, ' ', `Author_3`) REGEXP '{case3}'";
        mycursor.execute(sql,)
        result = mycursor.fetchall()
        self.mydb.commit()
        self.mydb.close()
        return result

    def searchPublisher(self, p):
        mycursor = self.mydb.cursor()
        case1 = f"[^a-zA-Z\d']{p}[^a-zA-Z\d]"
        case2 = f"^{p}[^a-zA-Z\d']"
        case3 = f"[^a-zA-Z\d']{p}$"

        sql = f'SELECT * FROM `Book Details` WHERE Publisher REGEXP "{case1}" OR Publisher REGEXP "{case2}" OR Publisher REGEXP "{case3}"';
        mycursor.execute(sql,)
        result = mycursor.fetchall()
        self.mydb.commit()
        self.mydb.close()
        return result

    def searchTitle(self, t):
        mycursor = self.mydb.cursor()
        case1 = f"[^a-zA-Z\d]{t}[^a-zA-Z\d]"
        case2 = f"^{t}[^a-zA-Z\d]"
        case3 = f"[^a-zA-Z\d]{t}$"

        sql = f"SELECT * FROM `Book Details` WHERE Title REGEXP '{case1}' OR Title REGEXP '{case2}' OR Title REGEXP '{case3}'";
        mycursor.execute(sql,)
        result = mycursor.fetchall()
        self.mydb.commit()
        self.mydb.close()
        return result
        
    def search(self, i, x):
        mycursor = self.mydb.cursor()
        if i == 0:
            result = self.searchTitle(x)
        elif i == 1:
            result = self.searchAuthors(x)
        elif i == 3:
            result = self.searchPublisher(x)
        else:
            if i == 2:
                action = "ISBN"
            elif i == 4:
                action = "Publication Year"

            sql = f"SELECT * FROM `Book Details` WHERE `{action}` = {x}"
            mycursor.execute(sql,)
            result = mycursor.fetchall()
            self.mydb.commit()
            self.mydb.close()
        
        return result

    def getLoans(self):
        mycursor = self.mydb.cursor()
        sql = "SELECT `Accession Number`, `Title`, `Author_1`, `Author_2`, `Author_3`, `ISBN`, `Publisher`, `Publication Year` FROM `Book Loan` NATURAL JOIN `Books` NATURAL JOIN `Book Details` WHERE `Return Date` IS NULL"
        mycursor.execute(sql,)
        result = mycursor.fetchall()
        self.mydb.commit()
        self.mydb.close()
        return result

    def getReservations(self):
        mycursor = self.mydb.cursor()
        sql = "SELECT `Accession Number`, `Title`, `Author_1`, `Author_2`, `Author_3`, `ISBN`, `Publisher`, `Publication Year` FROM `Book Reservation` NATURAL JOIN `Books` NATURAL JOIN `Book Details`"
        mycursor.execute(sql,)
        result = mycursor.fetchall()
        self.mydb.commit()
        self.mydb.close()
        return result

    def getOutstandingFines(self):
        mycursor = self.mydb.cursor()
        sql = "SELECT `Membership ID`, `Name`, `Faculty`, `Phone`, `Email` FROM `Outstanding Fine` NATURAL JOIN `Members`"
        mycursor.execute(sql,)
        result = mycursor.fetchall()
        self.mydb.commit()
        self.mydb.close()
        return result

    def memberLoans(self, memid):
        mycursor = self.mydb.cursor()
        sql = f"SELECT `Accession Number`, `Title`, `Author_1`, `Author_2`, `Author_3`, `ISBN`, `Publisher`, `Publication Year` FROM `Book Loan` NATURAL JOIN `Books` NATURAL JOIN `Book Details` WHERE `Return Date` IS NULL AND `Membership ID` = '{memid}'"
        mycursor.execute(sql,)
        result = mycursor.fetchall()
        self.mydb.commit()
        self.mydb.close()
        return result

    def checkOverdue(self, date, memid):
        fine = 0
        mycursor = self.mydb.cursor()
        sql = f"SELECT * FROM `Book Loan` WHERE `Return Date` IS NULL AND `Due Date` < '{date}'"
        mycursor.execute(sql,)
        result = mycursor.fetchall()

        for i in result:
            x = float((date - i[3]).days)
            fine += x

        sql = f"SELECT * FROM `Outstanding Fine` WHERE `Membership ID` = '{memid}'"
        mycursor.execute(sql,)
        result = mycursor.fetchone()

        if result:
            fine += result[2]
        self.mydb.commit()
        self.mydb.close()
        return fine

    def getLoanDate(self, acc):
        mycursor = self.mydb.cursor()
        sql = f"SELECT `Due Date` FROM `Book Loan` WHERE `Accession Number` = '{acc}' AND `Return Date` IS NULL"
        mycursor.execute(sql,)
        result = mycursor.fetchone()
        self.mydb.commit()
        self.mydb.close()
        return result

    def payFine(self, id, amt, date):
        mycursor = self.mydb.cursor()
        sql = f"INSERT INTO `Fine Payment`(`Membership ID`, `Payment Amount`, `Payment Date`) VALUES ('{id}', {amt}, '{date}')"
        mycursor.execute(sql,)
        self.mydb.commit()
        self.mydb.close()