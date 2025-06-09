# Kubernetes Flask PostgreSQL Deployment

This project demonstrates the deployment of a Flask application with PostgreSQL database on Kubernetes using Minikube.

## Project Structure
```
k8s-flask-app/
├── manifests/
│   ├── deployment/
│   ├── service/
│   ├── configmap/
│   └── secret/
├── app/
├── submission/
└── README.md
```

## Prerequisites
- Docker
- Minikube
- kubectl
- Python 3.11+

## Quick Start Guide

### 1. Start Minikube
```bash
minikube start
```

### 2. Enable Required Addons
```bash
minikube addons enable ingress
```

### 3. Build Docker Image
```bash
eval $(minikube docker-env)
docker build -t flask-app:latest ./app/
```

### 4. Deploy Application
Apply the Kubernetes manifests in the correct order:

```bash
# Create secrets and configmaps
kubectl apply -f manifests/secret/postgres-secret.yaml
kubectl apply -f manifests/configmap/postgres-configmap.yaml

# Create persistent volume and deployment
kubectl apply -f manifests/deployment/postgres-pv.yaml
kubectl apply -f manifests/deployment/postgres-deployment.yaml

# Create services
kubectl apply -f manifests/service/postgres-service.yaml
kubectl apply -f manifests/deployment/flask-deployment.yaml
kubectl apply -f manifests/service/flask-service.yaml
```

### 5. Verify Deployment
```bash
kubectl get all
```

### 6. Access the Application
Get the service URL:
```bash
minikube service flask-service --url
```

Test the application health:
```bash
curl http://<service-url>/health
```

## Scaling

Scale the Flask application:
```bash
kubectl scale deployment flask-deployment --replicas=3
```

## Monitoring

View all resources:
```bash
kubectl get all
```

View logs:
```bash
kubectl logs -l app=flask-app
kubectl logs -l app=postgres
```

## Cleanup

To clean up the deployment:
```bash
kubectl delete -f manifests/
minikube stop
```

## Documentation

Detailed documentation and test results can be found in the `submission/` directory. 