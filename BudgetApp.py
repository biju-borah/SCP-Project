class Category:
    def __init__(self,category):
        self.ledger = []
        self.category = category
    def check_funds(self,amount):
        if len(self.ledger)!=0 and self.ledger[0]["amount"]>= amount:
            return True
        else:
            return False
    def transfer(self,amount,other):
        if self.check_funds(amount):
            other.deposit(amount,"Transfer from " + self.category)
            self.withdraw(amount,"Transfer to " + other.category)
            return True
        else:
            return False
    def deposit(self,amount,desc=""):
        self.ledger.append({"amount":amount,"description":desc})
    def withdraw(self,amount,desc=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":desc})
            return True
        else:
            return False
    def get_balance(self):
        return self.ledger
       
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(500,clothing)
print(clothing.get_balance())