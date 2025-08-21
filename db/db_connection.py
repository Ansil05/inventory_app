import configparser
import mysql.connector
from mysql.connector import Error
class DBConnection:
    '''establish a singleton connection with db 
    this class will create only one instance '''
    __instance = None
    def __new__(cls):
        '''
        override to implement sisngleton
        Ensure only one instance of dbconnection is ever create
        '''
        if cls.__instance is None:
            cls.__instance = super(DBConnection,cls).__new__(cls)
            cls.__instance.__initialize()
        return cls. __instance
    def __initialize(self):
        try:
            config = configparser.ConfigParser()
            config.read("db_config.ini")
            self.connection = mysql.connector.connect(
                host = config.get("mysql","host"),
                user = config.get("mysql","user"),
                password = config.get("mysql","password"),
                database = config.get("mysql","database")
            )
            if self.connection.is_connected():
                print("connected to database....")
        except Error as e:
            print(f"error while connecting =mysql:{e}")
            self.connection = None
    def get_connection(self):
        return self.connection 