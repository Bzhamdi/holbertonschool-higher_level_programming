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
    cursor.execute("SELECT * FROM states ORDER BY id")
    lines = cursor.fetchall()
    for x in lines:
        if x[1][0] == "N":
            print(x)
    cursor.close()
    cnx.close()
