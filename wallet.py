class Wallet:
    def __init__(self, initial_amount):
        self.initial_amount = initial_amount

    def spend_cash(self, amount):
        if self.initial_amount < amount:
            return "issuffiecient balance"
        else:
            self.initial_amount  = self.initial_amount- amount
            return f"Hello you have withdrawen {amount} and you balance is {self.initial_amount}"
        
    def addCash(self, add_amount):
        self.add_amount = add_amount
        self.initial_amount = self.initial_amount + add_amount
        return f"Yo added {add_amount} on your account thus your balance is {self.initial_amount}"
        

    def __repr__(self):
        return f"Your balance is: {self.initial_amount}"
    

if __name__=='__main__':
    wallet1 = Wallet(100)
    print(wallet1)
    print(wallet1.spend_cash(20))
    print(wallet1.spend_cash(120))
    print(wallet1.spend_cash(80))
    print(wallet1.addCash(200))
    print(wallet1.spend_cash(50))


    
        