Exercise 10

Minikube Setup

Run the following command to setup minikube :



minikube start --nodes 3 -p devops-multinode --force

Run the following command to setup minikube with multiple node :



minikube -p devops-multinode addons enable registry

Application setup

Create and have the code in the product_catalog.py and shopping_cart.py

Create Dockerfiles to containerize the above applications named as Dockerfile.product and Dockerfile.shopping

Build the docker images using the following commands :

docker build -t product-catalog:latest -f Dockerfile.product .

docker build -t shopping-cart:latest -f Dockerfile.shopping .

Load the built images into the registry using the following commands :

minikube -p devops-multinode image load product-catalog:latest

minikube -p devops-multinode image load shopping-cart:latest

Verify that the images are loaded using the following command :



minikube -p devops-multinode ssh -- docker images

Deploy the applications on minikube

Create the deployement files product_catalog_deployment.yaml and shopping_cart_deployment.yaml



Create namespace using the following command



kubectl create namespace devops-exercise

And run the following commands to apply the configurations :



kubectl apply -f product_catalog_deployment.yaml

kubectl apply -f shopping_cart_deployment.yaml

Expose the services

Create the service files product_catalog_service.yaml and shopping_cart_service.yaml



And run the following commands to apply the services :



kubectl apply -f product_catalog_service.yaml

kubectl apply -f shopping_cart_service.yaml

Access product service using the following command :

minikube -p devops-multinode service product-catalog-service





## Screenshots and Evidence

### Screenshot 2026-10-19 050838

![ Screenshot 2026-10-19 050838 ](./Screenshot%202026-10-19%20050838.png)

### Screenshot 2026-10-19 050932

![ Screenshot 2026-10-19 050932 ](./Screenshot%202026-10-19%20050932.png)

### Screenshot 2026-10-19 051030

![ Screenshot 2026-10-19 051030 ](./Screenshot%202026-10-19%20051030.png)

### Screenshot 2026-10-19 052218

![ Screenshot 2026-10-19 052218 ](./Screenshot%202026-10-19%20052218.png)


