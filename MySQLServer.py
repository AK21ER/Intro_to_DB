import mysql.connector
from mysql.connector import Error


try:
    connection= mysql.connector.connect(
        host='localhost',
        user='root',
        password='itsme7991'
      )
    
    if connection.is_connected():
        cursor=connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print (f"Error connecting to mysql: {e}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
