class Account():
    print("Welcome to AV Bank")
    def __init__(self,choice):
        self.choice = choice
    def open_account(self):
        self.new_account_holder_name = str(input("Enter new account holder name: "))
        self.account_number = r.randrange(999999)
        print(f"Mr.{self.new_account_holder_name} your account has been successfully opened and account number is {self.account_number}, With balance 0. Please deposit minimum R.1000/-")
    def existing_holder(self):
        self.account_holder_name = str(input("Enter account holder name: "))
        print(f"Welcome Mr.{self.account_holder_name}. Following are the choices. Please select : \nPress 1 deposit money \nPress 2 for withdraw money")
    def deposit(self,amount_added):
        self.balance = 0
        self.amount_added = amount_added
        self.balance = self.balance + self.amount_added
        print(f"Added Rs. {self.amount_added} in account number {self.account_number}")
    def withdraw(self,subtract):
        self.balance = 0
        self.subtract = subtract
        if (self.balance<self.subtract):
            print("In sufficient balance in account")
        else:
            self.balance = self.balance - self.subtract
            print("Withrawal accepted")
            return self.balance
    def __str__(self):
        return (f"Account Owner: {self.owner} \nAccount Balance: {self.balance}")

customer_visit = int(input("Press 1: To Open New Bank Account or Press 2: To Use Existing Account : "))
acct1 = Account(customer_visit)
if customer_visit ==1:
    acct1.open_account()
    amount_added = int(input("Enter the deposit amount: "))
    acct1.deposit(amount_added)
if customer_visit ==2:
    acct1.existing_holder()
    holder_option = int(input())
    if holder_option ==1:
        amount_added = int(input("Enter the deposit amount: "))
        acct1.deposit(amount_added)
    if holder_option ==2:
        withdraw_money = int(input("Enter amount you want to withdraw: "))
        acct1.withdraw(withdraw_money)
