### Shell

- 1. Run server:
``` brew services start mongodb-community ```

- 2. Launch MongoDB console:
``` mongo ```

- 3. Change default DB -> my own
``` use ``` command, which uses the new DB name as an argument
ex: 
``` use hellzDB ```
(obs: it won't be shown at current DB list using the command '>show dbs' because MongoDB only creates the physical DB when you input data into it)
``` show dbs ```

- 4. Create a collection using shell: point db to target database and create collection using dot notation

```
use hellzDB

db 

hellzDB.myCollection.insertOne({x:1})

```


#### https://realpython.com/introduction-to-mongodb-and-python/