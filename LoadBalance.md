# Elastic Load Balance

### Application Load Balance -> HTTP and HTTPS
Used for load balancing HTTP/HTTPS trffic. They operate at Layer 7 and are application-aware.
OSI Model -- Look at it
They support advance request routing to specific web servers based on the HTTP header.
It can use HTTP request header to determine where to send each request header.
### Network Load Balance -> TCP and high performance
Used for load balancing TCP traffic where extreme performance is required. Operates at Layer 4(Transport Layer).
Capable of handling millions of requests per second while maintaining ultra-low latencies.
