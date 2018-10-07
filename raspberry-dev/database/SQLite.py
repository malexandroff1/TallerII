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
            TYPE        CHAR(10)        NOT NULL,
        );''')

    print "Table PINS created successfully"

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(2,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(3,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(4,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(5,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(6,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(7,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(8,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(9,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(10,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(11,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(12,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(13,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(16,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(17,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(18,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(19,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(20,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(21,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(27,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(22,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(23,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(24,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(25,"OFF","GPIO") )

    conn.execute('''INSERT INTO PINS (pin,state,type) 
               VALUES (?,?,?)''',(26,"OFF","GPIO") )

    conn.close()

except Exception as e:
    print('Error Exception: ', e) 
