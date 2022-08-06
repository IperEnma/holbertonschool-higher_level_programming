#!/usr/bin/python3
"""Write a script that takes in an argument"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name\
            ='{}' ORDER BY id ASC".format(argv[4]))
    row_state = cursor.fetchall()
    for state in row_state:
        print(state)
    cursor.close()
    conn.close()
