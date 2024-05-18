
import mysql.connector
import os


class DataBaseMysql:
    def __init__(self, ):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USERNAME"),
            passwd=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME"),
            autocommit=True,
            ssl_verify_identity=False,
            ssl_ca=r"C:\users\acqua\downloads\cacert-2023-08-22.pem",
            charset="utf8")
        self.__connection = mydb
        self.__cursor = self.__connection.cursor(buffered=True)
        return self.__cursor

    def disconnect(self):
        if self.__connection is not None:
            self.__connection.close()
            self.__connection = None

    def execute_query(self, query, params=None):
        try:

            cursor = self.connect()
            cursor.execute(query, params)

            if query.strip().startswith('SELECT') or query.strip().startswith('WITH'):
                result = cursor.fetchall()
                return result

            elif query.strip().startswith('INSERT INTO'):
                id_lastrow = cursor.lastrowid
                if query.strip().startswith('INSERT INTO cliente') and params[0] == '164':
                    self.update_cliente([id_lastrow])

                return id_lastrow

            else:
                return None
        except mysql.connector.Error as e:
            st.error(f"Error executing query: {e}")
            raise
        finally:
            self.disconnect()