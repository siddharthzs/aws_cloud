# Lambda

You are charged based on the number of requests, their duration, and the amount of memeory used by your Lambda function.

* ReQuest : the first 1 milion request per month are free. then 0.20 per month per 1 million requests.
* Duration : you are charged in 1 milisecond increment. The price depends upon the amount of memeory you allocate to the Lambda.
* Price per GB-second: $0.00001667 per GB-second.
A function that uses 512 MB nad runs for 100ms. The first 400,000GB-seconds per months are free.



### Version
when you create a Lambda function, there is only one version: $Latest


# Step Functions
Step Functions provides various types of state machines that feature different workflows to cater to a variety of tasks that you would like to orchestrate.
The Kind of tasks you are orchestrating determine the type of workflow you should use.


* Standard Workflow: Long-running, durable, and auditable workflows that may run for up to a year. Ful execution history avaialble for up to 90 days after completion.
Task are never executed more than once unless you explicity specify retry actions.
when processing payments, you only want a payment to be processed once, not multiple times. (non-idempotent actions)
Change in State? a request is non-idempotent if it always causes a change in state (e.g. sending the same email mutiple times causes a change in state because you end up with multiple emails in your inbox).


* Express Workflows: short-lived up to 5 minutes. great for high-volume, event-processing-type workloads. 
Idempotent actions, eg. transforming input data and storing the result in DynamoDB.
At-least-once model, ideal if there is possiblility that an execution might be run more than once of you require multiple concurrent executions. 
Identical Request has no side effect, a request is considered idempotent if an identical request can be made once or serveral times in a row with no addiotional side effects(e.g. reading data from a databae or S3 bucket).