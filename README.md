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

## Setup Instructions

1. Start Minikube:
```bash
minikube start
```

2. Enable required addons:
```bash
minikube addons enable ingress
```

3. Build the Docker image:
```bash
eval $(minikube docker-env)
docker build -t flask-app:latest ./app/
```

4. Apply Kubernetes manifests:
```bash
kubectl apply -f manifests/secret/postgres-secret.yaml
kubectl apply -f manifests/configmap/postgres-configmap.yaml
kubectl apply -f manifests/deployment/postgres-pv.yaml
kubectl apply -f manifests/deployment/postgres-deployment.yaml
kubectl apply -f manifests/service/postgres-service.yaml
kubectl apply -f manifests/deployment/flask-deployment.yaml
kubectl apply -f manifests/service/flask-service.yaml
```

## Accessing the Application

Get the service URL:
```bash
minikube service flask-service --url
```

The application will be available at the provided URL.

## Health Check

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
```

## Documentation

Detailed documentation and test results can be found in the `submission/` directory. 