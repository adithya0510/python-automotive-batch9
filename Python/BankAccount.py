class BankAccount:

#initialisation
    def __init__(self,account_number,customer_name,initial_balance = 0.0):
        self.account_number = account_number  #123
        self.customer_name = customer_name    # alice
        self.balance = initial_balance      #50.0

    def deposit(self,amount):
        self.balance = self.balance + amount  #70.00
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount  #60.00
        return self.balance

account1 = BankAccount("123","Alice",50.00)
print(account1.deposit(20))
print(account1.withdraw(10))

