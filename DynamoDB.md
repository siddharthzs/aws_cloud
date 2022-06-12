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
All items with the same partition key are stored together and then sorted according to the sort key value.


### Query / Scan
#### Query 
* A query finds items in a table based on the primay key attribute and a distinct value to search for.
* Use an Optional sort key name and value to refine the results.
* Results are always sorted by the sort key
* You can reverse the order by setting the **ScanIndexForward** parameter to false.
* By default, queries are eventually consistent.

#### Scan
* A scan operation examines every item in the table. By default, it returns all data attributes.
* User ProjectionExpression parameter to refine the scan to only return attribute you want.


Query is More Efficient than a Scan
As the table grows, the scan operation takes longer.
A scan operation on a large table can use upthe provisioned throughput for a large table in just a single operation.
#### Improving Performance
* set a smaller page size
* running a larger number of smaller operations wil allow other requests to succeed without throttling.
* scan process data sequrntially, returning 1mb increments before moving on to retrive the next 1mb of data.
* scans one partition at a time.
*


### Provisioned Throughput(measured in capacity units)
#### Read Capacity Units
1 x Read capacity unit = 1 x strongly consistent read of 4kb per second.
