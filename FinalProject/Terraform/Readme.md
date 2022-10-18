# CI/CD second part (INFRASTRUCTURE)



## My CI/CD has 2 files:
* For Application
* **For Infrastucture**

## Pipeline for infrastucture wrote for 2 branch (Develop && Master)

### develop && master:
* Checkout Repo
* Cloning Repo
* Creating VPC
* Creating RDS
* Creating EKS
* Availability check helm's chart
  * *IF* already have - **Update**
  * *ELSE*  - **Install**



## Credentials:
| Credentials | Technology | Destiny |
| ------------ | ------------ | ------------ |
| *AWS_ACCESS_KEY_ID* | Terraform | for access for AWS |
| *AWS_SECRET_ACCESS_KEY* | Terraform | for access for AWS |
| *AWS_REGION* | Terraform | for access for AWS |
| *POSTGRES_USER* | Helm(Type64) | For correct work appliaction |
| *POSTGRES_PASSWORD* | Helm(Type64) | For correct work appliaction |
| *REMOTE_USER* | Helm(Type64) | For correct work appliaction |
| *REMOTE_PASSWORD* | Helm(Type64) | For correct work appliaction |


## Variables

| Parametrs | Destiny |
| ------------ | ------------ |
| *PATH_INFRASTRUCTURE* | For start script applying infrastucture with terraform |
| *PATH_APP* | For start script applying application with helm |
| *tag* | Dynamic variable for applying need's verion appliaction |
