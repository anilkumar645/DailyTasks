
#Abstraction 

# In python abstraction is a findamental concept in object-oriented programming(oops) 
# that help in maneging complexity by hiding unnecessary details from the user and exposing only essential part of the code 




# real time


from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 

class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
    

class Cow(Animal):
    def sound(self):
        return "Ambaa"
    

dog = Dog()
cat = Cat()
cow = Cow()



print("Dog:",dog.sound())

print("Cat:",cat.sound())

print("Cow:",cow.sound())



from abc import ABC 

class Payment(ABC):
    @abstractmethod 
    def process_payment(self,amount):
        pass 

class CreditCardPayment(Payment):
    def process_payment(self,amount):
        return f"Processing credit card payment {amount}"
    

class PayPayalPayment(Payment):
    def process_payment(self,amount):
        return f"Processing credit card payment {amount}"
    

class BitcoinPayment(Payment):
    def process_payment(self,amount):
        return f"Processing credit card payment {amount}"
    

c = CreditCardPayment()
p = PayPayalPayment()
b = BitcoinPayment()

print(c.process_payment(100))
print(p.process_payment(200))
print(b.process_payment(300))