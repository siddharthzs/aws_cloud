# CI/CD
Continous Integration, Continous Delivery / Deployment.

* Software Development Best Practice
* Make Small Changes & Automate Everything!
Small, incremental code changes. Automate as much as possible e.g. code integration, build, test and deployment.
Continous Integration Workflow
* Shared Code Repository
* Automated Build
* Automated Test




### CodeCommit
Source control services enabling teams to collaborate on code, html pages, scripts, images and binaries

### CodeBuild
Compiles Source code, runs tests and produces packages that are ready to deploy.

### CodeDeploy
Automates code deployments to any instance, including EC2, Lambda and on-premises.
Quickly release new features. Avoid downtime during deployments. 

* In-Place Deployment (Rolling Update): The application is stopped on each instance and the new release is installed. Lambda is not supported. Capacity is reduced during the deploymen.
* Blue/Green : New instances are provisioned and the new realese is installed on the new instance. Blue represents the active deployment, green is the new release. Green instances can be created ahead of time. You pay for 2 enivronments until you terminate the old servers.

* AppSpec File: configuration file defines the parameters to be used during a CodeDeploy deployment. For EC2 and on-premises systems, YAML only. For Lambda YAML and JSON suppored. File structure depends on wheather you are deploying to Lambda or EC2.
File Structure: 
    version = reservered for future use. currently the allowed value is 0.0
    files = location of any application files that need to be copied and where they should be copied to.
    OS = The Operating System version you are using, e.g. linux, windows.
    Hooks = Lifecycle event hooks. Scripts which need to run at set points in the deployment lifecycle. Hooks have a very specific run order.

```
**LifeCycle event Hooks**
Lifecycle event Hooks are run in a specific order known as the Run Order.

Phase1: De-register instaces from a Load Balancer.
Phase2: The realnuts & bolts of the application deployment.
