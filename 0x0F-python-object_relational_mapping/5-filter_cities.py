#!/usr/bin/python3
'''Module for script that takes in the name of a state as an argument and lists
 all cities of that state'''

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
        ""
        "SELECT cities.name FROM cities LEFT JOIN states ON cities.state_id\
            = states.id WHERE states.name = %s ORDER BY states.id ASC",
        (sys.argv[4],
         ))
    rows = cur.fetchall()
    newRows = []
    print(', '.join('{}'.format(row[0]) for row in rows))

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
