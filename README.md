# Under Construction! You've been warned ;)
# ETL-using-k8s
A simple example of an ETL job using KinD (kubernetes in docker). Just for fun.

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
1. containerize etl-app
2. test etl app on k8s 
3. write a mysql pod manifest
4. test etl-app in k8s again
