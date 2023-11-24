# install mysql on computer
#pip intall mysql
#pip install mysql-connnectr


import mysql.connector


try:
    dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='passmyword123',
        auth_plugin='mysql_native_password'
    )
    cursorObject = dataBase.cursor()

    cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

    print("Database 'elderco' created successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'dataBase' in locals() and dataBase.is_connected():
        cursorObject.close()
        dataBase.close()
