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

The Resource section is Mandatory. The Transform section is used to reference additional code stored in S3, allowing for code re-use.
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

The Resource section is Mandatory. The Transform section is used to reference additional code stored in S3, allowing for code re-use.


### Exporting CloudFormation Stack Values


### CloudFormation Nested Stacks
enables re-use of CloudFormation code for common use cases. eg: standard configuation for a load balancer, web server, or application server.
Instead of copying out the code each time, create a standard template for each common use case and reference from within your CloudFormation template.
```
Resources:
Type: AWS::CloudFormation::Stack
Properties:
    NotificationARNs:
        - String
    Parameters:
        AWS CloudFormation Stack Parameters
      Tags:
        - Resource Tag
      TemplateUrl: http://s3.amazonaws.com/.../template.yml
      TimeoutInMinutes: Integer


```

### Exam Tips
* We Export the Values 
```
"Outputs": {
    "PublicSubnet" : {
        "Description" : "aksdjf",
        "Value" : { "Ref" : "PublicSubnet"},
        "Export" : {"Name": {"Fn::Sub": "${AWS::StackName}-SubnetID"}}
    }
}
```
* We Import Values
```
"Fn::ImportValue":{
    "Fn::Sub": "${NetworkStackParameter}-SubnetID"
}
```
* Nested Stacks allows to re-use your cloudformation code so you don't need to copy/paste every time. Stack Resource Type , reference it in the Resource section of any CloudFormation template using the Stack resource type.

* Infrastructure As Code: CloudFormation allows you to manage, configure, and provision AWS infrastruture as YAML or JSON code.
