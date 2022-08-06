#!/usr/bin/python3
""" NO  SQL Injection """

from sys import argv
import MySQLdb

if (__name__ == '__main__'):

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
            =%s ORDER BY id ASC", (str(argv[4]), ))
    row_states = cursor.fetchall()

    for state in row_states:
        print(state)
    cursor.close()
    conn.close()
