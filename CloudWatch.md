# CloudWatch

What can CloudWatch Monitor?
* Compute: EC2 Instance, Auto Scaling groups, Elastic Load Balancer, Route53 health check, Lambda
* Storage & Content Disk: EBS Volumnes, Storage Gateway, CloudFront
* Database & Analytic: DynamoDB tables, ElasticCache nodes, RDS instances, Redshift, Elastic Map Reduce
* Other: SNS topics, SQS Queue, API Gateway, Estimated AWS charges


**CloudWatch Agent** - define your own metrices. 
**CloudWatch Logs** allows you to monitor operations system and application logs.

### EC2 Logs
* Default EC2 host-level metrics consist of: CPU, network, disk and status check.
* Metrics are stored indefinitely.
* You can retrieve data from any EC2 or Elastic Load Balancer instance even after it has been terminated.
* By Default Ec2 does not send operating system-level metrics to CloudWatch
* By installing the cloudwatch agent on your Ec2 instance, you can collect operating system metrics and send them to CloudWatch.
* Memory Usages, processes running on your instance, amount of free disk space, CPU idle time, etc.
* By default EC2 sends metric data to cloudwatch in 5-minutes inervals.
* For an additional charge you can enable detailed montioring that sends metircs at 1-minute intervals.
* For custom metrics, the default is 1-minute intervals, and you can configure high resolution metrics that are sent at 1 second intervals.

### CloudWatch Alarms
* This can include ec2 cpu utilization, Elatic Load Balancer latency, or even the charges on your AWS bit.
* You can set appropriate thresholds to trigger the alarms and actions to be taken if an alarm state is reached.
* You can set an alarm that sends you a notification or execution an Auto Scaling policy if CPU utlization exceeds 90% on your EC2 instace for more than 5 minutes.


### CloudWatch Concepts
* **CloudWatch Metrics**: A metric is a variable to monitor. Metrics are uniquely defined by a name, a namespace, and zero or more dimensions.
A namespace is a container for CloudWatch metrics. e.g. EC2 uses the AWS/EC2 namespace. Create your own namespace to publish custom metric data.
You must specify a namespacce for each data point or value that you publish to CloudWatch. Metrics in different namespaces are isolateed from each other. Metrics from different applications are not aggregated into same statistics.

* **CloudWatch Dimensions**: A dimension is like a filter.
Name/Value Pair. Can be used to filter cloudwatch data. 
InstanceId. Use the instanceid dimensions to search for metrics relating to a specific EC2 instance.
Aggregate. Cloudwatch can aggregate data across dimensions for some services.


### CloudWatch vs CloudTrail
**CloudTrail** : Records user activity in your AWS account. Cloudtrail records event reated to creation, modification, or deletion of resources ( such as IAM users, S3 buckets, and EC2 instances).
By default, you can view the last 90 days of account activity.
* Records API calls for you AWS account. 
* Delivers log files containing API calls to an S3 bucket.
* can be integrated with Cloudwatch logs.



### Using CloudWatch Actions 
* What are CloudWatch Actions?
* PutMetricData
* PutMetricAlarm
* Example


### CloudWatch API
Supports a long list of different actions.
These actions allow you to publish, monitor, and alert on a variety of metrics.
These are particularly powerful when creating custom metrics for monitoring and alterting for your applications.
