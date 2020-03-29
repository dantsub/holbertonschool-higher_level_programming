#!/usr/bin/python3
# takes in arguments and displays all values in the states table
# of hbtn_0e_0_usa where name matches the argument. But this time,
# write one that is safe from MySQL injections!
import MySQLdb as mdb
from sys import argv

if __name__ == "__main__":
    user, pwd, data, name = argv[1], argv[2], argv[3], argv[4]  # arguments
    db = mdb.connect(user=user, passwd=pwd, db=data)  # connection
    cursor = db.cursor()  # Cursor class
    # execute query
    cursor.execute("SELECT * FROM `states` WHERE name=%s " +
                   "ORDER BY `id` ASC;", (name, ))
    [print(record) for record in cursor.fetchall()]  # print records
    cursor.close()  # close cursor
    db.close()  # close connection
