#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
use cursor
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    cnx = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])
    cursor = cnx.cursor()
    cursor.execute(
        "SELECT c.id, c.name, s.name FROM cities\
         c JOIN states s ON c.state_id = s.id ORDER BY c.id")
    lines = cursor.fetchall()
    for x in lines:
        print(x)
    cursor.close()
