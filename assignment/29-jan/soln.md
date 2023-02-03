

## Assignment Questions 
1. Who developed Python Programming Language?
    * It was created by Guido van Rossum and first released in the year 1991.

2. Which type of Programming does Python support?
    * It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming.

3. Is Python case sensitive when dealing with identifiers?
    * Yes

4. What is the correct extension of the Python file?
    * .py

5. Is Python code compiled or interpreted?
    * Generally we call python as interpreted language
    * But is half correct
    * The source code is converted into bytecode(.pyc) that is then executed by the Python virtual machine.

6. Name a few blocks of code used to define in Python language?
```
def myfunction():
    print("Hello World")

def addNum(num1, num2):
    print(num1 + num2)
addNum(2, 4)
```

7. State a character used to give single-line comments in Python?
    * `# (hash)` is used to make a single line comment
    * `''' (triple quotes)` are used to make multi-line comment.

8. Mention functions which can help us to find the version of python that we are currently working on?
```
from platform import python_version
python_version()
```

9. Python supports the creation of anonymous functions at runtime, using a construct called
    * Using a construct called lambda.

10. What does pip stand for python?
    * preferred installer program
    * pip is the package manager for Python packages.

11. Mention a few built-in functions in python?
    * print(), type(), len(), bool()

12. What is the maximum possible length of an identifier in Python?
    * There is no length limit for Python identifiers. But not recommended to use below 79 characters.

13. What are the benefits of using Python?
    * Simple and easy to learn
    * Open Source And Free
    * Large Standard Library
    * Platform Independent and Portability
    * Large Community Support

14. How is memory managed in Python?
    * In Python memory allocation and deallocation method `is automatic` as the Python developers created a `garbage collector` for Python so that the user does not have to do manual garbage collection.

15. How to install Python on Windows and set path variables?
    * Download python .exe file from python official website
    * For path setup
        1. Find in C-Drive where python is install
        2. Copy the path
        3. Go to `This PC > Properties > Advanced system settings > Environment Variables`
        4. Select user/System variable and add the PATH here

16. Is indentation required in python? 
    * Indentation in Python is very important.
    * Python uses indentation to indicate a block of code.