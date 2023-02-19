## 15 Feb Assignment Solution 
Q1. What is multiprocessing in python? Why is it useful?

Multiprocessing refers to the ability of a system to support `more than one processor` at the same time.

Applications in a multiprocessing system are `broken to smaller routines` that run independently. The operating system allocates these threads to the processors improving performance of the system.

The biggest advantage of a multiprocessor system is that it helps you to get more work done in a shorter period.




Q2. What are the differences between multiprocessing and multithreading?

A multiprocessing system has more than two processors whereas Multithreading is a program execution technique that allows a single process to have multiple code segments

Multiprocessing improves the reliability of the system while in the multithreading process, each thread runs parallel to each other.

Multiprocessing helps you to increase computing power whereas multithreading helps you create computing threads of a single process

In Multiprocessing, the creation of a process, is slow and resource-specific whereas, in multithreading, the creation of a thread is economical in time and resource.

Multithreading avoids pickling, whereas Multiprocessing relies on pickling objects in memory to send to other processes.

Multiprocessing system takes less time whereas for job processing a moderate amount of time is taken.




Q3. Write a python code to create a process using the multiprocessing module.

```
import time
import multiprocessing as mp

def task1(sleep_sec):
    print(f'Sleeping for {sleep_sec} seconds')
    time.sleep(sleep_sec)
    print(f'Finished sleeping: {sleep_sec}')


if __name__ == "__main__":
    start_time = time.perf_counter()
    p1 = mp.Process(target=task1, args=(3,))
    p2 = mp.Process(target=task1, args=(3,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish_time = time.perf_counter()
    print(f"Program finished in {(finish_time - start_time):.3f} seconds"
```



Q4. What is a multiprocessing pool in python? Why is it used?

A pool is a collection of processes used to execute tasks in parallel.
Pools help divide an enormous task into smaller parts that multiple processors can handle.

Withe the Pool we can increase the no of workers and then execute the task simultaneously.



Q5. How can we create a pool of worker processes in python using the multiprocessing module?

```
import multiprocessing as mp
import time
def square(n):
    time.sleep(2)
    res = n**2
    print(res, end=' ')
    return res

if __name__ == '__main__':
    with mp.Pool(5) as pool :
        out = pool.map(square , [3,4,5,6,6,7,87,8,8])
        print(out)
#[9, 16, 25, 36, 36, 49, 7569, 64, 64]
```
With the Pool set to have `workers=5` and the list has 9 elements, which means 5 component is executed simultaneously.



Q6. Write a python program to create 4 processes, each process should print a different number using the multiprocessing module in python.

```
import multiprocessing as mp
import time

def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    print(" Process %s Finished." % work_data[0])


if __name__ == '__main__':
    work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])
    p = mp.Pool(4)
    p.map(work_log, work)
```