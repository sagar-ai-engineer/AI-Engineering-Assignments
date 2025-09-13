class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    
    def display_balance(self):
        print("Account balance:", self.balance)
    
    def deposit(self, amount):
        amount+=self.balance
        print(f"Amount Rs.{amount} deposited successfully")
        self.display_balance()

    def withdraw(self, amount):
        if(amount<self.balance):
            self.balance-=amount
            print(f"Amount Rs.{amount} withdrawl successful")
            self.display_balance()
        else:
            print("Insufficient balance")


acc1 = BankAccount("Sagar", 10000000, "Savings")
acc1.display_balance
acc1.withdraw(50000)
acc1.deposit(100000)
