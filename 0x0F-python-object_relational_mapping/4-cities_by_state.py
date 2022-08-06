#!/usr/bin/python3
""" lists all cities from the database """

from sys import argv
import MySQLdb

if __name__ == '__main__':

    try:
        conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                charset="utf8"
                )
    except Exception:
        print("No conection")
        exit()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states WHERE cities.state_id=\
                states.id ORDER BY cities.id;")
    except Exception:
        print("interrupted query")
        cursor.close()
        conn.close()
        exit()

    rows_sc = cursor.fetchall()

    for row in rows_sc:
        print(row)
    cursor.close()
    conn.close()
