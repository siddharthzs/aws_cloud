# Serverless Application Model
CloudFormation for Serverless. The Serverless Application Model is an extension to cloudformation used to define Serverless applications.

Simplified Syntax. SAM uses a simplified syntax for defining serverless resources: APIs, Lambda functions, DynamoDB tables, etc.

SAM CLI. Use the SAM CLI to package your deployment code, upload it to S3, and deploy your Serverless application.

> sam package \
    -- template-file ./mytemplate.yml \ 
    -- output-template-file sam-template.yml \
    -- s3-bucket s3-bucket-name

> sam deploy \
    -- template-file sam-template.yml \ 
    -- stack-name mystack \
    -- capabilites CAPABILITY_IAM



## Exam Tips
* define and provision serverless applications using CloudFormation
* sam package: Packages your application and uploads to S3
* sam deploy: deploys your serverless app using CloudFormation 