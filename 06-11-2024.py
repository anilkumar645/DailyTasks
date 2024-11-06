# Inheritence:- Inheritance is a mechanism by which a class inherits attributes and methods from another class
 


# 1.sigle inheritence: a child class inherits properties and methods from a single parent class.

class Infinix:
    company = "Infinix"
    website = "www.infinix.com"

    def details(self):
        print("address : Hyderabad")

class Infinx_50_pro(Infinix):
    def __init__(self):
        self.name = "Infinix_50_pro"
        self.year = 1990

    def product_details(self):
        print("name : ",self.name)
        print("year : ", self.year)
        print("company : ", self.company)
        print("website : ", self.website)

mobile = Infinx_50_pro()
mobile.product_details()
mobile.details()

#2.hierachical inheritence:- inheriting properties and method from single class from multiple class at a same time.

class Animal:
    kingdom = "Animalia"

class Mammal(Animal):
    species = "Mammal"
    has_hair = True

class Bird(Animal):
    species = "Bird"
    has_feathers = True

class Fish(Animal):
    species = "Fish"
    can_swim = True

mammal = Mammal()
bird = Bird()
fish = Fish()


print(f"mammal: kingdom = {mammal.kingdom}, species = {mammal.species},Has Hair = {mammal.has_hair}")
print(f"Bird: kingdom = {bird.kingdom}, species = {bird.species},Has Feathers ={bird.has_feathers}")
print(f"Fish: kingdom = {fish.kingdom}, species = {fish.species},Can Swim = {fish.can_swim}")

#3.multiple inheritence:- a class to inherit attributes and methods from more than one parent class.


class Worker:
    def do_work(self):
        print("Doing work")
 
class Manager:
    def manage(self):
        print("Managing the team")
 
class Employee(Worker, Manager):
    def perform(self):
        print("Performing employee duties")
 
employee = Employee()
employee.do_work()  
employee.manage()  
employee.perform()
 


#4.hybrid inheritence:- using more then one type of inheritence.


class Device:
    def power_on(self):
        print("Device powered on")
 
class Phone(Device):
    def make_call(self):
        print("Making a call")
 
class SmartPhone(Phone):
    def browse_internet(self):
        print("Browsing the internet")
 
class Laptop(Device):
    def run_program(self):
        print("Running program")
 
class SmartLaptop(Laptop):
    def video_call(self):
        print("Making a video call")
 
s = SmartPhone()
s.power_on()
s.make_call()  
s.browse_internet()  
 
s = SmartLaptop()
s.power_on()  
s.run_program()
s.video_call()  