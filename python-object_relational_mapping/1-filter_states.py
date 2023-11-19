#!/usr/bin/python3
"""
    Selects all states from a database
"""

from sys import argv
import MySQLdb

database = MySQLdb.connect(
    host="localhost",
    user=argv[1],
    password=argv[2],
    database=argv[3]
)

con = database.cursor()
con.execute(
    """SELECT *
        FROM states
        WHERE name LIKE 'N%'
        ORDER BY id ASC;
    """
)
data = con.fetchall()
for i in data:
    print(i)