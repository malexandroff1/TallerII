#!/usr/bin/python

import sqlite3

try:
    conn = sqlite3.connect('panel-control.db')
    print "Open database successfully"

    conn.execute('''CREATE TABLE USERS
        (
            ID          INTEGER         PRIMARY KEY     AUTOINCREMENT,
            USERNAME    CHAR(50)        NOT NULL        UNIQUE,
            PASSWORD    CHAR(150)        NOT NULL
        );''')

    print "Table USERS created successfully"


    conn.execute('''CREATE TABLE PINS
        (
            ID          INTEGER         PRIMARY KEY     AUTOINCREMENT,
            PIN         INT             NOT NULL        UNIQUE,   
            STATE       CHAR(10)        NOT NULL,
            TY          CHAR(10)        NOT NULL
        );''')

    print "Table PINS created successfully"

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (12, 'OFF', 'GPIO' )")
    
    conn.commit()
    
    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (11, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (6, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (1, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (0, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (3, 'OFF', 'GPIO' )")

    conn.commit()

    conn.close()

except Exception as e:
    print('Error Exception: ', e) 
