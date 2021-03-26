#!/usr/bin/python3
'''Module with script that displays state names matching the argument'''

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
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
        (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
