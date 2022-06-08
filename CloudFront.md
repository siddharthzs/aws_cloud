# Content Devliery Network
A system of distributed servers which deliver webpages and other web content.
Easy and cost effective way to distribute content with low latency and high data transfer speeds.

### CloudFront Edge Location
location where content will be cached. this is seperated to an aws region az.
### CloudFront Origin
the origin of all the files that the distribution will server. can be an s3 bucket, and Ec2 instance, an ELB or Route53
### CloudFront Distribution
Name given to origin and configuration settings for the content you wish to distribute using CDN.
### Origin Access Identity (OAI)
An OAI is a special cloudfront user that can access the files in our bucket and server them to users.

### Restrict Access
OAI allows us to restrict access to the contents of our bucket, so that all users must use the CloudFront URL instead of a direct S3 URL.

### CloudFront Allowed Methods
* GET, HEAD <-- Read only -->
* GET, HEAD, OPTIONS <-- Read only -->
* GET,HEAD, OPTIONS, PUT, POST, PATCH, DELETE <--Write and Read-->
