#BankAccount
#Base Class
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposit amount: {amount},New Balance: {self.__balance}")
        else:
            print("The deposited amount must be positive")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            return self.__balance
        else:
            print("Insuffecient funds!!")
            return None
    #Getters method for protected value balance
    def get_balance(self):
        return self.__balance
class SavingsAccount(BankAccount): #child class1
    def __init__(self,account_number,balance=0,interest_rate=0.04):
        super().__init__(account_number,balance)
        self.__interest_rate= interest_rate
    def calculate_interest(self):
        return self.get_balance() *self.__interest_rate
class CurrentAccount(BankAccount): #child class2
    def __init__(self,account_number,balance=0,minimum_balance=500):
        super().__init__(account_number,balance)
        self.__minimum_balance = minimum_balance
    def withdraw(self, amount):
        #withdraw with minimum balance
        if self.get_balance() - amount>=self.__minimum_balance:
            return super().withdraw(amount)
        else:
            print("Withdrawl is denied")
            return None
saving =SavingsAccount(123456,1000,0.04)
print(f"Interest:{saving.calculate_interest()}")
saving.deposit(500)
saving.withdraw(100)
print(f"Final Balance:{saving.get_balance()}")

current = CurrentAccount(2468,1000,500)
print(current.withdraw(400))
print(f"Final Balance:{current.get_balance()}")


        