class Wallet:
    def __init__(self, initial_amount):
        self.initial_amount = initial_amount

    def spend_cash(self, amount):
        if self.initial_amount < amount:
            return "issuffiecient balance"
        else:
            self.initial_amount  = self.initial_amount- amount
            return f"Hello you have withdrawen {amount} and you balance is {self.initial_amount}"
        
    


    
        