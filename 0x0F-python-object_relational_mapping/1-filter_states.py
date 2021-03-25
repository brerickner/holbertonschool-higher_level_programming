#!/usr/bin/python3
'''Module with script to list all states starting with "N"'''

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
