

# classmethod:- its used to modify the class state that applies across all instance
# static variable :- When we declare a variable inside a class but outside method is called static variable.
# decorators :- The function that modify oe enhance another function without changing its actual code decorators are often used to add functionallity such as logging,access control,instrumentation in a clean and readable way.

class Mobile:
    def __init__(self, model):
        self.model = model

    def update_model(self, model):
        self.model = model


obj_1 = Mobile("iPhone 12")
print(obj_1.model)
obj_1.update_model("iPhone 12 Pro")
print(obj_1.model)



# Write a program to  get student details?

class institution :
    college_name= "Lord college of engineering and technology"
    def __init__(self,):
        self.name = input("Enter the student name here : ")
        self.id = int(input("Enter the student roll no here : "))
        self.group = input("Enter the branch here : ")
        self.address =str(input("Enter a address here : "))

    def details(self):
        print("Student Name : ", self.name)
        print("Student id : ", self.id)
        print("Student Branch : ", self.group)
        print("Student Address : ", self.address)

s1=institution()
print(s1)
s1.details()



# Write withdral and deposit money in bank

class account:
    def __init__(self):
        self.balance = 0
        print("Account Created.")
    def deposit(self):
        amount = float(input("Enter amount to Deposit : "))
        self.balance += amount
        print("New Balance : ", self.balance)
    def withdraw(self):
        amount = float(input("Enter amount to Withdraw : "))
        if amount > self.balance:
            print("insufficent balance")
        else:
            self.balance -= amount
            print("New Balance : ", self.balance)
    def Total_Balance(self):
        print("Total Balance : ", self.balance)

account = account()
account.deposit()
account.withdraw()
account.Total_Balance()



