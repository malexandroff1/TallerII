#!/usr/bin/python

import sqlite3

try:
    conn = sqlite3.connect('panel-control.db')
    print "Open database successfully"

    conn.execute("INSERT INTO PINS (ID,PIN,STATE) \
      VALUES (1, 2, 'OFF' )");

    conn.commit()

    print "Records created successfully";

    conn.close()

except Exception as e:
    print('Error Exception: ', e) 