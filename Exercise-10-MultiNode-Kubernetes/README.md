# Exercise 10: Multi-Node Kubernetes Deployment

## Minikube Setup

### 1. Start Minikube with Three Nodes

Run the following command to set up Minikube with three nodes:

```bash
minikube start --nodes 3 -p devops-multinode --force
```

### 2. Enable the Registry Add-on

Run the following command to enable the registry add-on for the multi-node Minikube cluster:

```bash
minikube -p devops-multinode addons enable registry
```

## Application Setup

### 3. Create the Application Files

Create the following Python application files:

- `product_catalog.py`
- `shopping_cart.py`

### 4. Create Dockerfiles

Create Dockerfiles to containerize the applications:

- `Dockerfile.product`
- `Dockerfile.shopping`

## Build the Docker Images

### 5. Build the Product Catalog Image

```bash
docker build -t product-catalog:latest -f Dockerfile.product .
```

### 6. Build the Shopping Cart Image

```bash
docker build -t shopping-cart:latest -f Dockerfile.shopping .
```

## Load the Images into Minikube

### 7. Load the Product Catalog Image

```bash
minikube -p devops-multinode image load product-catalog:latest
```

### 8. Load the Shopping Cart Image

```bash
minikube -p devops-multinode image load shopping-cart:latest
```

### 9. Verify the Loaded Images

Verify that the images are loaded using the following command:

```bash
minikube -p devops-multinode ssh -- docker images
```

## Deploy the Applications on Minikube

### 10. Create Deployment Files

Create the following deployment configuration files:

- `product_catalog_deployment.yaml`
- `shopping_cart_deployment.yaml`

### 11. Create the Namespace

Create the namespace using the following command:

```bash
kubectl create namespace devops-exercise
```

### 12. Apply the Deployment Configurations

Apply the product catalog deployment:

```bash
kubectl apply -f product_catalog_deployment.yaml
```

Apply the shopping cart deployment:

```bash
kubectl apply -f shopping_cart_deployment.yaml
```

## Expose the Services

### 13. Create Service Files

Create the following service configuration files:

- `product_catalog_service.yaml`
- `shopping_cart_service.yaml`

### 14. Apply the Service Configurations

Apply the product catalog service:

```bash
kubectl apply -f product_catalog_service.yaml
```

Apply the shopping cart service:

```bash
kubectl apply -f shopping_cart_service.yaml
```

## Access the Product Service

### 15. Access the Product Catalog Service

Run the following command to access the product catalog service:

```bash
minikube -p devops-multinode service product-catalog-service
```

## Screenshots

### 1. Screenshot 1

![Exercise 10 Screenshot 1](./Screenshot%202026-10-19%20050838.png)

---

### 2. Screenshot 2

![Exercise 10 Screenshot 2](./Screenshot%202026-10-19%20050932.png)

---

### 3. Screenshot 3

![Exercise 10 Screenshot 3](./Screenshot%202026-10-19%20051030.png)

---

### 4. Screenshot 4

![Exercise 10 Screenshot 4](./Screenshot%202026-10-19%20052218.png)

## Conclusion

In this exercise, a three-node Minikube cluster was configured. The product catalog and shopping cart applications were containerized, their Docker images were loaded into Minikube, and deployment and service configuration files were applied to Kubernetes. The product catalog service was accessed using Minikube.
