#!/usr/bin/python3
# takes in the name of a state as an argument and lists all cities
# of that state, using the database hbtn_0e_4_usa
import MySQLdb as mdb
from sys import argv

if __name__ == "__main__":
    user, pwd, data, name = argv[1], argv[2], argv[3], argv[4]  # arguments
    db = mdb.connect(user=user, passwd=pwd, db=data)  # connection
    cursor = db.cursor()  # Cursor class
    # execute query
    cursor.execute("SELECT cities.name FROM cities " +
                   "JOIN states ON cities.state_id = states.id " +
                   "WHERE states.name = %s ORDER BY cities.id;", (name,))
    # print records
    print(", ".join([entry[0] for entry in cursor.fetchall()]))
    cursor.close()  # close cursor
    db.close()  # close connection
