#!/usr/bin/python3
'''
a script that lists all states with a name starting with N 
(upper N) from the database hbtn_0e_0_usa
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         password=argv[2],
                         db=argv[3],
                         port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
