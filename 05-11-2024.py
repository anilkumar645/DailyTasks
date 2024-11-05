#nested class:- block inside another block is called nested block


class employee:
    def __init__(self,name,age,skill):
        self.name = name
        self.age = age
        self.skill = skill
    
    def display(self):
        print(self.name)
        print(self.age)
        print(self.skill)
    
    class employement:
        def __init__(self,cmpnyname,salary,domain):
            self.cmpnyname = cmpnyname
            self.salary = salary
            self.domain = domain
        def display(self):
            print(self.cmpnyname)
            print(self.salary)
            print(self.domain)
    
    m = employement("Tcs",45000,"python")
    m.display()

p = employee("anilkumar",25,"html,css,js")
p.display()