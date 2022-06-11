# DynamoDB
**Fast and Flexible NoSql Database**
**Fully Managed**
Consistent, single-digit millisecond latency at any scale. 
Supports key-value data models. supports document formats are JSON, HTML, and XML.
Use Cases: A great fit for mobile, web, gaming, ad teach, IoT, and many other applications.


### DynamoDB consistency Model
* Eventually Consisent Reads : consistency across all copies of data is usually reached within a second. **Best for read performance.**
* Strongly Consistent Reads : A strongly consistent read always reflects all successful writes. Writes are relected across all 3 locations at once. **Best for read consistency.**
* ACID Transactions : DynamoDb transactions provide the ability to perform ACID transactions (Atomic, Consistent, Isolated, Durable).


### DynamoDB Primary Key

* Partition Key: A unique attirbute. Value of the partition key is input to an internal hash function which determines the partition or physical location on which the data is stored.

* Composite Key : Partition Key + Sort Key
A item in the table may have the same partition key, but they must have a different sort key
