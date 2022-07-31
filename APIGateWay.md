# API GateWay
Publish, Maintain and Monitor APIs
Supports RESTFul APs which are optimized for stateless, serverless workloads, 
Websocket APIs are for real-time, two-way, stateful communication eg chat types.

### Importing APIs to API Gateway
import api using a definition file. OpenAPI,formely known as swager, is supported.

### API Gateway Caching and throttling
* Caches you endpoints response
* TTL : default is 300 seconds for cache response.
* API Gateway Returns the Cached Response
* default limit for throttling is 10,000 requests per second, per region.
* The maximum concurrent requests is 5k requests across all APIs, per region,
* 429 Error Too Many Requests


To prevent your API from being overwhelmed by too many requests, Amazon API Gateway throttles requests to your API using the token bucket algorithm, where a token counts for a request. You can enable usage plans to restrict client request submissions to within specified request rates and quotas. This restricts the overall request submissions so that they don't go significantly past the account-level throttling limits in a Region. Amazon API Gateway provides Per-client throttling limits that are applied to clients that use API keys associated with your usage policy as client identifier.
