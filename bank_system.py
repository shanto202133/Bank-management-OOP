class user:
    def __init__(self, name, balnce) -> None:
        self.name = name
        self.balance = balnce
        self.transaction = []
        self.loan_amount = 0
    def deposite(self,amount):
        self.balance += amount
        self.transaction.append(f'deposited:{amount}')
    def withdraw(self, amount):
        if amount > self.balance:
            print('Bankruptcy')
        else:
            self.balance -= amount            
        self.transaction.append(f'withdrawn :{amount}')
    def transfer(self, user_n ,amount):
         if amount > self.balance:
             print('Bankrupt')
         else:
             self.balance -= amount
             user_n.balance +=amount  
             self.transaction.append(f'transfered {amount} to {user_n.name}')
    def take_loan(self, amount):
        if amount > 2*self.balance:
            print('exeeds the limit')
        else:
            self.loan_amount += amount
            self.transaction.append(f'took load amount:{amount}')
            admin.total_loan += amount

    def get_balance(self):
        return self.balance
    def transaction_history(self):
        return self.transaction

class Admin:
    def __init__(self) -> None:
        self.users = []
        self.total_balance = 0
        self.total_loan = 0
        self.loan_feature = True

    def create_account(self, name, balance):
        User = user(name, balance)
        self.users.append(User)
        self.total_balance += balance
        print(f'congrats! {name} , your account created')

    def chk_total_balance(self):
        return self.total_balance
    def chk_total_loan_amount(self):
        return self.total_loan
    def on_load(self):
        self.loan_feature = True
    def Off_loan(self): 
        self.loan_feature = False



admin = Admin()

admin.create_account('twhid', 1000)
admin.create_account('shanto', 2000)

user1 = admin.users[0]
user2 = admin.users[1]

user1.deposite(500)

user2.withdraw(1000)
user1.transfer(user2, 300)
user2.take_loan(500)            

print( user1.get_balance())
print( user2.get_balance())

print( user1.transaction_history())
print( user2.transaction_history())

print( admin.chk_total_balance())
print(admin.chk_total_loan_amount())        
                       
       
