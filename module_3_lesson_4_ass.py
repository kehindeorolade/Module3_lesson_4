#creating a bank account class with methods and attributes
class bank_account:
    def __init__(self, deposit, account_balance, depositors_name, account_type, denomination):
        self.deposit = deposit
        self.account_balance = account_balance
        self.depositors_name = depositors_name
        self.account_type = account_type
        self.denomination = denomination
        

    def to_deposit(self, account_balance, amount_to_deposit):
       total_balance = account_balance + amount_to_deposit
        
       return total_balance 

bank_account_1 = bank_account(deposit = 10000, account_balance = 15000, depositors_name= "Kehinde", account_type = "savings", denomination = "naira",)

print(bank_account_1.to_deposit(10000, 150000))

def to_withdraw(self, account_balance, amount_to_withdraw):
    totall_balance = account_balance - amount_to_withdraw

    return totall_balance

#print(bank_account_1.to_withdraw(160000, 20000))

