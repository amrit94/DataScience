## 17 Feb Assignment Solution 
### Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use MongoDB over SQL databases?

MongoDB is an open-source document-oriented database that is designed to store a large scale of data and also allows you to work with that data very efficiently. It is categorized under the NoSQL (Not only SQL) database because the storage and retrieval of data in the MongoDB are not in the form of tables. 


Non-relational databases
* NoSQL Database is a non-relational Data Management System, that does not require a fixed schema. 
* It avoids joins, and is easy to scale.
* The major purpose of using a NoSQL database is for distributed data stores with humongous data storage needs.
* NoSQL is used for Big data and real-time web apps.
* For example, companies like Twitter, Facebook and Google collect terabytes of user data every single day.


MongoDB over SQL databases
* MongoDB is highly and easily scalable
* Maintaining NoSQL Servers is Less Expensive
* No Schema or Fixed Data model


### Q2. State and Explain the features of MongoDB.

Features of MongoDB
* Sharding
* Indexing
* Replication
* Document-Oriented
* High performance
* Ad-hoc Queries
* Schema-Less Database


### Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.

```
import pymongo

# Connect to DB
client = pymongo.MongoClient("mongodb://localhost:27017/labDB")

# Create DB
db = client["labDB"]

# Create Collection
collection = db['Products']
```


### Q4. Using the database and the collection created in question number 3, write a code to insert one record, and insert many records. Use the find() and find_one() methods to print the inserted record.


```
d = {'companyName': 'pwskills',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'}
     
rec = collection.insert_one(d)

list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},
    
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},
    
    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]
collection.insert_many(list_of_records)

all_record = collection.find()
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")


print(collection.find_one())
```

### Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to demonstrate this.

```
# All the record at once present
all_record = collection.find()

for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")

# Useing filter in find()
for i in collection.find({'companyName': 'iNeuron'}):
    print(i)
```

### Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.

The sort() method specifies the order in which the query returns the matching documents from the given collection. You must apply this method to the cursor before retrieving any documents from the database. 

* `db.Collection_Name.sort({filed_name:1 or -1})`
* The value is 1 or -1 that specifies an ascending or descending sort respectively.
```
db.student.find().sort({age:1})
```

### Q7. Explain why delete_one(), delete_many(), and drop() is used.

`delete_one()`
* delete the first documents that match with the specified filter criteria in a collection.
```
# db.collection.deleteOne(filter, options)

db.employees.deleteOne({ salary:7000 }) 
```

`deleteMany()`
* delete all the documents that match with the specified filter criteria in a collection.
```
# db.collection.deleteMany(filter, options)
db.employees.deleteMany({ salary:7000 })
```

`drop()`
  * used to drop a collection from the database.
```
# db.collection.drop()
db.employees.drop()
```
