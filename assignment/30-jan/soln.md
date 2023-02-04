## 30 Jan Assignment Solution

1. Write a program to accept percentage from the user and display the grade according to the following 

```
def get_grade(percentage):
    if percentage > 90:
        return 'A'
    elif percentage > 80:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'D'

percentage = int(input())
print(get_grade(percentage))
```


2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the 
following criteria: 

```
def get_road_tax(price):
    if price > 100000:
        return 0.15 * price
    elif price > 50000:
        return 0.1 * price
    else:
        return 0.05 * price

price = int(input())
print(get_road_tax(price))
```

3. Accept any city from the user and display monuments of that city. 

```
def get_city_monuments(city):
    if city == 'Delhi':
        return 'Red Fort'
    elif city == 'Agra':
        return 'Taj Mahal'
    elif city == 'Jaipur':
        return 'Jal Mahal'

city = input()
get_city_monuments(city)
```



4. Check how many times a given number can be divided by 3 before it is less than or equal to 10.

```
number = int(input())
if number > 10:
    print((number-10)//3)
else:
    print(0)
```

5. Why and When to Use while Loop in Python give a detailed description with example
    * We use do while when we want to execute the body of the at `least once`.
    * And `until some condition false`, then we should go for while loop.


6. Use nested while loop to print 3 different pattern. 
```
i = 0
while i < 6 :
    j = 0
    while j < i:
        print(i, end=' ')
        j += 1
    i += 1
    print('')

# Output
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
```

7. Reverse a while loop to display numbers from 10 to 1. 
```
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1

# 10 9 8 7 6 5 4 3 2 1 0 
```

8. Reverse a while loop to display numbers from 10 to 1 
```
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1

# 10 9 8 7 6 5 4 3 2 1 0 
```
