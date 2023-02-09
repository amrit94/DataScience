## 04 Feb Assignment Solution 

Q1. Create a python program to sort the given list of tuples based on integer value using a lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
```
nlist = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

nlist.sort(key = lambda x: x[1])
print(nlist)
# [('Virat Kohli', 24936), ('Jack Kallis', 25534), ('Ricky Ponting', 27483), ('Sachin Tendulkar', 34357)]
```


Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```
nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: x*x, nlist))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
```
nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple(map(lambda x: str(x), nlist))
# ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
```


Q4. Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25.
```
from functools import *

nlist = [i for i in range(1, 25)]
reduce(lambda x, y: x*y, nlist)
# 3628800
```

Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function.
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
```
nlist = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
list(filter(lambda x: x%2 == 0 and x%3 == 0, nlist))
# [6, 60, 90, 120]
```

Q6. Write a python program to find palindromes in the given list of strings using lambda and filter function.
['python', 'php', 'aba', 'radar', 'level']
```
nlist = ['python', 'php', 'aba', 'radar', 'level']
list(filter(lambda x: (x == "".join(reversed(x))), nlist))
```