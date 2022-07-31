# X-Ray
it is a tool which helps developers analyze and debug distirubuted applications.
Allowing you to troubleshoot the root cause of performance issues and errors

Provides a visualizaiton of your applicaiton's underlying components.

### X-Ray Service Map
provides an end-to-end view of requests as they travel through your applications.

### X-Ray Configuration Steps
the aws x-ray sdk sends the data to the x-ray daemon which buffers segments in a queue and uploads them to X-Ray in batches.
you need both the X-Ray SDK and the X-Ray daemon on your systems.

Elastic Contianer Service: install the x-ray daemon in its own Docker container on your ECS cluster alongside your app.

#### annotations and indexing
when instruments your applications, you can record additional information about requests by using annotations
key-value pairs