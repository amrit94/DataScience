## 10 Feb Assignment Solution 

Q1. Which function is used to open a file? What are the different modes of opening a file? Explain each mode of file opening.

* Open file using `open()` function
* There are many modes for opening a file but 3 are most useful
    * Read
        * Read the content of the file
    * Write
        * Create or re-write the content of the file
    * Append
        * Add more content to the file

Q2. Why close() function is used? Why is it important to close a file?

* The close() method closes an open file.
* You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.


Q3. Write a python program to create a text file. Write ‘I want to become a Data Scientist’ in that file. Then
close the file. Open this file and read the content of the file.

```
f1 = open("test.txt" ,'w' )
f1.write("I want to become a Data Scientist")
f1.close()

data = open("test.txt" , "r")
data.read()
data.close()
```

Q4. Explain the following with python code: read(), readline() and readlines().

* read()
    * read and reaturn all lines as string
* readline()
    * reads a line of the file and return it in the form of the string. 
* readlines()
    * reads all the lines at a single go and then return them as each line a string element in a list


Q5. Explain why with statement is used with open(). What is the advantage of using with statement and open() together?

* The with keyword in Python is used as a context manager.
* It making sure to release these resources after usage
    * i.e it make sure that file is closed after used


Q6. Explain the write() and writelines() functions. Give a suitable example.

* write() is used to write a string to an already opened file
* writelines() method is used to write a list of strings in an opened file

```
f1 = open("test.txt" ,'w' )
f1.write("Data Science Masters course")
f1.close()


f = open("demofile3.txt", "a")
f.writelines(["See you soon!", "Over and out."])
f.close()
```