class Account():
    def __init__(self,balance,account):
        self.balance=balance
        self.account=account
    def credit(self,amount):
        self.balance=+amount
        print(amount ,"will be credited")
        print("total balance=",self.balance_print())
    def debit(self,amount):
        self.balance=-amount
        print(amount, 'will be debited')
        print("total balance=",self.balance_print())
    def balance_print(self):
        return self.balance
s1=Account(30000,"Saving")
s1.credit(500)
s1.debit(500)