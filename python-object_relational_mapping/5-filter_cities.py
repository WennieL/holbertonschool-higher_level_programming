#!/usr/bin/python3
"""
 takes in the name of a state as an argument and lists
 all cities of that state, using the database hbtn_0e_4_usa
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
    state_name = sys.argv[4]

    query = """
        SELECT cities.name
        FROM cities
        JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    result = cursor.fetchall()

    if result:
        cities = [row[0] for row in result]
        print(", ".join(cities))
    else:
        print("")

    cursor.close()
    db.close()
