# Amazon SQS


## Short Pollong
REturns a resposne immediatetly even if the messae queue being polled is empty.
This can result in lot of empty responses if nothing is in the queue.
You will still pay for these responses.
## Long Polling
Periodically polls the queue.
Doesn't return a response until a message arrives in the message queue or the long poll times out.
can save money!
Long polling is generally preferable to short polling.

## Exam Tips
* Allows us to decouple the components of an application so that they are independent.
* Pull-based, not push-based.





