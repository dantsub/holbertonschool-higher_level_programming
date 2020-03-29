#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa
import MySQLdb as mdb
from sys import argv

if __name__ == "__main__":
    user, pwd, data = argv[3], argv[2], argv[1]  # arguments
    db = mdb.connect(user=user, passwd=pwd, db=data)  # connection
    cursor = db.cursor()  # Cursor class
    cursor.execute("SELECT * FROM `states`")  # execute query
    [print(record) for record in cursor.fetchall()]  # print records
    db.close()  # close connection
