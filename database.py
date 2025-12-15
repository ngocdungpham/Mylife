from binascii import Error
import mysql.connector

import GiaoDich

class DatabaseManager:
    "class quản lý kết nối và truy vấn"

    def __init__ (self, host, user, password, database):
        self.conn = None
        try:
            self.conn=mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.create_tables()

            if self.conn.is_connected():
                print("Finish connect")
                self.create_tables()
            else:
                print("connect fail, check database")

        except Error as e:
            print("Connect fail database. Error: {e}")
            self.conn = None

    def create_tables(self):
        if self.conn is None or not self.conn.is_connected():
            print("Skip create table because dont connect database")
            return
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


    def add_transaction(self, transaction: GiaoDich):
        cursor = self.conn.cursor()
        sql = "INSERT INTO transaction(amount, category, catalog, date, note) VALUES (%s, %s, %s, %s, %s)"

        val = (transaction.amount,
                transaction.category,
                transaction.catalog,
                transaction.date,
                transaction.note) 
        cursor.execute(sql, val)
        self.conn.commit()
        print(f"Saved transaction in MYSQL: {transaction.category} {transaction.amount}")