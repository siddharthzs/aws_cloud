# Elastic BeanStalk

**Infrastruture**
Provisioning infrastruture, load balancing, Auto Scaling, and application health monitoring.
**Aplicaion Platform**
Installation  and management of the application stack, incuding patching and updates to your operating system and application platform.
**You Are in Control**
You have complete administrative control of the AWS resources.

Developers don't have to be sysadmins.
YOu don't need to worry about any of the underlying infrastructure needed to run the application.
Get your appication to market faster.
Fastest and simplest way to deploy your application in AWS.


# Updating Elastic BeanStalk

* All at Once Deployment : Involves a services interruption. Rolling back requires a further all at once update.
* Rolling Deployment Policy : Reduced capacity during deployment. Rolling back requires a further Rolling update.
* Rolling with Additional Batch : Maintains full capacity during deployment. Lanuches an additional batch of instances. Rolling back requries a further rolling update.
* Immutable Deployments : Deploys the new version to a fresh group of instances.
* Immutable Deployment with Traffic Splitting: Enables Canary Testing. Install the new version on a new set of instances. Forwards a percentage of incoming client traffic to the new application version for a specified evaluation period.

## Customize Elastic BeanStalk Environment

### For Pre-Amazon Linux 2 Environment
* Configuration File: Define packages to install, create Linux users and groups, run shell commands, enable services, and configure load balancers.
* YAML or JSON : These are files written in YAML or JSON format.
* Constraints : The file must have .config extension and be inside a folder called .ebextensions in the top-level directory of your application source code bundle.

### For Amazon Linux 2
* use Buildfile, Procfile, and platform hooks whenever possible to configure and run custom code on your environment instances during instance provisoning.
* Buildfile : For commands that run for short periods and then exit upon task compeltion (eg., running a shell script).Create your Buildfile in root directory. Format: <process_name>: <command> ==> "make : ./build.sh"
* Procfile : Long-running application processes (eg, commands to start and run your application). Elastic beanstalk expects processes defined in the procfile to run continously. It monitors and restarts any processes that terminate.
Create Procfile in root directory. Format: <proces_name> : <commnad>
==> web : bin/myserver 
* Platform Hooks: Custome scripts or executable files that you would like Elastic BeanStalk to run at a chosen stage of the EC2 provisioning process. Stored in dedicated directories in your application source code. 
* **.platform/hooks/prebuild** : Files that you want Elastic BeanStalk to run before it builds, sets up, and configures the application and web server.
* **.platform/hooks/predeploy** : Files that you want to run afer it set up and configures the application and web server but before it deploys them to the final runtime location.
* **.platform/hooks/postdeploys** : Files that run after Elastic Beanstalk deploys the application.


## Integrating RDS With Elastic Beanstalk
Elastic BeanStalk supports two ways of integrating an RDS database with your Beanstalk environment. 

Option1: RDS Inside the Elastic BeanStalk
* Launch the RDS instance from within the Elastic BeanStalk
* If you terminate the environment, the database will also be terminated.
* It is a good option for Deve and Test deployments, not so good for Prod.

Option2: Launch RDS Outside of Elastic BeanStalk
* Use the RDS console or AWS CLI to create your RDS database.
* It allows you to tear down your application environment without affecting the database instance.
* This is the preferred approach for Production Systems.
* An additional Security Group must be added to your environments Auto Scaling group.
* You will need to provide connection string information to your application servers using Elastic BeanStalk environment properties.

## Migrating Applications to Elatic BeanStalk

1) Windows Web Application Migration Assistant 
* Enables you to migrate .NET application, or entire website from windows servers in your data center, to Elastic BeanStalk in AWS.
* Open Source

## Deploy Docker Container using Elatic BeanStalk
Single Docker Container: you can either run a single docker container on an EC2 instance provisoned by Elastic Beanstalk
Multiple Docker Container : Use Elastic BeanStalk to build an ECS cluster and deploy multiple docker container on each instance.
* Can deploy multiple Docker instances to an ECS cluster.# Elastic BeanStalk

**Infrastruture**
Provisioning infrastruture, load balancing, Auto Scaling, and application health monitoring.
**Aplicaion Platform**
Installation  and management of the application stack, incuding patching and updates to your operating system and application platform.
**You Are in Control**
You have complete administrative control of the AWS resources.

Developers don't have to be sysadmins.
YOu don't need to worry about any of the underlying infrastructure needed to run the application.
Get your appication to market faster.
Fastest and simplest way to deploy your application in AWS.


# Updating Elastic BeanStalk

* All at Once Deployment : Involves a services interruption. Rolling back requires a further all at once update.
* Rolling Deployment Policy : Reduced capacity during deployment. Rolling back requires a further Rolling update.
* Rolling with Additional Batch : Maintains full capacity during deployment. Lanuches an additional batch of instances. Rolling back requries a further rolling update.
* Immutable Deployments : Deploys the new version to a fresh group of instances.
* Immutable Deployment with Traffic Splitting: Enables Canary Testing. Install the new version on a new set of instances. Forwards a percentage of incoming client traffic to the new application version for a specified evaluation period.

## Customize Elastic BeanStalk Environment

### For Pre-Amazon Linux 2 Environment
* Configuration File: Define packages to install, create Linux users and groups, run shell commands, enable services, and configure load balancers.
* YAML or JSON : These are files written in YAML or JSON format.
* Constraints : The file must have .config extension and be inside a folder called .ebextensions in the top-level directory of your application source code bundle.

# Elastic BeanStalk

**Infrastruture**
Provisioning infrastruture, load balancing, Auto Scaling, and application health monitoring.
**Aplicaion Platform**
Installation  and management of the application stack, incuding patching and updates to your operating system and application platform.
**You Are in Control**
You have complete administrative control of the AWS resources.

Developers don't have to be sysadmins.
YOu don't need to worry about any of the underlying infrastructure needed to run the application.
Get your appication to market faster.
Fastest and simplest way to deploy your application in AWS.


# Updating Elastic BeanStalk

* All at Once Deployment : Involves a services interruption. Rolling back requires a further all at once update.
* Rolling Deployment Policy : Reduced capacity during deployment. Rolling back requires a further Rolling update.
* Rolling with Additional Batch : Maintains full capacity during deployment. Lanuches an additional batch of instances. Rolling back requries a further rolling update.
* Immutable Deployments : Deploys the new version to a fresh group of instances.
* Immutable Deployment with Traffic Splitting: Enables Canary Testing. Install the new version on a new set of instances. Forwards a percentage of incoming client traffic to the new application version for a specified evaluation period.

## Customize Elastic BeanStalk Environment

### For Pre-Amazon Linux 2 Environment
* Configuration File: Define packages to install, create Linux users and groups, run shell commands, enable services, and configure load balancers.
* YAML or JSON : These are files written in YAML or JSON format.
* Constraints : The file must have .config extension and be inside a folder called .ebextensions in the top-level directory of your application source code bundle.

### For Amazon Linux 2
* use Buildfile, Procfile, and platform hooks whenever possible to configure and run custom code on your environment instances during instance provisoning.
* Buildfile : For commands that run for short periods and then exit upon task compeltion (eg., running a shell script).Create your Buildfile in root directory. Format: <process_name>: <command> ==> "make : ./build.sh"
* Procfile : Long-running application processes (eg, commands to start and run your application). Elastic beanstalk expects processes defined in the procfile to run continously. It monitors and restarts any processes that terminate.
Create Procfile in root directory. Format: <proces_name> : <commnad>
==> web : bin/myserver 
* Platform Hooks: Custome scripts or executable files that you would like Elastic BeanStalk to run at a chosen stage of the EC2 provisioning process. Stored in dedicated directories in your application source code. 
* **.platform/hooks/prebuild** : Files that you want Elastic BeanStalk to run before it builds, sets up, and configures the application and web server.
* **.platform/hooks/predeploy** : Files that you want to run afer it set up and configures the application and web server but before it deploys them to the final runtime location.
* **.platform/hooks/postdeploys** : Files that run after Elastic Beanstalk deploys the application.


## Integrating RDS With Elastic Beanstalk
Elastic BeanStalk supports two ways of integrating an RDS database with your Beanstalk environment. 

Option1: RDS Inside the Elastic BeanStalk
* Launch the RDS instance from within the Elastic BeanStalk
* If you terminate the environment, the database will also be terminated.
* It is a good option for Deve and Test deployments, not so good for Prod.

Option2: Launch RDS Outside of Elastic BeanStalk
* Use the RDS console or AWS CLI to create your RDS database.
* It allows you to tear down your application environment without affecting the database instance.
* This is the preferred approach for Production Systems.
* An additional Security Group must be added to your environments Auto Scaling group.
* You will need to provide connection string information to your application servers using Elastic BeanStalk environment properties.

## Migrating Applications to Elatic BeanStalk

1) Windows Web Application Migration Assistant 
