import subprocess
import random as rd

fileNames = [
    "1.1_cloud_computing.md",
    "CodeArtifact.md",
    "DynamoDB.md",
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

