a = 'hello world'

mystring = 'abcdefghijklmn'

# slicing
print(mystring[::-1])

username = "Sammy"
color = "blue"

# dot format
print("{} favoure color is {}".format(username,color))

# f string literals!!!! 
print(f"{username} chose {color}")

# Sets - unique representation of unique elements
x = set()
x.add(1)
x.add(2)
x.add(3)
x.add(3)
x.add(3)
print(x)

myList = [1,2,3,3,3,4,4,4,1,2,33,44,2,2,2]
print(set(myList))

# iterating a list of tuples
# Tuple unpacking
myitem = [('a',1), ('b',2), ('c',3)]
for (letter,num) in myitem:
    print(letter)
    print(num)

# SCOPE - LEGB Rule
# LOCAL
# ENCLOSING
# GLOBAL
# BUILT-IN

#  OOP 

class University():
    def __init__(self, city):
        # print('University created')
        self.city = city
    
    def register(self):
        print('University registered')

    def government_list(self):
        print('University added to government list')

class Student(University):

    # class object attributes
    university = 'UoS'
    department = 'acse'

    # methods
    def __init__(self,city,id,firstname,secondname):
        University.__init__(self, city)
        self.id = id
        self.firstname = firstname
        self.secondname = secondname

    def student_id(self):
        print('student Id:',self.id)

class Math():

    def __init__(self,shape):
        self.shape = shape
    
    def report_shapes(self):
        # print(f'the shape selected is {self.shape}')
        print(f'the shape selected is {self.shape}')


class Circle(Math):
    # Object Class atrribute
    pi = 3.14159265359

    def __init__(self,shape,radius=1):
        Math.__init__(self,shape)
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi 

    def circumference(self):
        return 2 * self.pi * self.radius  

    def report_shapes(self):
        print('report_shapes is now overwritten')

    def __repr__(self):
        return f'Shape: {self.shape}, Radius: {self.radius}'
   


myCircle = Circle(shape='Circle',radius=20)
print(myCircle)
# print(myCircle.radius)
# print(myCircle.area())
# print(myCircle.circumference())
# print(myCircle.report_shapes())


