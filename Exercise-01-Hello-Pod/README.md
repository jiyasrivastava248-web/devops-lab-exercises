# Exercise 1: Deploy Nginx Using Minikube and Kubernetes

## Objective

To deploy an Nginx application in a local Kubernetes cluster using Minikube and expose it through a NodePort Service.

## Steps of Execution

### 1. Start the Minikube Cluster

```bash
minikube start --driver=docker
```

This starts a local Kubernetes cluster using Docker as the driver.

### 2. Create an Nginx Pod

```bash
kubectl run hello-k8s --image=nginx --port=80
```

This creates a Pod running the Nginx container.

### 3. Check the Pod Status

```bash
kubectl get pods
```

This command displays the Pod status and helps verify that the Nginx Pod is running.

### 4. Expose the Pod

```bash
kubectl expose pod hello-k8s --type=NodePort --port=80
```

This creates a NodePort Service to expose the Nginx application.

### 5. Access the Application

```bash
minikube service hello-k8s
```

This opens the Nginx service in a browser when the cluster and service are running correctly.

## Description

In this exercise, an Nginx container is deployed as a Pod in a local Kubernetes cluster using Minikube. The Pod is exposed using a NodePort Service, allowing the Nginx application to be accessed through a web browser.

## Screenshots

### 1. Minikube Cluster

![Minikube Cluster](./Screenshot%202026-10-01%20162708.png)

### 2. Nginx Pod

![Nginx Pod](./Screenshot%202026-10-01%20162733.png)

### 3. Nginx Service

![Nginx Service](./Screenshot%202026-10-01%20162745.png)

### 4. Application Verification

![Application Verification](./Screenshot%202026-10-01%20162753.png)

## Result

The Nginx application was deployed in Kubernetes using Minikube and exposed through a NodePort Service. The application was accessed through a web browser.
