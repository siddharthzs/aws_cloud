# Content Devliery Network
A system of distributed servers which deliver webpages and other web content.
Easy and cost effective way to distribute content with low latency and high data transfer speeds.

### CloudFront Edge Location
location where content will be cached. this is seperated to an aws region az.
### CloudFront Origin
the origin of all the files that the distribution will server. can be an s3 bucket, and Ec2 instance, an ELB or Route53
### CloudFront Distribution
Name given to origin and configuration settings for the content you wish to distribute using CDN.
