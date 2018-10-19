#!/usr/bin/python

import sqlite3


def connection():
	conn = sqlite3.connect('panel-control.db')
	print "Open database successfully"
	return conn

def insertUser(username, password):
	try:
		conn = connection()
		conn.execute("INSERT INTO USERS (ID,USERNAME,PASSWORD) \
			VALUES (1, " + username + ", " + password + " )")
		conn.commit()
		print "Records created successfully"
		conn.close()

	except Exception as e:
		print('Error Exception: ', e) 

def insertPin(pin,state):
	try:
		conn = connection()
		conn.execute("INSERT INTO PINS (ID,PIN,STATE) \
			VALUES (1, " + pin + ", " + state + " )")
		conn.commit()
		print "Records created successfully"
		conn.close()
	except Exception as e:
		print('Error Exception: ', e) 

def updatePin(pin,state):
	try:
		conn connection()
		conn.execute("UPDATE PINS set STATE = " + state + " where PIN = " + pin)
		conn.commit()
		print "Total number of rows updated :", conn.total_changes
	except Exception as e:
		print('Error Exception: ', e)

def updateUser(username,password):
	try:
		conn connection()
		conn.execute("UPDATE USERS set PASSWORD = " + password + " where USERNAME = " + username)
		conn.commit()
		print "Total number of rows updated :", conn.total_changes
	except Exception as e:
		print('Error Exception: ', e)

def deletePin(pin):
	try:
		conn = connection()
		conn.execute("DELETE from PINS where ID = " + pin + ";")
		print "Total number of rows deleted :", conn.total_changes
	except Exception as e:
		print('Error Exception: ', e)