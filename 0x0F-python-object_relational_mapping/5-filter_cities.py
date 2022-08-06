#!/usr/bin/python3
""" lists all cities of that state """

import MySQLdb
from sys import argv

if __name__ == '__main__':

    try:
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                charset="utf8")
    except Exception:
        print("Error conexion with database")
        exit()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT cities.name FROM states JOIN cities \
                ON cities.state_id=states.id \
                WHERE states.name=%s ORDER BY cities.id ASC", (argv[4], ))
    except Exception:
        cursor.close()
        conn.close()
        print("query interrumped")
        exit()
    row_cities = cursor.fetchall()

    count = 0
    if (len(row_cities) == 0):
        print()
    for citie in row_cities:
        if (count + 1) == len(row_cities):
            print(citie[0])
        else:
            print(citie[0], end=", ")
        count += 1
    cursor.close()
    conn.close()
