
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'ars19762002'
)

cursorObject = dataBase.cursor()

cursorObject.execute('Create Database elderco')

print('All Done')