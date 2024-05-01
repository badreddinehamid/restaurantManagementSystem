import mysql.connector
from mysql.connector import Error

#creating a class that manage the conneciton between the database and python 

class DBconnector:
    def __init__(self,host_name,user_name,user_passwd,user_db) -> None:
        self._host_name = host_name
        self._user_name = user_name
        self._user_passwd = user_passwd
        self._user_db = user_db
        #considered none at first until connected_to_db() executed
        self._connection = None

    #this function connect to the database and return 1 if everything is correct else it returns 0
    def connect_to_db(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host = self._host_name,
                user = self._user_name,
                passwd = self._user_passwd,
                database = self._user_db
            )
            print("connected successfuly`")


        except Error as err:
            print(f"error : {err}")
            return 0
        
        self._connection = connection
        return 1



    #this function excute all the query from the user to the database it return 0 if the error in the connection and 1 if the error in the cursor
    def execute_query(self,query):
        try:
            cursor = self._connection.cursor()
        except:
            print('error not connected to the database')
            return 0

        try :
            cursor.execute(query)
            print("executed")
        except Error as err:
            print(f"error : {err}")
            return 1


    #tto close the database after the use
    def close_DB(self):
        self._connection.close()
        print("closed succesfully")



    
managerConnnector = DBconnector('localhost','restaurantManager',"password","restaurantManangementDB")

managerConnnector.connect_to_db()