
"""1.Create a class Person that has instance variables name, age, and gender. Add methods to:
Initialize these variables.
Update the age.
Display the person's information.
 Exercise:
 > Create multiple instances of the Person class.
 > Change the age of one person and display the updated information."""

class Person:
    def __init__(self,name,age,gender):
        self.name = name 
        self.age = age 
        self.gender = gender 
    
    def updated(self,new_age):
        self.age = new_age

    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)

person1 = Person("anilkumar",25,"male")
person2 = Person("anil.a",27,"male")

person1.display()
person2.display()

person1.updated(31)
print("After updated age")
person1.display()
        

"""2.Create a class Company that keeps track of the total number of employees using 
    a static variable total_employees. 
  Each employee has instance variables name and department. Every time an employee is added, 
  the total_employees should increment.
  
  Exercise:
   >Create multiple employee instances.
   >Print the total number of employees after adding each new employee.
   >Check whether changing the total_employees in one instance affects the others."""

class Company:
    
    TotalEmployee = 0

    def __init__(self,ename,edepartment):
        self.ename = ename 
        self.edepartment = edepartment

        Company.TotalEmployee += 1 

        print("Employee added: ")
        print(self.ename)
        print(self.edepartment)

employee1 = Company("Anilkumar","It")
employee2 = Company("kumar","Testing")
employee3 = Company("sai","non-it")
employee4 = Company("pavan","HR")

Company.TotalEmployee += 1 

print("After manuel increment ,TotalEmployee: ",Company.TotalEmployee)




"""3.Create a class Rectangle that has instance variables length and width. 
  Add a method calculate_area that calculates and prints the area of the rectangle using local variables
    inside the method.
  Exercise:
    >Create instances of the Rectangle class with different lengths and widths.
    >Calculate and print the area for each rectangle."""

class Rectangle:
    def __init__(self,length,width):
        self.length = length 
        self.width = width 

    def calculate_area(self):
        area = self.length * self.width 
        print("The area of rectangle is: ",area)

rectangle1 = Rectangle(5,3)
rectangle2 = Rectangle(7,4)
rectangle3 = Rectangle(10,2)

rectangle1.calculate_area()
rectangle2.calculate_area()
rectangle3.calculate_area()




"""4.Create a class Employee where:
  Each employee has an instance variable salary.
  There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
  Write a method total_salary that calculates the total salary for an employee (including the bonus).
  Exercise:
   >Create several employee instances with different salaries.
   >Change the bonus amount (static variable) and see how it affects all employees.
   >Calculate and print the total salary for each employe""" 

class Employee:
    bonus = 1000

    def __init__(self,salary):
        self.salary = salary 
        
    def calculate_total_salary(self):
        total_salary = self.salary + Employee.bonus 
        print("Total salary including bonus:",total_salary)

e1 = Employee(5000)
e2 = Employee(6000)
e3 = Employee(7000)

print("Initial bonus:",Employee.bonus)

e1.calculate_total_salary()
e2.calculate_total_salary()
e3.calculate_total_salary()


Employee.bonus = 2000 

print("\nUpdayed bonus:",Employee.bonus)
e1.calculate_total_salary()
e2.calculate_total_salary()
e3.calculate_total_salary()