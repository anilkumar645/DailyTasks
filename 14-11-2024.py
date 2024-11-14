"""1.Create a class Vehicle with attributes brand and year. 
The class should have a method get_info() that returns the brand and year of the vehicle. 
Then, create two subclasses:

Car, which adds an attribute number_of_doors.
Motorcycle, which adds an attribute has_sidecar.
Both subclasses should override the get_info() method to include their respective
 additional attributes in the returned string."""

class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand 
        self.year = year 
    
    def get_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self,brand,year,number_of_doors):
        super().__init__(brand,year)
        self.number_of_doors = number_of_doors 

    def get_info(self):
        print(f"Brand: {self.brand}, Year: {self.year} , Door: {self.number_of_doors}")


class Motorcycle(Vehicle):
    def __init__(self,brand,year,has_sidecar):
        super().__init__(brand,year)
        self.has_sidecar = has_sidecar 

    def get_info(self):
        sidecar = "Yes" if self.has_sidecar else "No" 
        print(f"Brand: {self.brand} , Year: {self.year}, Sidecar: {sidecar}") 


vehicle = Vehicle("Toyota", 2020)
car = Car("Honda",2021,4)
motorcycle = Motorcycle("Harley-Davidson", 2019,True)

vehicle.get_info()
car.get_info()
motorcycle.get_info()


"""2.Define an abstract class Animal with an abstract method make_sound().
 Then, create three classes that inherit from Animal:

Dog with the sound "Woof".
Cat with the sound "Meow".
Cow with the sound "Moo".
Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method."""




from abc import ABC,abstractmethod 

class Animal(ABC):
    @abstractmethod 
    def make_sound(self):
        pass 
class Dog(Animal):
    def make_sound(self):
        print("Woof")
class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Cow(Animal):
    def make_sound(self):
        print("Ambaa")

def play_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()
cow = Cow()

play_sound(dog)
play_sound(cat)
play_sound(cow)

"""3.Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). 
Then, create two subclasses:

SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden)."""

from abc import ABC,abstractmethod 

class BankAccount(ABC):
    def __init__(self,balance = 0):
        self._balance = balance 
        
        @abstractmethod 
        def deposit(self,amount):

            pass 
        @abstractmethod 
        def withdraw(self,amount):
            pass 
        
        def get_balance(self):
            print(f"Balance: $ {self._balance}")

class SavingsAccount(BankAccount):
    def deposit(self,amount):
        self._balance += amount
    
    def withdraw(self,amount):
        if self._balance - amount >= 500:
            self._balance -= amount 
        else:
            print("Insufficient balance to maintain minimum $500.")
class CurrentAccount(BankAccount):

    def deposit(self,amount):
        self._balance += amount 
    
    def withdraw(self,amount):
        if self._balance - amount >= -1000:
            self._balance -= amount 
        else:
            print("Overdraft limit reached.")

savings = SavingsAccount(600)
current = CurrentAccount(0)
savings.withdraw(200)
current.withdraw(500)







"""4.Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). Then create two subclasses:

Manager, which adds an attribute department.
Developer, which adds an attribute programming_language.
Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.

Add a method increase_salary(percent) in the Employee class that increases the salary by a given percentage."""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
 
    def get_details(self):
            print(f"Name: {self.name}, Salary: {self.salary}")
 
    def get_salary(self):
        print(f"Salary: {self.salary}")
 
    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100
        print(f"Updated Salary: {self.salary}")
 
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
 
    def get_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")
 
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
 
    def get_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Language: {self.programming_language}")

manager = Manager("Alice", 70000, "Sales")
developer = Developer("Bob", 60000, "Python")
manager.get_details()     # Output: Name: Alice, Salary: 70000, Department: Sales
developer.get_details()   # Output: Name: Bob, Salary: 60000, Language: Python
manager.increase_salary(10)   # Output: Updated Salary: 77000


"""5.Create an abstract class Media with an abstract method play(). Then create the following subclasses:

Audio, which plays a .mp3 file.
Video, which plays a .mp4 file.
LiveStream, which plays a live stream.
Implement a function start_media(media) that takes an object of type Media and calls its play() method. 
Demonstrate polymorphism by passing different types of media to this function."""

from abc import ABC, abstractmethod
 
class Media(ABC):
    @abstractmethod
    def play(self):
        pass
 
class Audio(Media):
    def play(self):
        print("Playing audio file .mp3")
 
class Video(Media):
    def play(self):
        print("Playing video file .mp4")
 
class LiveStream(Media):
    def play(self):
        print("Streaming live content")
 
def start_media(media):
    media.play()
 
# Usage
audio = Audio()
video = Video()
livestream = LiveStream()
start_media(audio)        # Output: Playing audio file .mp3
start_media(video)




"""6.Create an abstract class LibraryItem with abstract methods borrow() and return_item(). Then create two subclasses:

Book, with attributes title, author, and num_copies.
DVD, with attributes title, director, and duration.
Implement a function borrow_item(item) that borrows the library item and decreases the number of available copies (for books) 
or marks the DVD as borrowed.
"""

from abc import ABC, abstractmethod
 
class LibraryItem(ABC):
    @abstractmethod
    def borrow(self):
        pass
 
    @abstractmethod
    def return_item(self):
        pass
 
class Book(LibraryItem):
    def __init__(self, title, author, num_copies):
        self.title = title
        self.author = author
        self.num_copies = num_copies
 
    def borrow(self):
        if self.num_copies > 0:
            self.num_copies -= 1
            print(f"Borrowed {self.title}. Copies left: {self.num_copies}")
        else:
            print("No copies available")
 
    def return_item(self):
        self.num_copies += 1
        print(f"Returned {self.title}. Copies now: {self.num_copies}")
 
class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        self.borrowed = False
 
    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"Borrowed DVD: {self.title}")
        else:
            print("Already borrowed")
 
    def return_item(self):
        if self.borrowed:
            self.borrowed = False
            print(f"Returned DVD: {self.title}")
        else:
            print("This DVD was not borrowed")
 
def borrow_item(item):
    item.borrow()
 
# Usage
book = Book("Python 101", "John Doe", 3)
dvd = DVD("Inception", "Christopher Nolan", "148 min")
 
# Borrow and return actions
borrow_item(book)         # Output: Borrowed Python 101. Copies left: 2
borrow_item(dvd)          # Output: Borrowed DVD: Inception
book.return_item()        # Output: Returned Python 101. Copies now: 3
dvd.return_item()         # Output: Returned DVD: Inception