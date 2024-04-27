#!/usr/bin/python3
"""Object-relational mapping - task 0. Get all states"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv   [2], db=argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)