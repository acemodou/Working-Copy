import pyodbc

class Database:
    __connection = None    # holds connection string pointing to DB

    @classmethod
    def initialise(cls, server, database, user, password):
        """
        Brief:
            _setConnectionString_SQLServer(server, database, user, password) - <*ADD BRIEF COMMENT
            HERE*>

        Description: -

        Argument(s):
            server - (Required) Server address string.
            database - (Required) Database name string.
            user - (Required) Database User name string.
            password - (Required) The above Database User's password string.

        Return Value(s):
            None

        Example:
            <*ADD EXAMPLE HERE*>

        Related: -

        Author(s):
            Modou Jaw
        """
        connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+ database +';UID='+ user +';PWD='+ password + ";"
        cls.__connection = pyodbc.connect(connectionString)

    @classmethod
    def get_connection(cls):
        return cls.__connection
    
    @classmethod
    def close_all_connection(cls):
        Database.__connection.close()
    
class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None 
        self.cursor = None 
    
    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.close_all_connection()
