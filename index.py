#  Create a BankAccount class with balance and account number.
# Add methods to:
# Deposit money
# Withdraw money
# Check balance
# Use private variable for balance (__balance)
class BankAccount:
    def __init__(self,account_no,balance=0):
        self._account_no=account_no #protected
        self.__balance=balance  # private

    def deposit(self,amt):
        self.__balance+=amt
        print(f"Sucessfylly Deposited= {amt}")

    def withdraw(self,amount):
        if(self.__balance<amount):
            print("No sufficient balance")
        else:
            self.__balance-=amount
            print(f"Sucessfully withdrawn = {amount}")
    def check(self):
        print(f"Current balance={self.__balance}")
        print(f"Account no = {self._account_no}")
    def get_balance(self):
        return(self.__balance)   
    

acc1=BankAccount(23502287,10000)
acc1.check()
ans=input("Do You want to Deposit or withdraw money[D/W]?")
if(ans=="d"):
    d=int(input("Enter the amount to deposit"))
    acc1.deposit(d)
elif(ans=="w"):
    w=int(input("enter the amount to withdraw"))
    acc1.withdraw(w)


print(f"Your Balance= {acc1.get_balance()}")


with open("Account","w")as f:
    f.write(f"{str(acc1._account_no)}: ")
    f.write(str(acc1.get_balance()))

