# CI/CD first part (APP)



## My CI/CD has 2 files:
* **For Application**
* For Infrastucture

## Pipeline for app wrote for 2 branch (Develop && Master)

### develop:
* Checkout Repo
* Cloning Repo
* Build Image for frontend
* Build image for backend
* Analasis code with SonarQube
* Deploy Back's && Front's Images in DockerrHub with tag dev-latest

### master:
* Checkout Repo
* Cloning Repo
* Build Image for frontend
* Build image for backend
* Deploy Back's && Front's Images in DockerrHub with tag latest


## Credentials:
For this pipelines using only credential for Docker Hub Regestry
