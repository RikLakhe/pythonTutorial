class Account():

    def __init__(self,path):
        self.path = path
        with open(self.path,'r') as file:
            try:
                self.balance = int(file.read())
            except:
                self.balance = 0


    def withdraw(self,ammount):
        self.balance = self.balance - ammount


    def save(self,ammount):
        self.balance = self.balance + ammount


    def commit(self):
        with open(self.path,'w') as file:
            file.write(str(self.balance))


account = Account("balance.txt")
account.save(1000)

account.withdraw(300)
account.save(20)

account.commit()