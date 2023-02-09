## 05 Feb Assignment Solution 

Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

1. **Class**
	* Classes are used to create `user-defined data structures`.
	* It's like a `blueprint for an object` where we define all its properties and behaviours
2. **Object**
	* An Object is an `instance of a Class` it's like a copy of the class.
	* `Everything in Python is an object`, and almost everything has attributes and methods

```
class Employee:
  def __init__(self, first, last):
    self.first=first
    self.last=last

  # Methods
  def user(self):
    print(self.first)

emp1=Employee('Amrit','Prasad')
emp1.user()
# Amrit
```

Q2. Name the four pillars of OOPs.

* These four pillars are Inheritance, Polymorphism, Encapsulation and Abstraction


Q3. Explain why the `__init__()` function is used. Give a suitable example.

* `__init__()` is an initializer, not a constructor
* It is used to initialize variables of the class

Q4. Why self is used in OOPs?

* self is not a keyword but a variable
* self represents the instance of the class.
* By using the “self”  we can access the attributes and methods of the class in python.
* It binds the attributes with the given arguments.



Q5. What is inheritance? Give an example for each type of inheritance.

* It specifies that the child object acquires all the properties and behaviors of the parent object.
* The new class is known as a `derived class or child class`, and the one whose properties are acquired is known as a `base class or parent class`.
* It provides `re-usability of the code`.


Single Inheritance: 
```
# Base class
class Parent:
    def func1(self):
        print("Parent class")
 
# Derived class
class Child(Parent):
    def func2(self):
        print("Child class")

# Driver's code
object = Child()
object.func1()
object.func2()
```
Multiple Inheritance
```
# Base class1
class Mother:
    def mother(self):
        print('Mother')

# Base class2
class Father:
    def father(self):
        print("Father")

# Derived class
class Son(Mother, Father):
    def parents(self):
        self.mother()
        self.father()

# Driver's code
s1 = Son()
s1.parents()
```

Multilevel Inheritance
```
# Base class
class Parent:
    def func1(self):
        print("Parent class")
 
# Derived class
class Child(Parent):
    def func2(self):
        print("Child class")

class Grandchild(Child):
    def func3(self):
        print("Grand child class")

# Driver's code
object = Grandchild()
object.func1()
object.func2()
object.func3()
```

Hierarchical Inheritance
```
class Parent:
    def func1(self):
        print("Parent class") 

class Child1(Parent):
    def func2(self):
        print("Child 1")
 
class Child2(Parent):
    def func3(self):
        print("Child 2")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
```