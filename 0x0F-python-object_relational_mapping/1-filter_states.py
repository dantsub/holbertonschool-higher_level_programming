#!/usr/bin/python3
# lists all states with a name starting with N (upper N) from
# the database hbtn_0e_0_usa
import MySQLdb as mdb
from sys import argv

if __name__ == "__main__":
    user, pwd, data = argv[1], argv[2], argv[3]  # arguments
    db = mdb.connect(user=user, passwd=pwd, db=data)  # connection
    cursor = db.cursor()  # Cursor class
    # execute query
    sql = "SELECT * FROM `states` WHERE `name` \
         LIKE BINARY 'N%' ORDER BY `id` ASC"
    cursor.execute(sql)
    [print(record) for record in cursor.fetchall()]  # print records
    cursor.close()  # close cursor
    db.close()  # close connection
