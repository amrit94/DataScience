## 14 Feb Assignment Solution 

1. What is multithreading in python? Why is it used? Name the module used to handle threads in python

* Multithreading allows you to `break down` an application `into multiple sub-tasks` and run these tasks simultaneously.
* Multithreading is defined as the ability of `a processor to execute multiple threads concurrently`.

If you use multithreading properly, your application `speed`, `performance`, and rendering can all be improved.

Python provides one `inbuilt module "threading"` to provide support for developing threads.




2. Why threading module used? Write the use of the following functions
* activeCount()
* currentThread()
* enumerate()


`active_count()`
* This function returns the number of active threads currently running

```
import time
from threading import *
def test(id) :
    for i in range(id):
        time.sleep(0.5)

thred = [Thread(target=test , args = (i,)) for i in [10 , 2 , 5]]
for t in thred:
    t.start()
print("The Number of active Threads:",active_count())
time.sleep(3)
print("The Number of active Threads:",active_count())
```

`current_thread()`
* We use the current_thread() function to get the current thread object.
```
import threading
print("Current Executing Thread:",threading.current_thread().getName())
```

`enumerate()`
* This function returns a list of all active threads currently running
```
from threading import *
threads =enumerate()
for i in threads:
    print(i)
```



3. Explain the following functions
* run()
* start()
* join()
* isAlive()

`start()`
* When a thread instance is created, it doesn’t start executing until its start() method (which invokes the target function with the arguments you supplied) is invoked.

`run()`
* The .run() method executes any target function belonging to a given thread object that is now active.
* It normally executes in the background after the start() method is invoked.

```
import threading

class CustomThread(threading.Thread):
  def run(self):
    print("This is my custom run!")

custom_thread = CustomThread()
custom_thread.start()
```

`isAlive()`
* isAlive() method checks whether a thread is still executing or not.

`join()`
* If a thread wants to wait until completing some other thread then we should go for join() method.



4. Write a python program to create two threads. Thread one must print the list of squares and thread two must print the list of cubes
```
from threading import *

def square(nlist):
    print([i*i for i in nlist])

def cube(nlist):
    print([i*i*i for i in nlist])
    
nlist = [5 , 2 , 3]
t1 = Thread(target=square , args = (nlist,))
t2 = Thread(target=cube , args = (nlist,))
t1.start()
t2.start()
```



5. State advantages and disadvantages of multithreading

Disadvantages of multithreading

* It needs more `careful synchronization`.
* My have `Deadlocks` and `Race conditions`
* It imposes context `switching overhead`.
* It can consume a large space of stocks of blocked threads.
* It needs support for thread or process.
* If a parent process has several threads for proper process functioning, the child processes should also be multithreaded because they may be required.

Advantages of multithreading

* Enables `efficient utilization` of the resources as the threads share the data space and memory.
* Allows the `concurrent and parallel` exwcution of various tasks.
* Reduction in `time consumption or response time`, thereby increasing the performance.




6. Explain deadlocks and race conditions.

A situation where a set of `processes are blocked` because each process is `holding a resource and waiting for another` resource acquired by some other process. This block situation is `called Deadlock(DL)`

Race condition is an `undesirable condition` that usually happens due to `multiple threads accessing a shared resource at the same time`. Due to which shared data are `not synchronized`,
