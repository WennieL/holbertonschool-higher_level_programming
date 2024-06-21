#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
    )

    cursor = db.cursor()
    query = """
        SELECT * 
        FROM states
        WHERE BINARY name = '{}'
        ORDER BY id ASC""".format(sys.argv[4])

    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print("({}, '{}')".format(row[0], row[1]))
