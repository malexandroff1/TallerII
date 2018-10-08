#!/usr/bin/python

import sqlite3

try:
    conn = sqlite3.connect('panel-control.db')
    print "Open database successfully"

    conn.execute("INSERT INTO USERS (USERNAME,PASSWORD) \
      VALUES ('admin', 'admin' )")

    conn.commit()

    print "Records created successfully"

    conn.close()

except Exception as e:
    print('Error Exception: ', e) 
