from binascii import Error
from typing import List
import mysql.connector

from GiaoDich import GiaoDich
from HuTien import CoinBank

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

    def add_jar(self, jar: CoinBank):
        cursor = self.conn.cursor()
        sql = "INSERT INTO jars(name_jars, goal_jars, current_jars) VALUES (%s, %s, %s)"

        val = (jar.name,
               jar.goal,
               jar.current_balance)
        cursor.execute(sql, val)
        self.conn.commit()
        print("Saved new jar in MYSQL:", f"jar: {jar.name}, current_balance: {jar.current_balance}", end="\n")

    def add_transaction(self, transaction: GiaoDich):
        cursor = self.conn.cursor()
        sql = "INSERT INTO transaction(amount_money, category, catalog, date_transaction, note) VALUES (%s, %s, %s, %s, %s)"

        val = (transaction.amount_money,
                transaction.category,
                transaction.catalog,
                transaction.date_transaction,
                transaction.note) 
        cursor.execute(sql, val)
        self.conn.commit()
        print(f"Saved transaction in MYSQL: category->{transaction.category} amount->{transaction.amount_money}")

    def get_all_jars(self) -> List[CoinBank]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name_jars, goal_jars, current_jars FROM jars")
        rows = cursor.fetchall()

        list_jars = []
        for r in rows:
            jar = CoinBank()
            jar.id = r[0]
            jar.name = r[1]
            jar.goal = r[2]
            jar.current_balance = r[3]
            list_jars.append(jar)
        
        return list_jars
    
    def get_all_transactions(self) -> List[GiaoDich]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, amount_money, category, catalog, date_transaction, note FROM transaction")
        rows = cursor.fetchall()

        list_transaction = []

        for r in rows:
            transaction = GiaoDich()
            transaction.amount_money = r[0]
            transaction.catalog = r[1]
            transaction.category = r[2]
            transaction.date_transaction = r[3]
            transaction.note = r[4]
            list_transaction.append(transaction)

        return list_transaction
    
    def update_jar_balance(self, jar: CoinBank):
        cursor = self.conn.cursor()
        sql = "UPDATE jars SET current_jars = %s WHERE id = %s"
        val = (jar.current_balance, jar.id)
        cursor.execute(sql, val)
        self.conn.commit()
        print(f"Update balance of jar: {jar.name} trong DB")
