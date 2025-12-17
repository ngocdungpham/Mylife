from binascii import Error
import datetime
from database import DatabaseManager
from GiaoDich import GiaoDich
from HuTien import CoinBank

class ManageAccount:
    def __init__(self):
        self.db = DatabaseManager(
            host = "localhost",
            user = "root",
            password = "LopTruong2024@",
            database = "ql_tai_chinh"
        )

        self.list_Jars = []
        self.list_transactions = []
        self.load_data()

    def load_data(self):
        if self.db.conn and self.db.conn.is_connected():
            self.list_Jars = self.db.get_all_jars()
            self.list_transactions = self.db.get_all_transactions()
            print(f"Successfully load data from to database: {len(self.list_Jars)} jar and {len(self.list_transactions)} transaction")

    def is_db_connected(self):
        return self.db is not None and self.db.conn is not None and self.db.conn.is_connected()
    
    def add_new_jar(self, name_jar: str, goal: float): # VND
        for jar in self.list_Jars:
            if jar.name == name_jar:
                print(f"Jar {name_jar} existed!")
                return
        new_jar = CoinBank()
        new_jar.name = name_jar
        new_jar.goal = goal
        new_jar.current_balance = 0
        self.list_Jars.append(new_jar)

        if self.db:
            self.db.add_jar(new_jar)
            print(f"Create new jar: {new_jar.name}")
    
    def new_transaction(self, amount: float, category: str, jar_name: str, catalog: str, note: str="" ):
        """
        Hàm trung tâm điều phối logic:
        1. Tìm hũ tiền.
        2. Cộng/Trừ tiền trong object hũ.
        3. Tạo object giao dịch.
        4. Lưu tất cả xuống DB.
        """
        select_jar = None
        for jar in self.list_Jars:
            if jar.name == jar_name:
                select_jar = jar
                break
        
        if not select_jar:
            print(f"DONT HAVE {jar_name} in list jars")
            return
        
        if category == "DEPOSIT":
            select_jar.payment(amount)
        elif category == "WITHDRAW":
            log = select_jar.withdrawal(amount)
            if isinstance(log, str):
                print(f"Error: {log}")
                return

        date = datetime.date.today().strftime("%Y-%m-%d")
        new_gd = GiaoDich()
        new_gd.amount_money = amount
        new_gd.category = category
        new_gd.catalog = catalog
        new_gd.date_transaction = date
        new_gd.note = f"{note} (Jar: {catalog})"
        
        try:
            if self.db and self.db.conn:
                self.list_transactions.append(new_gd)
                self.db.update_jar_balance(select_jar)
                self.db.add_transaction(new_gd)
                print("Add new a transaction, done!")
            else:
                print("Add fail, you need a new transaction.")

        except Error as e:
            print(f"Add fail, Error: {e}")
            new_gd = None

if __name__ == "__main__":
    app = ManageAccount()

    if app.is_db_connected():
        print("Success, you can do it")
    else:
        print("Plz check database")

    # app.new_transaction(amount=110, category="thu", catalog="Lương", note="Lương tháng 1")
    app.new_transaction(1000, category="DEPOSIT", catalog="lương", jar_name="Tiết kiệm", note="Lương công ty tháng 12 năm 2025")
    
    app.add_new_jar("Mua xe PC", 30000000)
    app.add_new_jar("Tiết kiệm", 1000000000)


    

    