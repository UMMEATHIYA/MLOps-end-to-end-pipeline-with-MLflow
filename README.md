# MLOps-end-to-end-pipeline-with-MLflow

# End-to-end-Machine-Learning-Project-with-MLflow


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components 
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/UMMEATHIYA/MLOps-end-to-end-pipeline-with-MLflow.git
```
### STEP 01- Create a conda environment after opening the repository
```
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/Scripts/activate  # For Windows Git Bash
# source .venv/bin/activate    # For Mac/Linux

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Start MLflow tracking server (run in a new terminal if needed)
mlflow ui --backend-store-uri sqlite:///mlruns.db --host 127.0.0.1 --port 5000

# Run the ML pipeline
python main.py

# Open MLflow UI
# Open manually: http://127.0.0.1:5000
```

## Sample Output
---
```
(.venv) PS C:\Users\ummea\MLOps-end-to-end-pipeline-with-MLflow> python .\main.py
[2025-07-21 03:12:17,730: INFO: main: >>>>>> stage Data Ingestion stage started <<<<<<]
[2025-07-21 03:12:17,731: INFO: common: yaml file: config\config.yaml loaded successfully]
[2025-07-21 03:12:17,731: INFO: common: yaml file: params.yaml loaded successfully]
[2025-07-21 03:12:17,731: INFO: common: yaml file: schema.yaml loaded successfully]
[2025-07-21 03:12:17,731: INFO: common: created directory at: artifacts]
[2025-07-21 03:12:17,737: INFO: common: created directory at: artifacts/data_ingestion]
[2025-07-21 03:12:17,738: INFO: data_ingestion: File already exists of size: ~ 23 KB]
[2025-07-21 03:12:17,742: INFO: main: >>>>>> stage Data Ingestion stage completed <<<<<<

x==========x]
[2025-07-21 03:12:17,742: INFO: main: >>>>>> stage Data Validation stage started <<<<<<]
[2025-07-21 03:12:17,744: INFO: common: yaml file: config\config.yaml loaded successfully]
[2025-07-21 03:12:17,746: INFO: common: yaml file: params.yaml loaded successfully]
[2025-07-21 03:12:17,748: INFO: common: yaml file: schema.yaml loaded successfully]
[2025-07-21 03:12:17,749: INFO: common: created directory at: artifacts]
[2025-07-21 03:12:17,749: INFO: common: created directory at: artifacts/data_validation]
[2025-07-21 03:12:17,777: INFO: main: >>>>>> stage Data Validation stage completed <<<<<<

x==========x]
[2025-07-21 03:12:17,777: INFO: main: >>>>>> stage Data Transformation stage started <<<<<<]
[2025-07-21 03:12:17,789: INFO: common: yaml file: config\config.yaml loaded successfully]
[2025-07-21 03:12:17,791: INFO: common: yaml file: params.yaml loaded successfully]
[2025-07-21 03:12:17,793: INFO: common: yaml file: schema.yaml loaded successfully]
[2025-07-21 03:12:17,794: INFO: common: created directory at: artifacts]
[2025-07-21 03:12:17,794: INFO: common: created directory at: artifacts/data_transformation]
[2025-07-21 03:12:17,815: INFO: data_transformation: Splited data into training and test sets]        
[2025-07-21 03:12:17,815: INFO: data_transformation: (1199, 12)]
[2025-07-21 03:12:17,815: INFO: data_transformation: (400, 12)]
(1199, 12)
(400, 12)
[2025-07-21 03:12:17,815: INFO: main: >>>>>> stage Data Transformation stage completed <<<<<<

x==========x]
[2025-07-21 03:12:17,815: INFO: main: >>>>>> stage Model Trainer stage started <<<<<<]
[2025-07-21 03:12:17,818: INFO: common: yaml file: config\config.yaml loaded successfully]
[2025-07-21 03:12:17,818: INFO: common: yaml file: params.yaml loaded successfully]
[2025-07-21 03:12:17,822: INFO: common: yaml file: schema.yaml loaded successfully]
[2025-07-21 03:12:17,822: INFO: common: created directory at: artifacts]
[2025-07-21 03:12:17,826: INFO: common: created directory at: artifacts/model_trainer]
C:\Users\ummea\MLOps-end-to-end-pipeline-with-MLflow\.venv\Lib\site-packages\_distutils_hack\__init__.py:33: UserWarning: Setuptools is replacing distutils.
  warnings.warn("Setuptools is replacing distutils.")
[2025-07-21 03:12:25,136: INFO: model_trainer: Model trained and logged to MLflow. RMSE: 0.6790, R2: 0.2533]
[2025-07-21 03:12:25,157: INFO: main: >>>>>> stage Model Trainer stage completed <<<<<<

x==========x]
[2025-07-21 03:12:25,157: INFO: main: >>>>>> stage Model evaluation stage started <<<<<<]
[2025-07-21 03:12:25,161: INFO: common: yaml file: config\config.yaml loaded successfully]
[2025-07-21 03:12:25,163: INFO: common: yaml file: params.yaml loaded successfully]
[2025-07-21 03:12:25,165: INFO: common: yaml file: schema.yaml loaded successfully]
[2025-07-21 03:12:25,166: INFO: common: created directory at: artifacts]
[2025-07-21 03:12:25,166: INFO: common: created directory at: artifacts/model_evaluation]
[2025-07-21 03:12:25,217: INFO: common: json file saved at: artifacts\model_evaluation\metrics.json]  
[2025-07-21 03:12:28,989: INFO: main: >>>>>> stage Model evaluation stage completed <<<<<<

x==========x]
```
---
<img width="1907" height="867" alt="image" src="https://github.com/user-attachments/assets/fb57964f-53cd-447b-b885-f6131ab244bb" />


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=entbappy \
MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


 
