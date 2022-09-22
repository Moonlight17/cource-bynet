# Kubernetes part



## My Kebernetes cluster has 5 files:
* ConfigMap.yaml
* deployment.yaml
* namespace.yaml
* service.yaml
* secret.yaml

But i can push on public repo only 4 files, without my secret. But i attached `secret.yaml.template` for use rename the file to `secret.yaml` and 


---
### **ConfigMap.yaml**
This file used to store non-confidential data in key-value pairs. Pods can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume.
 
### **deployment.yaml**
A Deployment provides declarative updates for Pods and ReplicaSets.

You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.


### **namespace.yaml**
This file need for created envinroment it's mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced objects (e.g. Deployments, Services, etc) and not for cluster-wide objects (e.g. StorageClass, Nodes, PersistentVolumes, etc).

### **service.yaml**
The service is used to describe the network interaction between pods and programs. An abstract way to expose an application running on a set of Pods as a network service.

### **secret.yaml**
This file that contains a small amount of sensitive data such as a password, a token, or a key. Such information might otherwise be put in a Pod specification or in a container image. Using a Secret means that you don't need to include confidential data in your application code.


---
## Kubernetes Cluster
First step: u need run your Kubernetes Cluster. I used minikube:

```bash
moonlight:~$ 
moonlight:~$ minikube start

✨  Using the vmware driver based on existing profile
...
👍  Starting control plane node minikube in cluster minikube
...
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
moonlight:~$ 
```

``` bash
moonlight:~$ minikube status
    minikube
    type: Control Plane
    host: Running
    kubelet: Running
    apiserver: Running
    kubeconfig: Configured
moonlight:~$ 
```
### Now need start applications into our Cluster
``` bash
moonlight:~$ cd Kubernetes
moonlight:~$ ls -l
  -rw-r--r--  1 moonlight  staff   341 Sep 19 23:01 ConfigMap.yaml
  -rw-r--r--  1 moonlight  staff  6568 Sep 22 17:11 Readme.md
  -rw-r--r--  1 moonlight  staff  5791 Sep 19 23:49 deployment.yaml
  -rw-r--r--  1 moonlight  staff   207 Sep 20 08:35 namespace.yaml
  -rw-r--r--  1 moonlight  staff   244 Sep 22 14:08 secret.yaml
  -rw-r--r--  1 moonlight  staff   277 Sep 20 14:23 secret.yaml.template
  -rw-r--r--  1 moonlight  staff   594 Sep 19 21:40 service.yaml
moonlight:~$ #---
moonlight:~$ kubectl apply -f . 
moonlight:~$ # OR
moonlight:~$ kubectl apply -f ConfigMap.yaml
moonlight:~$ kubectl apply -f deployment.yaml
moonlight:~$ kubectl apply -f namespace.yaml
moonlight:~$ kubectl apply -f secret.yaml
moonlight:~$ kubectl apply -f service.yaml
moonlight:~$ #---
  configmap/backend-configmap created
  deployment.apps/backend-deployment created
  deployment.apps/frontend-deployment created
  deployment.apps/database-deployment created
  namespace/bynet created
  secret/backend-secret created
  service/backend-service created
  service/frontend-service created
  service/database-service created
moonlight:~$ 
```
Check our running pods. (-nbynet - "-n" set the namespace, "bynet" - name in the Namespace)
``` bash
moonlight:~$ kubectl get -nbynet pod
NAME                                   READY   STATUS    RESTARTS   AGE
backend-deployment-5f97df49d7-w6b2m    1/1     Running   0          4m36s
database-deployment-6cc7dc48b7-gxmvs   1/1     Running   0          4m36s
frontend-deployment-55646d5688-8kf62   1/1     Running   0          4m36s
```
```bash
moonlight:~$ minikube -nbynet service frontend-service
|-----------|------------------|-------------|----------------------------|
| NAMESPACE |       NAME       | TARGET PORT |            URL             |
|-----------|------------------|-------------|----------------------------|
| bynet     | frontend-service |          80 | http://URL_YOUR_KUBE:31001 |
|-----------|------------------|-------------|----------------------------|
🎉  Opening service bynet/frontend-service in default browser...

```
After this message, the browser will open on the desired page!

---

Next step:
### Stopping Cluster
Similarly to launching, we use the following commands

``` bash
moonlight:~$ #---
moonlight:~$ kubectl delete -f . 
moonlight:~$ # OR
moonlight:~$ kubectl delete -f ConfigMap.yaml
moonlight:~$ kubectl delete -f deployment.yaml
moonlight:~$ kubectl delete -f namespace.yaml # This can take a very long time (don't recomend!)
moonlight:~$ kubectl delete -f secret.yaml
moonlight:~$ kubectl delete -f service.yaml
moonlight:~$ #---
  configmap "backend-configmap" deleted
  deployment.apps "backend-deployment" deleted
  deployment.apps "frontend-deployment" deleted
  deployment.apps "database-deployment" deleted
  namespace "bynet" deleted
  secret "backend-secret" deleted
  service "backend-service" deleted
  service "frontend-service" deleted
  service "database-service" deleted
moonlight:~$ 
```
Check our running pods.
``` bash
moonlight:~$ kubectl get -nbynet pod
NAME                                   READY   STATUS    RESTARTS   AGE
```
Perfectly! We can stop our Cluster
```bash
moonlight:~$ minikube stop
✋  Stopping node "minikube"  ...
🛑  1 node stopped.
moonlight:~$ 
```
