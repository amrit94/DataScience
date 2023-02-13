## 12 Feb Assignment Solution 

Q1. What is an Exception in python? Write the difference  between Exceptions and Syntax errors

* An `unwanted and unexpected event` that disturbs normal flow of program is called exception.

* Timming
    * A syntax error is when something goes wrong during parsing.
    * Exception occurs during execution of program
* Reason
    * A syntax error occurs when wrong sintax is used
    * Exception occurs when there is programming logic issue.


Q2. What happens when an exception is not handled? Explin with an example  

* When an exception is not handled
    * It disturbs normal flow of program
    * Complete program will not get executed
```
marks = 10000

# perform division with 0
a = marks / 0
print(a)
```
* Normal flow of program is disturbed


Q3. Which Python statements are used to catch and handle exceptions? 
Explin with an example

```
try:
    Risky Code
except XYZ:
    Handling code/Alternative Code
```
* The try-except block is used to handle exception

```
try:
    marks = 10000

    # perform division with 0
    a = marks / 0
    print(a)
except:
    print('Exception is handled')
```

Q4. Explain with an exmple:
    * try and else
    * finally 
    * raise 

* **try-except**
    * To handle exception and proper execution of program we put Risky code inside `try-except` block
```
try:
    marks = 10000
    a = marks / 0
    print(a)
except:
    print('Exception is handled'
```
* **try-else**
    * If there is no exception then else block will be executed
```
x,y = 2, 4
try:
    # Floor Division : Gives only Fractional
    # Part as Answer
    result = x // y
except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")
else:
    print("Yeah ! Your answer is :", result)
```
* **finally**
    * finally block is `executed always` irrespective of whether exception raised or not raised and whether exception handled or not handled.
```
try:
	k = 5//0 # raises divide by zero exception.
	print(k)
except ZeroDivisionError:
	print("Can't divide by zero")
finally:
	print('This is always executed')
```
* **raise**
    * We can define custom exception by using `"raise" keyword`
```
age = -1
if age < 1:
    raise RuntimeError("Wrong age")
else:
    print("Done")
```

Q5. What are Custom Exceptions in python? Why do we need Custom Exeptions? Explain with an exmple

* Custom exception are those which are created using `"raise" keyword`

Some time we have to define and raise exceptions explicitly to indicate that something 
goes wrong ,such type of exceptions are called Custom Exceptions

* In the below example an exception is created if the age variable is smaller than 1
```
age = -1
if age < 1:
    raise RuntimeError("Wrong age")
else:
    print("Done")
```


Q6. Create  a custom exception class. Use this class to handle an exception

```
class NegativeAgeException(Exception):
    def __init__(self,arg):
        self.msg=arg

age = -1
if age < 1:
    raise NegativeAgeException("Age can't be Negative")
else:
    print("Valid Age")
```