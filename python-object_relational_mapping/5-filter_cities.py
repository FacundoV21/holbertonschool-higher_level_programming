#!/usr/bin/python3
"""
    Selects all states from a database
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    con = database.cursor()
    con.execute(
        f"""
            SELECT cities.name
            FROM cities
            JOIN states ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id ASC;
        """, (argv[4],)
    )
    data = con.fetchall()
    out = []

    for i in data:
        out.append(i[0])

    print(*out, sep=', ')
