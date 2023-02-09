
# 02 feb Assignment Solution 
Q1. What are the characteristics of the tuples? Is tuple immutable?

* Tuple is Read Only version of List
* Tuple are immutable and insertion order is preserved
* Duplicates and Heterogeneous objectsare allowed



Q2. What are the two tuple methods in python? Give an example of each method. Give a reason why  tuples have only two in-built methods as compared to Lists.

* `count()`- Returns the number of times a specified value occurs in a tuple
* `index()`	- Searches the tuple for a specified value and returns the position of where it was found
```
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
print(Tuple1.count(3))
# 3

print(Tuple1.index(3))
# 3
```
* Tuple are immutable so they have only 2 in-built methods



Q3.  Which collection datatypes in python do not allow duplicate items? Write a code using a set to remove  duplicates from the given list. 
List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
* set don't allow duplicates
```
List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]

unique_list = list(set(List))
print(unique_list)
```


Q4. Explain the difference between the union() and update() methods for a set. Give an example of  each method. 

* union()
    * We can use this function to return all elements present in both sets
```
x={10,20,30,40}
y={30,40,50,60}

print(x.union(y)) 
# {10, 20, 30, 40, 50, 60}
```

* update(x, y, z)
    * To add multiple items to the set
```
s = {10, 20}
s.update([40, 50], (1, 2))
print(s)
# {1, 2, 40, 10, 50, 20}
```


Q5. What is a dictionary? Give an example. Also, state whether a dictionary is ordered or unordered.

* Dictionaries are used to store data values in key-value pairs
```
d2 = dict(a=1, b=2,c=3)
# OP: {'a': 1, 'b': 2, 'c': 3}
```
* As of Python version 3.7, dictionaries are ordered.
* In Python 3.6 and earlier, dictionaries are unordered.



Q6. Can we create a nested dictionary? If so, please give an example by creating a simple one-level  nested dictionary.
```
d3 = {'a': 1, 'b': {'c': 2, 'd': 3}}
print(d3)
# {'a': 1, 'b': {'c': 2, 'd': 3}}
```


Q7. Using setdefault() method, create key named topics in the given dictionary and also add the value of  the key as this list ['Python', 'Machine Learning’, 'Deep Learning'] 
dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}

```
dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}
dict1.setdefault('topics', 'Machine Learning')
# 'Machine Learning'

dict1.setdefault('topics', 'Deep Learning')
# 'Machine Learning'

print(dict1)
# {'language': 'Python', 'course': 'Data Science Masters', 'topics': 'Machine Learning'}

```



Q8. What are the three view objects in dictionaries? Use the three in-built methods in python to display  these three view objects for the given dictionary. 
dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']} 

```
dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

print(dict1.keys())
# ['Sport', 'Teams']

dict1.values()
# ['Cricket', ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']]

dict1.items()
# [('Sport', 'Cricket'), ('Teams', ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand'])]
```
