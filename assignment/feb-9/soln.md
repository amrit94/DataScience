
## 09 Feb Assignment Solution 

Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed and average_of_vehicle.

```
class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle
```


Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
Create a method named seating_capacity which takes capacity as an argument and returns the name of the vehicle and its seating capacity.

```
class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

class Car(Vehicle):
    def seating_capacity(self, capacity):
        return self.name_of_vehicle, capacity
```


Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.

* When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.

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

Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this class.

* We use getters & setters to add validation logic around getting and setting a value.
* To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

```
class Geek:
	def __init__(self, age = 0):
		self._age = age
	
	# getter method
	def get_age(self):
		return self._age
	
	# setter method
	def set_age(self, x):
		self._age = x

raj = Geek()

# setting the age using setter
raj.set_age(21)

# retrieving age using getter
print(raj.get_age())

print(raj._age)
```


Q5.What is method overriding in python? Write a python code to demonstrate method overriding.

* Override parent methods in child class.
* Change the implementation of a method in child class that is defined in parent class.

```
class Vehicle:
    def apply_break(self):
        print('Velicle applying break')


class Car(Vehicle):
    def apply_break(self):
        print('Car applying break')
        
c1 = Car()
c1.apply_break()
```