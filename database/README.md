# EC500_Spring19

Storage Module(from https://github.com/alexlin0625/EC500_Spring19/tree/alert-system)
================
**The storage module contains four basic functions**

  * add: obtain json from input module and store patient's data

  * delete: input patient's id(number) in order to complete the deletion. 

  * Update: update patient's data according to the id(number) and json. 

  * Search: input patient's id(number) in order to search the current data of the patient. 

**Table elements**

  * {id, name, gender, age, blood pressure, oxygen, pulse, time}

db.frame.py
================
This allows you to connect to a existed MongoDB database and store data from the input_module. All functions are within a class storage that we created
```bash
class storage:
	'''
	class for storage of data from input module
	basic functions: CRUD(create, read, update, delete)
	'''
```

**database selection**
: MongoDB
```bash
self.client = pymongo.MongoClient()
```

**package**
```bash
import pymongo
import json
```
