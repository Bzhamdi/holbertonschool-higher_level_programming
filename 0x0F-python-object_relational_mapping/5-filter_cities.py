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
    cursor.execute("SELECT c.name FROM cities c  JOIN states s ON\
                 c.state_id = s.id WHERE s.name \
                 LIKE '{}' ORDER BY c.id".format(argv[4]))
    lines = cursor.fetchall()
    print(", ".join(x[0] for x in lines))
    cursor.close()
