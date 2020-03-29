#!/usr/bin/python3
# lists all cities from the database hbtn_0e_4_usa
import MySQLdb as mdb
from sys import argv

if __name__ == "__main__":
    user, pwd, data = argv[3], argv[2], argv[1]  # arguments
    db = mdb.connect(user=user, passwd=pwd, db=data)  # connection
    cursor = db.cursor()  # Cursor class
    # execute query
    sql = "SELECT cities.id, cities.name, states.name "
    sql += "FROM cities LEFT JOIN states "
    sql += "ON cities.state_id = states.id"
    cursor.execute(sql)
    [print(record) for record in cursor.fetchall()]  # print records
    cursor.close()  # close cursor
    db.close()  # close connection
