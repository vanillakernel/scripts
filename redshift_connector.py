#!/bin/python
#TODO: break out name, port, ETC in to config file with password.
import psycopg2
import json


with open('../wolfgang_config.txt') as config_file:
    config = json.loads(config_file.read()) 

connect_string = (
  "dbname='{0}' port='{1}' user='{2}' host='{3}' password='{4}' options='{5}'"
  ).format(config['dbname'], config['port'], config['user'], 
	config['host'], config['password'], config['options'])
try:
    conn = psycopg2.connect(connect_string)
except:
    print "I am unable to connect to the database"
cur = conn.cursor()
conn.set_isolation_level( psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT )
try:
    #cursor.execute( 'begin' )
    cur.execute("select * from reports limit 10;")
    #cursor.execute( 'commit' )
except:
    print "Unable to select from test database!"
rows = cur.fetchall()
for row in rows:
    print row
