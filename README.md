# Under Construction! You've been warned ;)
# ETL-using-k8s
A simple example of an ETL job using KinD (kubernetes in docker).
Requests data from the weather API and sends to a mysql table. 
Eventually, this app will implement airflow and spark to do this in a more scalable way.

# Requirements
- KinD (Kubernetes in Docker)
- Docker

# Demo 
1. (if running locally) Setup kind cluster 
`kind create cluster --name etl-using-k8s`
2. Pull image
`docker pull nicoxdockerhub/etl-app:latest`
3. Run deployment 
`kubectl apply -f manifests/deployment.yml`

### TODO
3. write a mysql pod manifest (https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/)
4. manually interact with mysql pod, create a table
5. update etl-app with mysql connection creds
6. test mysql app again
