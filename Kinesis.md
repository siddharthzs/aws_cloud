# Kinesis
A family of services which enables you to collect, process, and analyze streaming data, in real-time.
Allows you to build custom applications for your own business needs.

#### Steaming DATA?
Data generated continouly by thousands of data sources, which typically send in the data records simultanously and in small size.

* Financial Transactions
* Stockprices
* Game data
* Social media feeds
* location tracking data
* iot sensors
* clickstream data
* log files


## Core Services Under Kinesis
* Kinesis Streams : Streams data and video to allow you to build custom applications that process data in real-time.
Data Streams and Video Streams.
* Kinesis Data Firehose : Capture, transform, load data streams into AWS data stores to enable near-real-time analytics with BI tools.
* Kinesis Data Analytics
Analyze, query and transform streamed data in real-time using standard SQL. Store the results in an AWS data store.

### Kinesis Shards
* Kinesis streams are made up of shards.
* Each shard is a sequence of one or more data records and provides a fixed unit of capacity
* 5 reads per second, The max total read rate is 2mb per second.
* 1000 writes per second, max total write rate is 1mb per second.

### kinesis Shards vs Consumers
* A kinesis data stream is a set of shards.
* A shard is a sequence of data records in a stream, each data record has a unique sequence number.

Consumers
* Kinesis client library runs on the customer instances.
* Tracks the number of shards in your stream.
* Discovers new shards when you reshard.
* The KCL ensures that for every shard there is a record processor.
* Manages the number of record processors relative to the number of shards & consumers
* If you have only one consumer, the KCL will create all the record processors on a single consumer.
* If you have two consumers it will load balance and create half the processors on one instance and half on another.

What about scaling out the consumers?
* with KCL, generally you should ensure that the nubmer of instances doesn not exceed the number of shards(except for failure or standby purposes).
* You never need multiple instances to handle the processsing load of one shard.
* Howeer, one worker can process multiple shards.
* Use an Auto Scaling group, and base scaling decisions on CPU loads on your consumers.
* KCL adds another reord processor on each consumer
