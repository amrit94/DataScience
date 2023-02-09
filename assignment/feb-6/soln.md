## 06 Feb Assignment Solution 

Q1. Create a function which will take a list as an argument and return the product of all the numbers
after creating a flat list.
Use the below-given list as an argument for your function.

list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
Note: you must extract numeric keys and values of the dictionary also.

```
def get_flat_list_product(list1):
    flat_list = []
    for i in list1:
        if type(i) in [list, set, tuple]:
            for j in i:
                if type(j) in [int, float]:
                    flat_list.append(j)
        elif type(i) == dict:
            for j in i:
                if type(j) in [int, float]:
                    flat_list.append(j)
                values = i[j]
                if type(values) in [int, float]:
                    flat_list.append(values)
                elif type(values) in [list, set, tuple]:
                    for k in values:
                        if type(k) in [int, float]:
                            flat_list.append(k)
        elif type(i) in [int, float]:
            flat_list.append(i)
    print(flat_list)
    flat_list = get_flat_list(list1)
    return reduce(lambda x, y: x * y, flat_list)

list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
print(get_flat_list_product(list1))
```



Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption should be such that, for a the output should be z. For b, the output should be y. For c, the output should be x respectively.

Also, the whitespace should be replaced with a dollar sign. Keep the punctuation marks unchanged. 

Input Sentence: I want to become a Data Scientist.
Encrypt the above input sentence using the program you just created.

Note: Convert the given input sentence into lowercase before encrypting. The final output should be
lowercase.

```
def encrypted_data(my_input):
    my_input = my_input.lower()
    new_str = ''
    for i in my_input:
        letter = i
        if 96 <= ord(i) <= 122:
            letter = chr(122 - (ord(i) - 97))
        elif i == ' ':
            letter = '$'
        new_str += letter
    return new_str

my_input = 'I want to become a Data Scientist.'
print(encrypted_data(my_input))
# r$dzmg$gl$yvxlnv$z$wzgz$hxrvmgrhg.
```
