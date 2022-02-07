import mysql.connector
from mysql.connector import errorcode

try:
    config = {
        'user': 'root',
        'password': 'NEW',
        'host': '192.168.1.26',
        'raise_on_warnings': True
        }

    cnx = mysql.connector.connect(**config)

    Cursor = cnx.cursor()
    Cursor.execute('DROP DATABASE test_connect')

    cnx.close()
except mysql.connector.Error as err:
    print(err)

