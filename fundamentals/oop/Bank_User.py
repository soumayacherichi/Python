class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


savings = BankAccount(.05,1000)
checking = BankAccount(.02,5000)

savings.deposit(10).deposit(20).deposit(40).withdraw(600).yeild_interest().display_account_info()
checking.deposit(100).deposit(200).deposit(400).withdraw(60).yeild_interest().display_account_info()

BankAccount.print_all_accounts()