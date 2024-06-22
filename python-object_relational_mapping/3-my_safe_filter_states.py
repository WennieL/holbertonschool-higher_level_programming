#!/usr/bin/python3
"""
 test "Arizona'; TRUNCATE TABLE states ;
 SELECT * FROM states WHERE name = '" as an input?
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
    # %s => This is crucial for preventing SQL injection because
    # it ensures that user input is treated purely as data,
    # not executable SQL code.
    query = """
        SELECT *
        FROM states
        WHERE BINARY name = %s
        ORDER BY id ASC
    """
    # In Python, when using MySQLdb or similar database libraries that
    # support parameterized queries, like %s placeholders,
    # typically provide the parameters to be substituted into the query as a tuple(immutability).
    cursor.execute(query, (sys.argv[4],))
    result = cursor.fetchall()

    for row in result:
        print("({}, '{}')".format(row[0], row[1]))

    cursor.close()
    db.close()
