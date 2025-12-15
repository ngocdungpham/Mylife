from database import DatabaseManager


class ManageAccount:
    def __init__(self):
        self.db = DatabaseManager(
            host = "localhost",
            user = "root",
            password = "LopTruong2024@",
            database = "ql_tai_chinh"
        )

    def is_db_connected(self):
        return self.db is not None and self.db.conn is not None and self.db.conn.is_connected()

if __name__ == "__main__":
    app = ManageAccount()

    if app.is_db_connected():
        print("Success, you can do it")
    else:
        print("Plz check database")
