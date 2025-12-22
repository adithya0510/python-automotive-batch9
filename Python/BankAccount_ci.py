class BankAccountci:

    # Constructor: initializes account details
    def __init__(self, account_number, customer_name, balance, age):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.age = age

    # Deposit money (exception: negative deposit)
    def deposit(self, amount):
        try:
            if amount <= 0:     # excp : amount cannot be negative
                raise ValueError("Deposit amount must be positive")
            self.balance += amount
            return f"After depositing {amount} the balance is {self.balance}"
        except ValueError as e:
            return e

    # Withdraw money 
    def withdraw(self, amount):
        try:
            if amount <= 0:    # excp : ammount cannot be negative
                raise ValueError("Withdraw amount must be positive")
            if amount > self.balance:    # balance should we more than amount
                raise ValueError("Insufficient balance")
            self.balance -= amount
            return f"After withdrawing {amount} the balance is {self.balance}"
        except ValueError as e:
            return e

    # Calculate compound interest 
    def calculate_ci(self, time):
        try:
            if self.age < 60:    # excp : only for senior citizens
                raise ValueError("Sorry. Only senior citizens are eligible")
            if time <= 0:
                raise ValueError("Time must be positive")

            rate = 8  
            amount = self.balance * (1 + rate / 100) ** time
            ci = amount - self.balance
            return f"Compound Interest to be paid after {time} years at {rate}% is {ci:.3f}"
        except ValueError as e:
            return e

#ojects are created
acc1 = BankAccountci("574489918", "Rahul", 10000, 65)
acc2 = BankAccountci("664727384","Rohit", 20000, 56) 

#object1
print(acc1.deposit(2000))
print(acc1.withdraw(3000))
print(acc1.calculate_ci(2))

print()   #prints an empty line
#object2
print(acc2.deposit(1000))
print(acc2.withdraw(15000))
print(acc2.calculate_ci(4))
