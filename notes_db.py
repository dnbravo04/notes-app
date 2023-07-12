import mysql.connector
from mysql.connector import errorcode

config = {"user": "root", "password": "", "host": "localhost", "database": "notes"}

try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied" + str(e))
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Invalid database. Perhaps you are using a different database name")
    else:
        print(e)
else:
    cnx.close()
