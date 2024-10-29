
# Brief about oops 

# object oriented programming is way of approach design and developing a software.
#  the components of the software and interactions between them resemblence real life objects.
#  proper usage of oops concept help us to build well organised system.that are essy to use and extend.


# use cases 

# software development 
# gui applications
# real time systems 
# large-scale systems 
# simulation system 

#importence of oops 

#encapsulation 
#abstraction
#inheritence
#polimorphim


class Mobile:
    def __init__(self, model, storage):
        self.model = model
        self.storage = storage


obj = Mobile("iPhone 12 Pro", "128GB")
print(obj.model)

obj = Mobile("infinix 50 pro", "128GB")
print(obj.model)
