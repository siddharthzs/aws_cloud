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

