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
                       = 2 x eventually consistent reads of 4kb per second(default).
#### Write Capactiy Units
1 x write capcity unit = 1 x 1KB writes per second.
* Read and write capcity requirements can be forecasted.
* Predictable application traffic.
* Application traffic is consistent or increases gradually.
* You have more control over the cost.

### On-Demand Capcity
DynamoDb instanly scales up and down based on the activity of your application.
* Unknow workloads
* Unpredictable application traffic
* spiky, short-lived peaks.
* A pay-per-use model is desired
* It might be more difficult to predict the cost

## DynamoDB Accelerator (DAX)
It is a fully-managed, clustered in-memory cache for DynamoDB.
Delivers up to a 10x read performance improvement. Microsecond performance for millions of requests per second.
* DAX is write-thorugh caching service.
* Reduces the read load on DynamoDB tables.
* May be able to reduce provisioned read capacity on your table and save money on your AWS bill.

#### Not Suitable For
* required strongly consistent reads.
* applications whch are mainly write-intensive
* do not perform many read operations.
* do not require microsecond response times.

## Time-To-Live(TTL)
