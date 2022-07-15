import subprocess
import random as rd

fileNames = [
    "CloudWatch.md",
    "SAM.md",
    "gitcommit.py",
    "IAM.md"
]

# s = subprocess.call('git init', cwd='D:/cloud-aws/aws_cloud')

curFile = fileNames.pop(rd.randrange(len(fileNames)))
OutFile = open(f'aws_cloud/{curFile}','a')
InFile = open(curFile,'r')
date = 13
fileContent = InFile.readlines()
i = 1
x = rd.randrange(5)
y = rd.randrange(6)
s = subprocess.call(f'git add . && git commit --date "{date} day ago" -m "created a new file {curFile}"', cwd='D:/cloud-aws/aws_cloud',  shell=True)
for content in fileContent:
    OutFile.writelines(content)
    if(i%10 == 0):
        OutFile.close()
        
        if(y <= 1):
            s = subprocess.call(f'git add . && git commit --date "{date} day ago" -m "learning {curFile[:-3]}"', cwd='D:/cloud-aws/aws_cloud',  shell=True)
        elif(y > 1  and y <= 3):
            s = subprocess.call(f'git add . && git commit --date "{date} day ago" -m "learned more on {curFile[:-3]}"', cwd='D:/cloud-aws/aws_cloud',  shell=True)
        elif(y > 3):
            s = subprocess.call(f'git add . && git commit --date "{date} day ago" -m "continue on {curFile[:-3]}"', cwd='D:/cloud-aws/aws_cloud',  shell=True)
        OutFile = open(f'aws_cloud/{curFile}','a')
        x-=1
        if(x == 0):
            date = date-1
            x = 3
    i+=1

OutFile.close()
InFile.close()


    


# set /p txt=Your Text Content; 
# echo %txt% > "Location\textfile.txt"import subprocess
import random as rd
import filecmp

fileNames = ['1.1_cloud_computing.md', '1.2_aws_setup.md', '1.3_IAM.md', '1.4_S3_101.md', '1.5_cloudFront.md', '1.6_EC2_101.md', 'aws_cloud', 'aws_mindMap.PNG', 'CICD.md', 'CloudFormation.md', 'CloudFront.md', 'CloudWatch.md', 'CodeArtifact.md', 'DynamoDB.md', 'EC2.md', 'ECS.md', 'ElasticBeanStalk.md', 'gitcommit.py', 'IAM.md', 'index.js', 'Kinesis.md', 'KMS.md', 'LoadBalance.md', 'S3.md', 's3examtips.PNG', 'SAM.md', 'Screenshot.png', 'SES.md', 'SNS.md', 'SQS.md', 'test.py']
date = 20
# s = subprocess.call('git init', cwd='D:/cloud-aws/aws_cloud')
for _ in range(31):
    try:
        curFile = fileNames.pop(rd.randrange(len(fileNames)))
        OutFile = open(f'aws_cloud/{curFile}','a+')
        InFile = open(curFile,'r')
        comp_res = filecmp.cmp(curFile, f'aws_cloud/{curFile}')
        if(comp_res):
            exit()
        date = date - 3
        fileContent = InFile.readlines()
        i = 1
        x = rd.randrange(5)
        y = rd.randrange(6)
