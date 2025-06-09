# Kubernetes Flask PostgreSQL Deployment - Task List

## Project Overview
Deploy a Flask-based web application with a PostgreSQL database on a Minikube-managed Kubernetes cluster. Complete all tasks in order and submit required documentation.

## Prerequisites Checklist
- [ ] Docker installed on your system
- [ ] Minikube installed and configured
- [ ] kubectl command-line tool installed
- [ ] Basic knowledge of Kubernetes concepts
- [ ] Git repository cloned and ready

## Project Structure Setup
Create the following directory structure:
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

## Task 1: Environment Setup
- [ ] Start Minikube cluster
  ```bash
  minikube start
  ```
- [ ] Verify cluster is running
  ```bash
  kubectl cluster-info
  ```
- [ ] Enable necessary addons
  ```bash
  minikube addons enable ingress
  ```
- [ ] Verify kubectl can connect to cluster
  ```bash
  kubectl get nodes
  ```

## Task 2: Create Flask Application
- [ ] Create `app/app.py` with Flask application code
- [ ] Create `app/requirements.txt` with Python dependencies
- [ ] Create `app/Dockerfile` for containerization
- [ ] Test Flask app locally (optional)
- [ ] Build Docker image
  ```bash
  eval $(minikube docker-env)
  docker build -t flask-app:latest ./app/
  ```
- [ ] Verify image is built
  ```bash
  docker images | grep flask-app
  ```

## Task 3: Create Kubernetes Manifests for PostgreSQL

### 3.1: Create PostgreSQL Secret
- [ ] Create `manifests/secret/postgres-secret.yaml`
- [ ] Include base64 encoded database credentials
- [ ] Apply the secret
  ```bash
  kubectl apply -f manifests/secret/postgres-secret.yaml
  ```
- [ ] Verify secret creation
  ```bash
  kubectl get secrets
  ```

### 3.2: Create PostgreSQL ConfigMap
- [ ] Create `manifests/configmap/postgres-configmap.yaml`
- [ ] Include database configuration (non-sensitive data)
- [ ] Apply the configmap
  ```bash
  kubectl apply -f manifests/configmap/postgres-configmap.yaml
  ```
- [ ] Verify configmap creation
  ```bash
  kubectl get configmaps
  ```

### 3.3: Create PostgreSQL Deployment
- [ ] Create `manifests/deployment/postgres-deployment.yaml`
- [ ] Configure persistent volume claim
- [ ] Set environment variables from secret and configmap
- [ ] Apply the deployment
  ```bash
  kubectl apply -f manifests/deployment/postgres-deployment.yaml
  ```
- [ ] Verify deployment status
  ```bash
  kubectl get deployments
  kubectl get pods -l app=postgres
  ```

### 3.4: Create PostgreSQL Service
- [ ] Create `manifests/service/postgres-service.yaml`
- [ ] Configure ClusterIP service for internal access
- [ ] Apply the service
  ```bash
  kubectl apply -f manifests/service/postgres-service.yaml
  ```
- [ ] Verify service creation
  ```bash
  kubectl get services
  ```

## Task 4: Create Kubernetes Manifests for Flask Application

### 4.1: Create Flask Deployment
- [ ] Create `manifests/deployment/flask-deployment.yaml`
- [ ] Configure deployment with image reference
- [ ] Set environment variables for database connection
- [ ] Configure readiness and liveness probes
- [ ] Apply the deployment
  ```bash
  kubectl apply -f manifests/deployment/flask-deployment.yaml
  ```
- [ ] Verify deployment status
  ```bash
  kubectl get deployments
  kubectl get pods -l app=flask-app
  ```

### 4.2: Create Flask Service
- [ ] Create `manifests/service/flask-service.yaml`
- [ ] Configure NodePort or LoadBalancer service
- [ ] Apply the service
  ```bash
  kubectl apply -f manifests/service/flask-service.yaml
  ```
- [ ] Verify service creation
  ```bash
  kubectl get services
  ```

## Task 5: Testing & Verification

### 5.1: Basic Connectivity Tests
- [ ] Check all pods are running
  ```bash
  kubectl get pods
  ```
- [ ] Check all services are available
  ```bash
  kubectl get services
  ```
- [ ] View deployment status
  ```bash
  kubectl get deployments
  ```

### 5.2: Application Access Tests
- [ ] Get Flask service URL
  ```bash
  minikube service flask-service --url
  ```
- [ ] Access Flask application via web browser
- [ ] Verify database connectivity through application
- [ ] Test application functionality

### 5.3: Log Verification
- [ ] Check Flask application logs
  ```bash
  kubectl logs -l app=flask-app
  ```
- [ ] Check PostgreSQL logs
  ```bash
  kubectl logs -l app=postgres
  ```
- [ ] Verify no error messages in logs

## Task 6: Scaling Tests

### 6.1: Scale Up Test
- [ ] Record current replica count
  ```bash
  kubectl get deployment flask-deployment
  ```
- [ ] Scale up to 3 replicas
  ```bash
  kubectl scale deployment flask-deployment --replicas=3
  ```
- [ ] Verify scaling completed
  ```bash
  kubectl get pods -l app=flask-app
  ```
- [ ] Test load distribution across replicas

### 6.2: Scale Down Test
- [ ] Scale down to 1 replica
  ```bash
  kubectl scale deployment flask-deployment --replicas=1
  ```
- [ ] Verify scaling completed
  ```bash
  kubectl get pods -l app=flask-app
  ```
- [ ] Verify application still accessible

### 6.3: Replica Configuration Investigation
- [ ] Examine deployment YAML for replica settings
- [ ] Document minimum replica count
- [ ] Document maximum replica count (if HPA configured)
- [ ] Test resource limits and requests

## Task 7: Documentation & Screenshots

### 7.1: Create Submission Folder
- [ ] Create `submission/` directory
- [ ] Organize all required documentation

### 7.2: Required Screenshots
- [ ] Take snapshot of internal deployment
  ```bash
  kubectl get all -o wide
  ```
- [ ] Screenshot of `kubectl get all` output
- [ ] Screenshots of scaling operations (before/after)
- [ ] Screenshot of pods during scaling process

### 7.3: Create Documentation Files
- [ ] Create `submission/scaling-test-results.md`
- [ ] Document scaling up process and results
- [ ] Document scaling down process and results
- [ ] Create `submission/replica-investigation.md`
- [ ] Document minimum replica configuration
- [ ] Document maximum replica configuration
- [ ] Explain replica count implications

## Task 8: Final Verification & Cleanup

### 8.1: Final System Check
- [ ] Verify all manifests are applied correctly
- [ ] Test complete application workflow
- [ ] Verify persistent data survives pod restarts
- [ ] Check resource utilization
  ```bash
  kubectl top pods
  kubectl top nodes
  ```

### 8.2: Repository Finalization
- [ ] Commit all code and manifests
- [ ] Add comprehensive README.md
- [ ] Ensure all files are in correct directory structure
- [ ] Push to GitHub repository

### 8.3: Submission Checklist
- [ ] All YAML manifests created and working
- [ ] Flask application containerized and deployed
- [ ] PostgreSQL database deployed with persistent storage
- [ ] Services configured for proper communication
- [ ] Scaling tests completed and documented
- [ ] Screenshots captured and saved in submission folder
- [ ] Documentation files completed
- [ ] Repository structure matches requirements

## Troubleshooting Checklist
If you encounter issues:
- [ ] Check pod status: `kubectl describe pod <pod-name>`
- [ ] Review logs: `kubectl logs <pod-name>`
- [ ] Verify service endpoints: `kubectl get endpoints`
- [ ] Check persistent volumes: `kubectl get pv,pvc`
- [ ] Validate YAML syntax: `kubectl apply --dry-run=client -f <file>`
- [ ] Test connectivity: `kubectl exec -it <pod> -- /bin/bash`

## Learning Outcomes Verification
Upon completion, you should be able to:
- [ ] Create and manage Kubernetes deployments
- [ ] Configure services for inter-pod communication
- [ ] Use ConfigMaps and Secrets for configuration management
- [ ] Implement persistent storage for databases
- [ ] Scale applications horizontally
- [ ] Debug Kubernetes deployments
- [ ] Document and present Kubernetes solutions