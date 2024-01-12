
# Face Authentication System

Deep Authenticator is an innovative API-driven authentication system I engineered to address the pressing need for heightened security in restricted areas.
## Problem statement
The project was conceived to resolve the inadequacies in conventional access control systems, particularly in environments demanding stringent security measures. Traditional authentication methods often fall short in high-security settings, necessitating an innovative solution capable of providing reliable access control without compromising on speed or accuracy.

## Solution
## Project Archietecture
The architecture revolves around a well-structured system with distinct routes for user registration, login, and real-time face detection. FastAPI serves as the backbone, ensuring seamless interactions, while MongoDB efficiently stores and retrieves user data and embeddings for comparison during authentication processes.

<img width="844" alt="image" src="https://user-images.githubusercontent.com/57321948/195135349-9888d9ea-af5d-4ee2-8aa4-1e57342add05.png">

## workflow
```
User Interface
    |
FastAPI (API endpoints)
    |
MongoDB (User Collection, Embedding Collection)
    |
Pre-Trained Models:
    - MTCNN (Face Detection)
    - FaceNet (Embedding Generation)
    |
Authentication Process:
    - User Registration Route
        - User details stored in User Collection
        - Proceeds to Registration Embedding Route
    - Registration Embedding Route
        - Face detection using MTCNN
        - Embedding generation using FaceNet
        - Embeddings stored in Embedding Collection
    - Login Route
        - User authentication (email/password)
        - Retrieves user ID from MongoDB
        - Proceeds to Authentication Route
    - Authentication Route
        - Real-time face detection using MTCNN
        - Embedding generation using FaceNet
        - Cosine similarity comparison for authentication
```

## Run the Application
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need Azure account to access the service like ACS and App services.

### Step 1-: Clone the Repository
```bash
git clone https://github.com/NeHa77A/DEEP-AUTHENTICATOR.git
```

### Step 2-: Creat conda environment
```bash
conda create -p ./venv python=3.8.13 -y
```

### Step 3-: Activate Conda environment
```bash
conda activate venv/
```

### Step 4-: Install requirements
```bash
pip install -r requirements.txt
```

### Step 5-: Export the environment variable
```
export SECRET_KEY=<SECRET_KEY>
export ALGORITHM=<ALGORITHM>
export MONGODB_URL_KEY=<MONGODB_URL_KEY>
export DATABASE_NAME=<DATABASE_NAME>
export USER_COLLECTION_NAME=<USER_COLLECTION_NAME>
export EMBEDDING_COLLECTION_NAME=<EMBEDDING_COLLECTION_NAME>
```

### Step 6-: Run the project
```bash
uvicorn app:app
```

### Build the Docker Image
```
docker build -t face_authentication .
```

### Run the Docker Image

```
docker run -p 8000:8000 face_authentication
```
### upload on Docker hub
```
docker tag face_authentictor:latest nehavish/face_authentication:v1.2
```
```
docker login
```
```
docker push nehavish/face_authentication:tag
```
### to pull docker image
you can check the docker hub repo

https://hub.docker.com/r/nehavish/face_authentication

or you can pull the docker image from the docker hub with following command
```
docker pull nehavish/face_authentication
```
![](https://raw.githubusercontent.com/NeHa77A/DEEP-AUTHENTICATOR/main/output/docker%20hub.png)
