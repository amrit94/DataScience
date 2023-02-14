Q1. Explain why we have to use the Exception class while creating a Custom Exception.
Note: Here Exception class refers to the base class for all the exceptions.

* Exceptions need to be derived from the Exception class, either directly or indirectly. 
* Instead of creating own exception class from scratch it's better to inherit all the feature available in the parent Exception class




Q2. Write a python program to print Python Exception Hierarchy.

```
def treeClass(cls, ind=0):
    # print name of the class
    print('-' * ind, cls.__name__)

    # iterating through subclasses
    for i in cls.__subclasses__():
        treeClass(i, ind + 3)

print("Hierarchy for Built-in exceptions is : ")
treeClass(BaseException)
```



Q3. What errors are defined in the ArithmeticError class? Explain any two with an example.

* ArithmeticError raised for various arithmetic errors
    * OverflowError
    * ZeroDivisionError
    * FloatingPointError

ZeroDivisionError exception occurs when a number is divided by 0
```
# ZeroDivisionError
try :
    10 / 3
except Exception as e :
    print(e)
```
An OverflowError exception is raised when an arithmetic operation exceeds the limits to be represented
```
# OverflowError
j = 5.0

for i in range(1, 1000):
    j = j**i
    print(j)
```



Q4. Why LookupError class is used? Explain with an example KeyError and IndexError.

* The LookupError exception in Python forms the base class for all exceptions that are raised when an index or a key is not found for a sequence or dictionary respectively.

IndexError error occurs when an attempt is made to access an item in a list at an index which is out of bounds.
```
# IndexError
l = [1,2,3,3]
l[10]
```

KeyError is raised when a mapping key is accessed and isn't found in the mapping.
```
# KeyError
d = {1: [3,4,5,6] , "key" :"sudh"}
d["key10"]
```



Q5. Explain ImportError. What is ModuleNotFoundError?

* The ImportError is raised when an import statement has trouble successfully importing the specified module.
* It may occur due to -
    * Module name not found
    * Circular import
* ModuleNotFoundError
    * This error occurs when you're trying to access or use a module that cannot be found.



Q6. List down some best practices for exception handling in python.

* Always use specific exception
* Print always a valid msg
* Always avoid to write a multiple exception handling
* Always try to log the error
* Prepare a proper documnetation