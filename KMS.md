# Key Management Service
Managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.
Seamlessly integrated with many AWS services to make encrypting data in those services as easy as checking a box.

With KMS, it is simple to encrypt your data with encryption keys that you manage. 

**Whenver you are dealing with sensitive information**
consider KMS

* EBS
* EFS
* CloudTrail
* Developer Tools

### CMK Customer Master Key
Encrypt/ Decrypt data up to 4KB.
Used to generate/ encrypt/ decrypt the data key.
and the Data Key is used to encrypt/ decrypt your data.
This is called as Envelope Encryption

CMK cannot be exported outside of KMS.

* SetUp CMK : Alias, Description, Key Material
* Key Administrative Permissions: IAM users and roles that can administer the key through the KMS API.
(Users, Roles, Admin Permissions) 
* Key Usage Permissions: IAM users and roles that can use the key to encrypt and decrypt data.


### Envelope Encryption 
Encrypting the key that encrypts our data.
The CMK is used to encrypt the data key ( or envelope key).
The data key encrypts our data.
Used for encrypting anything over 4KB.
Using evvelope encryption avoids sending all your data into KMS over the network

## Exam Tips
* AWS-Managed CMK : AWS-provided and AWS-managed CMK. Used on your behalf with the AWS services interagated with KMS.
* Customer-Managed CMK : You create, own and manage yourself.
*Data Key: Encryption keys that you can use to encrypt data, including large amount of data.

