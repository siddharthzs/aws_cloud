# Identity And Access Management
AWS Identity and Access Management (IAM) provides fine-grained access control across all of AWS. With IAM, you can specify who can access which services and resources, and under which conditions. With IAM policies, you manage permissions to your workforce and systems to ensure least-privilege permissions.


## What is IAM?
Identity and Access Management(IAM)
    * Allows you to manage users and their level of access to the AWS console.

## Key Features of IAM
    * Centralized Control of your AWS account
    * Shared access to your AWS account
    * Granular Permissions
    * Multi-factor authentication
    * ability to provide temporary access for users, devices, and services nescessary
    * a custom password rotation policy
    * Integartion with many AWS services

## Key Terminology for IAM
    1) Users : end user
    2) Groups : collection of users
    3) Roles : create roles and assign them
    4) Policies : made up of documents, formatted in JSON and provide permisions for users, groups, and roles.

## Exam Tips
    1) IAM : Identity and Access Management
    2) IAM is global : You do not specify a region when dealing with IAM. When you create a user or group, it is created globally.
    3)  You can access the AWS platform in threee ways:
        1. via the console
        2. programmatically
        3. using a software development kit(sdk)
    4) Your root account is the email address you used to set up your aws account. the root accoutn always has full administrator access. You should not give these account credentials to anyone. Insted, create a user for each individual within your orgranization. You should always secure this root account using multi-factor authentication.
    5) A group is simply a place to store your users.
    6) To set the permissions in a group, you need to apply a policy to that group.
    policies consist of JSON



## Web Identity Federation
Simplifies authentication and authorization for web applications. 
**Users Access to AWS Resources** : Users access AWS resources after successfully authenticating with a web-based identity provider like Facebook, Amazon or Google.
**Authentication**: Following successful authentication users receive an authentication code from the web ID provider. 
**Authorization**: Users can trade this authentication code for temporary AWS security credentials, authorizing access to AWS resources.

### Amazon Cognito (web ID federation)
* provides web ID Federation, including sign-up and sign-in functionally for your applications and access for guest users.
* Identity Broker, manages authenticaiton between your application and web ID providers, so you don't need to write any additional code.
* Multiple Devices, Synchronizes user data for multiple devices.
* Recommended for all mobile applicatoins that call AWS services.

**Authenitcation with Amazon Cognito**
Temporary Credentials, cognito broker between the app and facebook, amazon, or google to provide temporary credentials.
Secure and Seamless, No need for the application to embed or store AWS credentials locally on the device.
IAM Role, the temporary credentials map to an IAM role, allowing access to the required resources.
```
**User Pools** : User directories used to manage sign-up and sign-in functionality for mobile and web applications.
**Sign-in** : Users can sign-in directly to the User Pool, or using Facebook, Amazon, or Google.
**Identity Pools** : Identity Pools enable you to provide temporary AWS credentials. Enabling access to AWS services like S3 or DynamoDB.
```

**Cognito Push Synchronization**
* Cognioto tracks the association between user identity and the various different devices they sign-in from.
* Cognito uses Push Synchronizaiton to push updates and synchronize user data across multiple devices.
* Under the hood uses SNS notification to all the devices associated with a given user identity whenever data stored in the cloud changes.


Correct. The preferred way to use web identity federation for mobile apps is to use Amazon Cognito. Reference: Using Amazon Cognito for mobile apps

Correct. With Amazon Cognito identity pool, your users can obtain temporary AWS credentials to access AWS services, such as Amazon S3 and DynamoDB. Identity pools support anonymous guest users, as well as federation through third-party IdPs. Reference: Common Amazon Cognito Scenarios

Correct. After a successful user pool authentication, your app will receive user pool tokens from Amazon Cognito. You can exchange them for temporary access to other AWS services with an identity pool.



**User Pools Vs Identity Pools**
* User Pools: user directories used to manage sign-up and sign-in functionality for mobile and web applications.
* Identity Pools : enables you to provide temporary AWS credentials. Enabling access to AWS services like S3 or dynamoDB.


### Identity Access Management
Used to define user access permissions within AWS.
**AWS Managed Policies** : IAM policy which is created and administered by AWS. across account scope.
**Customer Managed Policies** : poclicy that you create and aadminister inside your own AWS account. with in account scope.
**Inline Policies**: 1:1 relationship between entity and the policy. when you delete the user, group, or role the inline policy will also be deleted.




### STS AssumeRoleWithWebIdentity
STS API : assume-role-with-web-identity is an api provided by STS (Security Token Service).
Temporary Credentials: Returns temporary security credentials for users authenticated by a mobile or web application or using a web ID provider like Amazon, Feacbook, Google, etc.
Web Applications: Regular web applications can use the assuem-role-with-web-identity API. For mobile applications, Cognito is recommended.


### Cross Account Access
Delegate access to resources in different AWS accounts that you own.
Manage Resources in Other Accounts: Share resources in one account with users in a different account.
IAM Role: Create a role in one account to allow access and grant permissions to users in a different account.



