Exercise 10

Minikube Setup

Run the following command to setup minikube :



minikube start --nodes 3 -p devops-multinode --force

Run the following command to setup minikube with multiple node :



minikube -p devops-multinode addons enable registry

Application setup

Create and have the code in the product\_catalog.py and shopping\_cart.py

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

Create the deployement files product\_catalog\_deployment.yaml and shopping\_cart\_deployment.yaml



Create namespace using the following command



kubectl create namespace devops-exercise

And run the following commands to apply the configurations :



kubectl apply -f product\_catalog\_deployment.yaml

kubectl apply -f shopping\_cart\_deployment.yaml

Expose the services

Create the service files product\_catalog\_service.yaml and shopping\_cart\_service.yaml



And run the following commands to apply the services :



kubectl apply -f product\_catalog\_service.yaml

kubectl apply -f shopping\_cart\_service.yaml

Access product service using the following command :

minikube -p devops-multinode service product-catalog-service



