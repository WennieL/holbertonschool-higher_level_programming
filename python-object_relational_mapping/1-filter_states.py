#!/usr/bin/python3
"""
 lists all states with a name starting with N (upper N)
 from the database hbtn_0e_0_usa
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
        WHERE name LIKE BINARY'N%'
        ORDER BY id ASC
    """
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(f"({row[0]}, '{row[1]}')")
