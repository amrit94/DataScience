
Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25.

* `def` -- is used to create a function
```
def get_odd_numbers():
    odd_list = []
    for i in range(1, 25):
        if i%2 != 0:
            odd_list.append(i)
    return odd_list

print(get_odd_numbers())
```



Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use.

* `*args`
    * Used to pass variable number of arguments to the function
* `**kwargs`
    * Used to pass key word variable length arguments to the function
```
def f1(n1,*s):
    print(n1, s)

f1(10)
# 10 ()
f1(10,20)
# 10 (20,)
f1(10, "A", 30)
# 10 ('A', 30)
```
```
def display(**kwargs):
    print(kwargs)

display(n1=10)
# {'n1': 10}

display(rno=100,name="Amrit")
# {'rno': 100, 'name': 'Amrit'}
```



Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].

* Iteration means to access each item of something one after another generally `using a loop`
* list, tuples, dictionaries, etc. -->  all are iterables
* `iter()` -- initialise the iterator object
* `next()` -- used for iteration
```
nlist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
nlist_iter = iter(nlist)
print(next(nlist_iter))
print(next(nlist_iter))
print(next(nlist_iter))
print(next(nlist_iter))
print(next(nlist_iter))
```


Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator function.

* Generator is a function which is responsible to generate a sequence of values.
* yield passs each generate value without waiting for the whole program to complete
* Yield Improves memory utilization and performance

```
def simpleGeneratorFun(): 
  yield 1         
  yield 2         
  yield 3 

x = simpleGeneratorFun() 
print(list(x))
# [1, 2, 3]      
```



Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.

```
# Python program to print all
# prime number in an interval

def get_prime_nos():
	for i in range(1, 1000):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				yield i

lst = get_prime_nos()
for i in range(1, 20):
    print(next(lst), end= ' ')
```