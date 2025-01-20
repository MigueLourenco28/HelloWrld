#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("""Content-type:text/html\n\n
<!DOCTYPE html>
<head>
    <title> New Contact </title>
</head>
<body> """)
    
form = cgi.FieldStorage()

id = str(form["id"].value)
user_name = str(form["user_name"].value)
password = str(form["password"].value)
confirm_password = str(form["confirm_password"].value)
email = str(form["email"].value)
confirm_email = str(form["confirm_email"].value)

db_connection = sqlite3.connect('users.db')
cursor = db_connection.cursor()

try:
    cursor.execute('INSERT INTO Users VALUES( ?, ?, ?, ?, 0);' , \
               	( int(id), user_name, password, email ))
except sqlite3.Error as er:
	print('Error in INSERT: ', er)
except password != confirm_password as er:
    print('Error in INSERT: ', er)
except email != confirm_email as er:
    print('Error in INSERT: ', er)
db_connection.commit()
db_connection.close()

print('<h2> A new contact was added ' + \
  	user_name +  '</h2> <p>')
print("""  <p> <a href="listContacts.py" > Return to Contact List. </a> </p>
</body>
</html>""")
