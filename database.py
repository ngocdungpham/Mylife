import mysql.connector

class DatabaseManager:
    "class quản lý kết nối và truy vấn"

    def __int__ (self, host, user, password, database):
        self.conn=mysql.connector.connect{
            host=host,
            user=user,
            password=password,
            database=database
        }
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            create table if not exists transaction(
                id INT AUTO_INCREMENT PRIMARY KEY,
                amount_money FLOAT,
                category VARCHAR(10),
                catalog VARCHAR(100),
                date_transaction DATE,
                note VARCHAR(255)     
            )
        """
        )

        cursor.execute("""
            CREATE table if not exists jars(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       name_jars VARCHAR(100),
                       goal_jars FLOAT,
                       current_jars FLOAT
            )
            """
        )
        self.conn.commit()