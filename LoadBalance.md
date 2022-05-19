# Elastic Load Balance

### Application Load Balance -> HTTP and HTTPS
Used for load balancing HTTP/HTTPS trffic. They operate at Layer 7 and are application-aware.
OSI Model -- Look at it
They support advance request routing to specific web servers based on the HTTP header.
It can use HTTP request header to determine where to send each request header.
### Network Load Balance -> TCP and high performance
Used for load balancing TCP traffic where extreme performance is required. Operates at Layer 4(Transport Layer).
Capable of handling millions of requests per second while maintaining ultra-low latencies.
As it is high performance, it is also the most expensive option.
### Classirc Load Balance -> Both HTTP and TCP
Legacy Option
Support Layer 7 specific features, such as X-Forwarded-For headers(to identify originating request IP address) and sticky sessions(allows keep sending requests which originates from same session on to the same web server making the session sticky).
Support Layer 4 load balancing for applications that rely purely on the TCP protocol.

### GateWay Load Balancer -> 
Allow you to load balance workloads for third-party virtual appliances running in AWS, such as Virtual applications purchased using the AWS Marketplace
Virtual firewalls from companies like Fortinet, Palo Alto, Juniper, Cisco
IDS/IPS system from companies like CheckPoint, Trend Micro, etc.



### Common Load Balance Errors
* Error 504 Gateway Timeout
the target failed to respond.
The Elastic Load Balancer could not establish a connection to the target, e.g., the web server, database, Lambda funciton.
Your application is having issues.
Identify where the application is failing and fix the problem.

