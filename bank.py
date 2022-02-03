class bankAccount(object):

    def __init__(self, initial_balance = 0):
        self.balance = initial_balance

    def deposit(self,amount):
        self.balance+= amount

    def withdrawal(self,amount):
        self.balance-= amount

    def welcome(self):
        print("Press 1 for Deposit")
        print("Press 2 for Withdrawal")
        print("Press 3 for Balance")
        print("Press 4 for Exit")

    def cont(self):
        print("Press y to continue??")


print("Welcome to the Banking Programm")
print("Enter initial Bank Balance")
bal = int(input())
obj = bankAccount(bal)
print()
while True:
    obj.welcome()
    print("Enter: ")
    user = int(input())
    if user == 1:
        print("Enter Amount to be deposit: ")
        deposit = int(input())
        obj.deposit(deposit)
        print("Your New Balnce is : ", obj.balance)
        obj.cont()
        a = input()
        if a != 'y':
            print("Thankyou For using This Programm")
            break
        print()
    elif user == 2:
        print("Enter amount to be withdraw: ")
        withdraw = int(input())
        obj.withdrawal(withdraw)
        print("Your Remaining Balnce is : ", obj.balance)
        obj.cont()
        a = input()
        if a != 'y':
            print("Thankyou For using This Programm")
            break
        print()
    elif user == 3:
        print("Your Balnce is : ", obj.balance)
        obj.cont()
        a = input()
        if a != 'y':
            print("Thankyou For using This Programm")
            break
        print()
    elif user == 4:
        print("Thankyou for using this program")
        break
    else:
        print("Wrong Option Please try again")
        print()
