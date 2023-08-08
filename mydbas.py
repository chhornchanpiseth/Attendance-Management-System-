

# Install Mysql on pc
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector (general)[optional]
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root1',
    password = 'root1'

)

cursorObj = database.cursor()
cursorObj.execute("CREATE DATABASE attendance_system"),

print("All Done")
