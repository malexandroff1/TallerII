#!/usr/bin/python

import sqlite3

try:
    conn = sqlite3.connect('users.db')
    print "Open database successfully"

    conn.execute("INSERT INTO USERS (ID,USERNAME,PASSWORD) \
      VALUES (1, 'admin', 'admin' )");

    conn.commit()

    print "Records created successfully";

    conn.close()

except Exception as e:
    print('Error Exception: ', e) 