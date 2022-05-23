# Elastic Compute Cloud (EC2)
secure, resizable compute capacity in the cloud
like a VM, only hosted in AWS instead of your own data center.
Designed to make web-scale cloud computing easier for developers.
The capacity you want when you need it.
You are in completed control of your own instances.

# EC2 Instance Priciing 
On Demand -> Pay by the hour or the second depending on the type of instance you run.
    Flexible, Short-Term, Testing The Water
Reserved--> Reserved capacity for one or three years. Up to 72% discounton the hourly charge.**Regional**
    Predicatble Usage, Specific Capacity Requirements 
    Pay Up-Front

    Standard Rls (cannnot upgrade)
    Conertible Rls (change to a different Reservered instacnt type of equal or greater value)

    Sheduled Rls (Launch within the time window you define, day, week or month)


Spot --> Purchase unused capacity at discout of up to 90%. Price fluctuate with supply and demand.
Dedicated-> A physical EC2 server dedicated for your use. The most expensive option.

Flexible : Application the have flxible start and end time
Urgent Capacity : Image Processing
Cost Sensitive

Dedicared Hosts 
    Compliance: Regulatory requirements that may not support multi-tenant virtualization 
    Licensing:Great for licensing which does not support multi-tenancy or cloud deployments.
    On-Demand: Can be purchased on-demand
    Reserved: Can be purchased as a reservation for up to 70% off the on-demand price.

### Saving Plans
    Save up to 73%
    Commit to one or Three Years
    Super Flexible

    AWS Pricing Calculator
    


## EC2 Instance Type
Hardware -> the instance type determines the hardware of the host computer used for your instance

Capabilities-> Each instance type offers different compute, memory, and storage capabilites are grouped in instance families

#### Micro Instance ::->
#### General Purpose ::->
#### Compute Optimized ::->
#### FPGA instance ::->
#### GPU instance ::->
#### Machine Learning ASIC Instance ::->
#### Memory optimized ::->
#### Storage optimized ::->

## EBS Volumes
Elastic Block Store
#### Whare are EBS Volume
Storage volumes that you can attach to your EC2 instances.
