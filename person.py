# file Person.py

class Person:
    def __int__(self, name, age, job, pay, current):
        self.name = name
        self.age = age
        self.job = job
        self.pay = pay
        self.current = current
        
    def __init__(self, name="Dũng", age=20, job="Graduate Student", pay=0, current=0):
        self.name = name
        self.age = age
        self.job = job
        self.pay = pay
        self.current = current
    
    def last_name(self):
        return self.name.split()[-1]
    
    def money_paid(self, amount_paid):
        if self.current - amount_paid < 0:
            return "Your account dont enough money to pay"
        else:
            self.current -= amount_paid
    
    def 


ZuniHaZY = Person("Pham Ngoc Dung")
Peter = Person("Pham Nam Khanh", 19, "Teach English" , 2000)
print(f"My name is {ZuniHaZY.name}, {ZuniHaZY.age} and is the {ZuniHaZY.job}. My payment is {ZuniHaZY.pay}.")
print(Peter.name, Peter.age, Peter.job, Peter.pay)