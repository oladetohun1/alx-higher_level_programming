#!/usr/bin/python3
'''
a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument. It is safe from MySQL injections!
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         password=argv[2],
                         db=argv[3],
                         port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name = %s
        ORDER BY id ASC""", (argv[4],))
    # cursor.execute("""SELECT * FROM states WHERE name LIKE '{:s}'
    #   ORDER BY id ASC""".format(argv[4]))
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)

    cursor.close()
    db.close()
