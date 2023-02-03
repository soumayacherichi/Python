class BankAccount:# déclaration du type une classe est un data type #nottouha juste i nabda bech te5demha w ba3d nerja"elha n7otha bech mato93odlich erreur et ki nji bech ne5demha na77Iha
#has
    all_accounts= []
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance =  balance
        #Apprend all instances to all acounts list
        BankAccount.all_accounts.append(self)
#does
    def deposit(self, amount):
        self.balance += amount 
        return self

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -=amount
        else:
            print ("Insufficient funds: Charging a 5$ fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance*self.int_rate
            return self
    
    @classmethod 
    def print_accounts(cls):
        for acc in cls.all_accounts:
            print (f"Balance:{acc.balance},Interest rate:{acc.int_rate}")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02,balance=0) #Abstraction

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return(self)
    
    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"{self.name} Balance:{self.account.balance}")
        return self


account1 = BankAccount() #houni 3andhom default values donc man7ottouhomch
# account1.deposit(200).withdraw(50).display_account_info().yield_interest().display_account_info()

account2= BankAccount(0.04,2000)
# account2.deposit(200).withdraw(50).display_account_info().yield_interest().display_account_info()

account3=BankAccount(0.05,5000)

BankAccount.print_accounts()

john = User("John", "john@gmail.com")
john.display_user_balance().make_deposit(500).make_deposit(200).make_withdraw(300).display_user_balance()




