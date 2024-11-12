
#1. Single Inheritance
# Problem Statement: Create a base class Animal with an attribute name and a method speak(). Then, create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".
'''
Define a base class Animal with an __init__ method that takes name as a parameter.
Define a method speak() in Animal that prints "Animal sound".
Create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".
Create an instance of Dog and call the speak() method.'''

class Animal:
    def __init__(self):
        self.name = input("Enter Animal Name Here : ")
        self.breed = input("Enter Animal Breed Here :  ")
        self.color = input("Enter Animal Color Here : ")
        print("-"*30)

    def details(self):
        print("Animal Name : ",self.name)
        print("Animal Breed : ",self.breed)
        print("Animal Color : ",self.color)

class dog(Animal):

    def speak(self):
        self.bark = "bow bow"
        print(self.bark)
        
a=dog()
a.details()
a.speak()


#2. Multiple Inheritance
#1.Problem Statement: Create a class Teacher with an attribute subject. Then, create a class Researcher with an attribute field. Finally, create a class TeachingResearcher that inherits from both Teacher and Researcher, and has an additional method to display both attributes.

'''
Define a Teacher class with an __init__ method to initialize subject.
Define a Researcher class with an __init__ method to initialize field.
Define a TeachingResearcher class that inherits from both Teacher and Researcher, and has an __init__ method to initialize both subject and field. Add a method to display both.
Create an object of TeachingResearcher and display its attributes.'''

class Teacher:
    def __init__(self):
        self.name = input("Enter Teacher's Name Here : ")
        self.subject = input("Enter Name Of Teacher's Subject : ")

    def Teacher_details(self):
        print("Teacher Name : ",self.name)
        print("Teacher Subject : ",self.subject)

class Researcher:
    def __init__(self):
        self.name = input("Enter Researcher Name Here : ")
        self.topic = input("Enter Researcher Topic Name Here : ")

    def Researcher_details(self):
        print("Researcher Name : ",self.name)
        print("Research Topic Name : ",self.topic)

class TeachingResearcher(Teacher,Researcher):
    def __init__(self):
        Teacher.__init__(self)
        Researcher.__init__(self)
    def display(self):
        print("Subject : ",self.subject)
        print("Topic : ",self.topic)

details = TeachingResearcher()
details.display()



#2.Problem Statement: Create two base classes: Bird and Flyable. Bird should have an attribute species, and Flyable should have a method fly(). Then, create a derived class Eagle that inherits from both Bird and Flyable.

'''
Define a class Bird with an attribute species.
Define a class Flyable with a method fly() that prints "Flying".
Create a class Eagle that inherits from both Bird and Flyable, and has a method to display species and flying capability.
Create an instance of Eagle and call its methods.'''

class Bird:
    def __init__(self):
        self.species = input("Enter Bird Name Here : ")

class Flyable:

    def fly(self):
        self.Flyable = "Flying"

class Eagle(Bird,Flyable):
    
    def __init__(self):
        Bird.__init__(self)
        Flyable.fly(self)

    def display(self):
        print(self.species)
        print(self.Flyable)

e=Eagle()
e.display()


#3. Multilevel Inheritance
#Problem Statement: Create a class hierarchy where Person is the base class, Employee is derived from Person, 
#and Manager is derived from Employee. Each class should add an additional attribute, and a method to display all attributes from the hierarchy.

'''Tasks:
Define a base class Person with attributes name and age.
Define a derived class Employee with an additional attribute salary.
Define another derived class Manager that inherits from Employee and adds an attribute department.
Implement methods to display the information in each class.
Create an instance of Manager and display its information.'''


class Person:
    def __init__(self):
        self.name = input("Enter Person Name : ")
        self.age = input("Enter Person Age : ")
 
    def person_details(self):
        print("Person Name: ",self.name)
        print("Person Age: ",self.age)
 

class Employee(Person):
    def __init__(self):
        super().__init__() 
        self.salary = input("Enter Employee Salary : ")

    def employee_details(self):
        self.person_details()  
        print("Employee Salary: ",self.salary)
 

class Manager(Employee):
    def __init__(self):
        super().__init__() 
        self.department = input("Enter Department Name : ")
 
    def manager_details(self):
        self.employee_details() 
        print("Department Name: ",self.department)

m = Manager()
print('-'*30)
m.manager_details()
 


#4. Hierarchical Inheritance

#1.Problem Statement: Design a class hierarchy for an employee management system with the following structure:

'''Employee: Base class with name and salary.
Developer: Inherits from Employee with an additional attribute programming_language.
Manager: Inherits from Employee with an additional attribute team_size.
Intern: Inherits from Developer and has an additional attribute internship_duration.
Implement a method to display the details of each employee.'''

class Employee:
    def __init__(self):
        self.name = input("Enter Employee Name Here : ")
        self.salary = input("Enter Employee Salary Here : ")
 
    def employee_details(self):
        print("Employee Name: ",self.name)
        print("Employee Salary: ",self.salary)
 
class Developer(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.programming_language = input("Enter Language Name Here :  ")
 
    def developer_details(self):
        self.employee_details()
        print("Programming Language Name : ",self.programming_language)

class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.team_size = input("Enter Team Size : ")

    def manager_details(self):
        self.employee_details()
        print("Team Size: ",self.team_size)

class Intern(Developer):
    def __init__(self):
        Developer.__init__(self)
        self.internship_duration = input("Enter Intern Duration Here : ")

    def intern_details(self):
        self.developer_details()
        print(f"Internship Duration: {self.internship_duration} months")

e=Employee()

#print('-'*30)

e.employee_details()


#print('-'*30)


d = Developer()

#print('-'*30)

d.developer_details()


#print('-'*30)


m = Manager()

#print('-'*30)

m.manager_details()


#print('-'*30)


i=Intern()

#print('-'*30)

i.intern_details()