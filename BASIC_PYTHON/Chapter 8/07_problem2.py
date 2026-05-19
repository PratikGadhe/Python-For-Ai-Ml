# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account :
    def __init__(self,account_number,balance):
        self.account=account_number
        self.balance=balance
    def debit(self,amount):
        self.balance-=amount
        print(f"Rs.{amount} is debited from acoount {self.account}")
        print(f"Total Balance : {self.get_balance()}")
    def credit(self,amount):
        self.balance+=amount
        print(f"Rs.{amount} is debited from acoount {self.account}")
        print(f"Total Balance : {self.get_balance()}")
    def get_balance(self):
        return self.balance

acct=int(input("Enter Account Number : "))
balance=int(input("Enter Balance : "))
user1 = Account(acct,balance)

user1.debit(1000)
user1.credit(500)
