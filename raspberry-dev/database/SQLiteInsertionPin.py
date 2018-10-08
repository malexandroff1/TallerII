#!/usr/bin/python

import sqlite3

try:
    conn = sqlite3.connect('panel-control.db')
    print "Open database successfully"

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (2, 'OFF', 'GPIO' )")
    
    conn.commit()
    
    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (3, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (4, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (5, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (6, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (7, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (8, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (9, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (10, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (11, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (12, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (13, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (16, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (17, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (18, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (19, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (20, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (21, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (22, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (23, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (24, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (25, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (26, 'OFF', 'GPIO' )")

    conn.commit()

    conn.execute("INSERT INTO PINS (pin,state,ty) VALUES (27, 'OFF', 'GPIO' )")
    
    conn.commit()

    print "Records created successfully"

    conn.close()

except Exception as e:
    print('Error Exception: ', e) 
