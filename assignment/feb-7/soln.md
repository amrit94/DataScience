## 07 Feb Assignment Solution 

Q1. You are writing code for a company. The requirement of the company is that you create a python function that will check whether the password entered by the user is correct or not.
The function should take the password as input and return the string “Valid Password” if the entered password follows the below-given password guidelines else it should return “Invalid Password”.
Note:
1. The Password should contain at least two uppercase letters and at least two lowercase letters.
2. The Password should contain at least a number and three special characters.
3. The length of the password should be 10 characters long.

```
def check_password(password):
    if len(re.findall('[a-z]', password)) >= 2 and len(password) >= 10:
        if len(re.findall('[A-Z]', password)) >= 2:
            if len(re.findall('[0-9]', password)) >= 1:
                if len(re.findall('[@$_]', password)) >= 3:
                    return "Valid Password"
    return "Invalid Password"

print(check_password('am#r_IT@1'))
# Invalid Password

print(check_password('am@r_I@1'))
# Valid Password
```



Q2. Solve the below-given questions using at least one of the following:
1. Lambda function
2. Filter function
3. Zap function
4. List Comprehension

* Check if the string starts with a particular letter
```
print((lambda x,y : x[0] == y)('Amrit', 'A'))
```
* Check if the string is numeric
```
print((lambda x: x.isnumeric())('111'))
```
* Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)]
```
nlist = [("mango",99),("orange",80), ("grapes", 1000)]
nlist.sort(key = lambda x: x[1])
```
* Find the squares of numbers from 1 to 10
```
[i*i for i in range(1, 10+1)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
* Find the cube root of numbers from 1 to 10
```
[i*i for i in range(1, 10+1)]
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```
* Check if a given number is even
```
print((lambda x: x%2==0)(10))
# True
```
* Filter odd numbers from the given list. [1,2,3,4,5,6,7,8,9,10]
```
nlist = [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x%2 != 0, nlist))
# [1, 3, 5, 7, 9]
```
* Sort a list of integers into positive and negative integers lists. [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
```
nlist = [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]

print(list(filter(lambda x: x >= 0, nlist)))

print(list(filter(lambda x: x < 0, nlist)))
```