#!/usr/bin/python3
'''
script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         password=argv[2],
                         db=argv[3],
                         port=3306,
                         )
    # Create a cursor objs to execute queries and fetch results
    cursor = db.cursor()

    # Execute the SQL query with state_name as a parameter
    query = '''
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    '''
    cursor.execute(query, (argv[4],))

    # Fetch all the results
    results = cursor.fetchall()
    print(", ".join([row[0] for row in results]))
    # Close cursor and database connection
    cursor.close()
    db.close()
