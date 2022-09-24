[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()

# Graduation project


## 📍 Task:

Download csv-files from the remote server, parse them, restructure data and write information to the database. Output data about the current attendance of classes.

---

## 🛢 DataBase [PostgreSQL](https://www.postgresql.org)
* [x] Recording the data update in the database



## 🔩 Backend ([Python](https://www.python.org)/[Django](https://docs.djangoproject.com/en/4.2/))
* [x] Full data output
* [x] Setting up data output with a filter by selected peoples
* [x] Setting up data output with a filter by the selected date
* [x] Configuring the data output of all available dates
* [x] Writing data to the database from files
---
## 🖥 Frontend ([JS](https://www.javascript.com)/[Vue.js](https://v3.vuejs.org))
* [x] Full data output from the database
* [x] Ability to sort data by people
* [x] Ability to sort data by date
* [ ] Displaying information about a specific participant
---
## 🎞 [CI/CD](https://www.jenkins.io/doc/)
*  [x] Start setting up the pipeline
---
## 🛠 [Docker](https://www.docker.com)
* [x] [Backend](https://hub.docker.com/repository/docker/moonlight234/bynet_attendance_back)
* [x] [Frontend](https://hub.docker.com/repository/docker/moonlight234/bynet_attendance_front)
---

## 🧬 IaC ([Terraform](https://terraform.io/))
* [ ] Create playbook for EKS
* [ ] Create playbook for RDS
* [ ] Create playbook for VPC
* [ ] Group all wrote playbooks in alone big playbook
---

## ⛅️ Cloud [AWS](https://aws.amazon.com/)
* [ ] Use EKS as main Kubernetes Cluster
* [ ] Use RDS as main DataBase
* [ ] Create 2 VPC (staging and production)

---



<!-- --- -->



| Criteria  |  Reqiurements  |  Related Module |
| ------------ | ------------ | ------------ |
| SCM  |  Application sources should be placed in Git repository. Branching strategy should be explained. |  Git |
|  Quality gate |  CI/CD pipeline should use some quality/vulnerability control tool like a Sonar or Anchore. |  CI/CD |
|  IaC |  CI/CI and runtime infrastructure should be described as a code using Terraform, CloudFormation, or any similar tool. On the demonstration deployment procedure should be shown. |  Cloud, Terraform, Ansible |
|  Orchestration |  All non cloud-native tools should be spinned up inside a K8S/OpenShift cluster inside a cloud. Application runtime environments should be inside the cluster too. |  Kubernetes |
|  Logging |  Infrastructure should have centralized log collection/display system. Logs of the application components and infra components should be collected. |  Monitoring and Logging |
|  Monitoring |  Infrastructure should have centralized metric collection/display system. Metrics of the application components and infra components should be collected. |  Monitoring and Logging |
|  Runtime/Deployment |  Runtime infrastructure should have production and non production environments.  Deploy/release strategy should be explained. |  CI/CD |
|  Scalability/redundancy |  Scalability should be provided and demonstrated |  Kubernetes |
|  Cloud and Cost efficiency |  Cloud resources and services must be used for the task. Report about the Cloud resource usage and the cost must be provided in the presentation. It should be efficient (minimal) – in accordance to the solving tasks. You can choose any cloud provider taking into account possible extra costs for the resources.  |  Cloud |

---
``` docker-compose --env-file .env.docker up --build ```
```bash
# .env for docker-compose
POSTGRES_PASSWORD=db_password
POSTGRES_USER=dbusername
POSTGRES_DB=name


POSTGRES_NAME=name
POSTGRES_USER=dbusername
POSTGRES_PASSWORD=db_password
DATABASE_PORT=db_port
BACKEND_PORT=port_backend
REMOTE_HOST=IP_ADDRESS
REMOTE_PORT=22
REMOTE_USER=username
REMOTE_PASSWORD=password
REMOTE_FOLDER=/var/tmp/csv_files

DATABASE_HOST=db        # This env you can change on service for connect into Kubernetes Cluster 
BACKEND_URL=backend     # This env you can change on service for connect into Kubernetes Cluster 
```

---
# RoadMap
* [ ] **Database**: AWS RDS

* [ ] **IaC**: Terraform

* [ ] **Orchestration**: EKS

* [ ] **Quality Gate**: SonarKube

* [x] **Scalability**: Horizontal Pod Autoscaling(HPA) in K8S

* [ ] **Monitoring + Logging**: Grafana, Prometheus
