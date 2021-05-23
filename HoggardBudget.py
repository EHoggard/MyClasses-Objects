class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category. Current Balance: {}".format(amount, self.category, self.amount) 
    def balance(self, amount):
        return "This is the current balance: {}".format(self.amount)
    def withdrawl (self, amount):
        self.amount -= amount
        return "You have withdrawn {} in {} category".format(amount, self.category)
    def transfer(self, amount):
        if self.amount > amount:
            return "Transfer of {} successful from category {}".format(self.amount, self.category)
        else:
            print("Insufficient funds remaining") 
        
category = Budget("Mortgage", 1425)
category1 = Budget("Car", 400)
category2 = Budget("Student Loan", 500)
category3 = Budget("Food", 300)
category4 = Budget("Car Insurance", 135)
category5 = Budget("Utilities", 100)
category6 = Budget("Baby", 150)

#Deposit:
print(category.deposit(2000))
print(category1.deposit(700))
print(category2.deposit(600))
print(category3.deposit(700))
print(category4.deposit(500))
print(category5.deposit(300))
print(category6.deposit(300))

#Withdrawl:
print(category.withdrawl(1500))
print(category1.withdrawl(400))
print(category2.withdrawl(600))
print(category3.withdrawl(400))
print(category4.withdrawl(400))
print(category5.withdrawl(300))
print(category6.withdrawl(300))


#Balance:
print(category.balance(1700))
print(category1.balance(100))
print(category2.balance(600))
print(category3.balance(400))
print(category4.balance(500))
print(category5.balance(300))
print(category6.balance(300))



#Transfer:
print(category.transfer(100))
print(category1.transfer(100))
print(category2.transfer(100))
print(category3.transfer(100))
print(category4.transfer(100))
print(category5.transfer(100))
print(category6.transfer(100))









