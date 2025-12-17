import library

class CoinBank:
    id: int
    name: str
    goal: str
    current_balance: float

    def payment(self, amount: float):
        self.current_balance += amount
    
    def withdrawal(self, amount: float):
        if self.current_balance < amount:
            return "Your account haven't enough to draw money"
        else:
            self.current_balance -= amount
    
