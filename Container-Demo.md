## Tools/Utilites Required:
    - Git
    - Docker Desktop
    - Python


### Steps to Containerize your App

1. Clone the Repo

        git clone https://github.com/poladinesh/MLOpsDemo.git

2. Switch to src-container folder

        cd src-container

3. Install & Activate Python Virtual Environment

    For Mac/Linux:

        python -m venv .
        source ./bin/activate

    For Windows:

            python -m venv .
            .\Scripts\activate

4. Inspect & Run the Code

        pip install -r requirements.txt
        uvicorn main:app --reload


5. Containerize / Generate Dockerfile

        docker init

6. Build the Container Image
        
        docker build -t mlops-demo:v1 .

        docker buildx build --platform linux/amd64 -t mlops-demo:v2 .

>[!Important]
Please look at docs here [Multiplatform build](https://docs.docker.com/build/building/multi-platform/#build-multi-platform-images) if you are building on ARM-Based Laptops/Machines

>[!Caution] : Exit code 255 - architecture mismatch:
    If the Docker image is built for a different architecture than the ECS cluster's underlying instances (e.g., x86_64 image on an ARM64 instance), it can lead to an "exec format error" and a 255 exit code.

7. Tag & Push the Container Image with Container Registry Name (here, we use docker hub)

        docker image tag mlops-demo:v2 poladinesh/mlops-demo:v2
        docker push poladinesh/mlops-demo:v2

Requires `docker login` # if not already logged in - requires dockerhub login

8. Verify the latest container image in Dockerhub

9. Remove local Container Images and pull from Dockerhub

        docker images | grep -i mlops
        docker rmi mlops-demo:v2
        docker pull poladinesh/mlops-demo:v2

10. Run the downloaded container image from Dockerhub

        docker run -p 8000:8000 mlops-demo:v2

11. Access the app at http://localhost:8000 or http://localhost:8000/docs

12. Now we can deploy image anywhere we want, for example we can deploy this on a ECS Cluster

[Placeholder for Container Deployment on a AWS ECS Cluster]

>[!Note]
    exit code 255 - architecture mismatch:
    If the Docker image is built for a different architecture than the ECS cluster's underlying instances (e.g., x86_64 image on an ARM64 instance), it can lead to an "exec format error" and a 255 exit code.