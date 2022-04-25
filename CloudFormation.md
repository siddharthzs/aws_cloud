# CloudFormation
Manage, configure, and provision your AWS infrastruture as Code.

1) Resources are defined using CloudFormation template.
2) CloudFormation interprets the template and makes the appropriate API calls to create the resources you have defined.
3) supports YAML or JSON

### CloudFormation Benefits
* Consistent : Infrastruture is provisioned consistently, with fewer mistakes.
* Quick and Efficient : Less time and effort than configuring things manually.
* Version Control
You can version control and peer review your templates.
* Free to Use : you get charged for the aws resources you create using cloudformation.
* Manage updates : can be used to manage updates and dependencies
* RollingBack: YOu can roll back to a previous state and delete the entire stack as well.

### Process
Create Your Template
Store in S3 bucket
CloudFormation willread and make API calls to create
resulting set of resources that CloudFormation builds is called a Stack.


CloudFormation Template Structure(YAML)
```
AWSTemplateFormatVersion: "2010-08-02"
Descript: "Create an EC2 instance"
Metadata: 
    Instances:
        Description: "Web Server Instace"
Parameters: 
    EnvTpe:
        Description: "environment type"
        Type: String
        AllowedValues: 
            - prod
            - test
Conditions: 
    CreateProdResources: !Equals [!Ref EnvType, prod]
    Mappings:
    RegionMap:
        eu-west-1:
            "ami: "ami-obakdsf"
Transform: #include snippets of code outside the main template
    Name: 'AWS::Include'
    Parameters: 
        Location: 's3://s3bucketname.yaml'
Resources: # the AWS resources you are deployment
    EC2Instace: 
        Type: AWS::EC2::Instance
        Properties:
        Outputs:
    InstaceID:
        Description: The Instace ID
        Value: !Ref EC2Instance
            InstanceType: t2.micro
            ImageId: ami-a34l3skdjf1
    Outputs:
        InstancID:
            Description: THeinstace ID
            Value: !Ref EC2Instace
            ImageId: ami-aldskf39    

```
