from database import DatabaseManager


class ManageAccount:
    def __int__(self):
        self.db = DatabaseManager(
            host = "localhost",
            user = "root",
            password = "Loptruong2024@",
            database = "ql_tai_chinh"
        )

if __name__ == "__main__":
    app = ManageAccount()
