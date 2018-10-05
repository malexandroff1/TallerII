#!/usr/bin/python

import sqlite3
import SQLiteCRUD

try:
    conn = sqlite3.connect('panel-control.db')
    print "Open database successfully"

    conn.execute('''CREATE TABLE USERS
        (
            ID          INT         PRIMARY KEY     NOT NULL,
            USERNAME    CHAR(50)    NOT NULL,
            PASSWORD    CHAR(150)        NOT NULL
        );''')

    print "Table USERS created successfully"


    conn.execute('''CREATE TABLE PINS
        (
            ID          INT         PRIMARY KEY     NOT NULL,
            PIN         INT         NOT NULL,
            STATE       CHAR(10)    NOT NULL
        );''')

    print "Table PINS created successfully"

    conn.close()

except Exception as e:
    print('Error Exception: ', e) 