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
