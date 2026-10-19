# Exercise 4: Docker Networking with Multiple Containers

## Objective

Understand Docker networking concepts and configure a multi-container application using a custom bridge network.

## Steps of Execution

Create a custom bridge network to allow communication between the Flask, MySQL, and Redis containers.

### 1. Create a Custom Bridge Network

```bash
docker network create --driver bridge my-bridge-net
```

### 2. Verify the Network

```bash
docker network ls
```

### 3. Inspect the Network

```bash
docker network inspect my-bridge-net
```

## Create the Flask Application

### 4. Create `app.py`

Create an `app.py` file with the following code:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/about', methods=['GET'])
def about():
    return jsonify({
        "name": "Simple REST API",
        "version": "1.0",
        "description": "This is a simple REST API built with Flask."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

### 5. Create `requirements.txt`

```text
Flask==2.0.1
Werkzeug==2.0.3
```

### 6. Create the `Dockerfile`

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]
```

### 7. Build the Flask Docker Image

```bash
docker build -t flask-api .
```

## Launch the Containers

### 8. Start the MySQL Container

```bash
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=LabPass123! mysql:8.0
```

### 9. Start the Redis Container

```bash
docker run -d --name redis --network my-bridge-net redis:latest
```

### 10. Start the Flask Container

```bash
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api
```

### 11. Verify the Running Containers

```bash
docker ps
```

## Test the Flask Application

### 12. Open the API Endpoint

Open the following URL in a browser:

```text
http://localhost:5001/about
```

The application returns information about the REST API in JSON format:

```json
{
  "name": "Simple REST API",
  "version": "1.0",
  "description": "This is a simple REST API built with Flask."
}
```

## Test Connectivity Between Containers

### 13. Enter the Flask Container

```bash
docker exec -it flask sh
```

### 14. Check the IP Addresses of MySQL and Redis

Run the following command inside the Flask container:

```bash
python -c "import socket; print(socket.gethostbyname('mysql')); print(socket.gethostbyname('redis'))"
```

### 15. Test Connectivity to MySQL

```bash
python -c "import socket; s=socket.create_connection(('mysql',3306),5); print('MySQL connection successful'); s.close()"
```

```text
MySQL connection successful
```

### 16. Test Connectivity to Redis

```bash
python -c "import socket; s=socket.create_connection(('redis',6379),5); print('Redis connection successful'); s.close()"
```

```text
Redis connection successful
```

### 17. Exit the Flask Container

```bash
exit
```

## Clean Up

### 18. Stop the Containers

```bash
docker stop flask mysql redis
```

### 19. Remove the Containers

```bash
docker rm flask mysql redis
```

### 20. Remove the Custom Bridge Network

```bash
docker network rm my-bridge-net
```

## Conclusion

Docker networking was demonstrated by connecting Flask, MySQL, and Redis containers to a custom bridge network. Container name resolution and connectivity to the MySQL and Redis service ports were verified successfully.
