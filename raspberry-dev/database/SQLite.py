#!/usr/bin/python

import sqlite3

try:
    conn = sqlite3.connect('test.db')
    print "Open database successfully"

    conn.execute('''CREATE TABLE COMPANY
        (
            ID          INT         PRIMARY KEY     NOT NULL,
            USERNAME    CHAR(50)    NOT NULL,
            PASSWORD    TEXT        NOT NULL
        );''')

    print "Table created successfully"

    conn.close()

except Exception as e:
    print('Error Exception: ', e) 