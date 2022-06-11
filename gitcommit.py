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
