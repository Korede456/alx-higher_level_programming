#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4].split('\'')[0]

    db = MySQL.connect(host='localhost', user=username, passwd=password,
                       db=database_name, port=3306)
    cursor = db.cursor()
    qry = """SELECT cities.name FROM cities\
             INNER JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s
             OREDER BY cities.id ASC
          """

    cursor.execute(qry, (state_name,))
    data = [row[0] for row in cursor.fetchall()]
    print(*data, sep=', ')
    cursor.close()
    db.close()
