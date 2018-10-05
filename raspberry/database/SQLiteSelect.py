#!/usr/bin/python

import sqlite3

try:
	conn = sqlite3.connect('panel-control.db')
	print "Opened database successfully";
	pins = conn.execute("SELECT id, pin, state from PINS")
	for row in pins:
		print "ID = ", row[0]
		print "PIN = ", row[1]
		print "STATE = ", row[2], "\n"

	print "Operation done successfully";
	conn.close()
except Exception as e:
	print('Error Exception: ', e) 



