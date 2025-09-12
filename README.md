# MLOpsDemo
This repository contains MLOPS Demo Code and Documentation
# MLOPS Module

## Introduction to MLOPS:

From the Demo: According to a Gartner & other research studies, close to 90% of models never make it to production i.e, Only 1 in 10 Machine Learning Models gets deployed to Production.

### Definition:
MLOPS is about efficiently deploying the models to solve real-world problems. It is the intersection of ML and Operations.

MLOPS aims to bridge the gap between development and deployment.

### Importance:

MLOPS provides a standard process/framework for the ML lifecycle to follow. It brings together disparate processes and tools into a unified workflow

MLOPS Benefits:
- Faster time to market
- Improved Productivity
- Efficient Model Deployment
- Reduce Risk of Manual Errors
- Consistency
- Scalability
- Compliance
- Fosters Collaboration

### Evolution from Devops to MLOPS:

MLOPS extends Devops practices to Machine Learning as traditional software development practices falls short due to the dynamic nature of ML Models.

Core Principles:
- Versioning
- Continuous Integration
- Continuous Delivery/Deployment
- Continuous Training
- Continuous Monitoring
- Reproducibility


### Key Similarities and Differences:

##### Similarities:
- Automation: In DevOps, automation often revolves around code deployment and infrastructure provisioning, while MLOps extends this automation to model training and deployment
- Collaboration: DevOps teams bring together developers and IT operations, while MLOps bridges the gap between data scientists and operations teams
- Continous Integration and Continous Delivery (CI-CD): CI/CD principles are fundamental to both DevOps and MLOps. They ensure that changes are tested and deployed systematically, reducing the risk of errors

##### Differences:
- Nature of Artifacts
- Testing and Data Quality
- Model Drift and Monitoring
- Continous Training
- Data Governance

### MLOPS Maturity Levels:
- Level 0: No Automation
- Level 1: Semi-Automation
- Level 2: Full Automation

References:
- [MLOPS Maturity Levels](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- [What is MLOPS ?](https://aws.amazon.com/what-is/mlops/)

## MLOPS Tools Overview:

### Kubeflow:

Kubeflow is an open-source platform designed to orchestrate machine learning workflows on Kubernetes, enabling scalable and reproducible ML operations.

Kubeflow Components:

![kubeflow-components](./images/kubeflow-components.png)

When to use:
- Working on Medium/Large Project to provide an end-to-end platform to ML Teams
- When working with Kubernetes based environments or any Cloud, On-Prem or Hybrid environments

Caution:
- Setup and operation require significant Kubernetes expertise and computing resources; 
- Documentation may be weak in some advanced or custom scenarios

- [kubeflow](https://www.kubeflow.org/)
- [kubeflow article](https://kodekloud.com/blog/running-ai-ml-workloads-on-kubernetes-using-kubeflow-a-beginners-guide/)
- [ChatGPT on Kubernetes](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)

### MLFlow:

MLFlow is an open-source framework for managing the complete machine learning lifecycle, helping teams track experiments, package code, and streamline deployment.

MLFLow Components:

- Tracking: Tracking is an API and UI for logging parameters, code versions, metrics, and artifacts
- Projects: Projects are a standard format for packaging reusable data science code
- Models: Models offer a convention for packaging machine learning models in multiple flavors, and a variety of tools to help you deploy them
- Registry: Registry offers a centralized model store, set of APIs, and UI, to collaboratively manage the full lifecycle of an MLflow Model, also show model lineage (which experiment and run produced the model), model versioning and promotion

Note: MLFlow is also integrated in Sagemaker, see below [References](#References)

- [MLFlow Quickstart](https://mlflow.org/docs/latest/ml/tracking/quickstart/)
- [MLFlow Components](https://www.mlflow.org/docs/2.1.1/concepts.html)
- [MLFlow Experiment Comparison](https://mlflow.org/docs/2.21.3/getting-started/quickstart-2/)

When to use:
- Can be used on any Project scale ranging from personal to Production grade
- Teams seeking framework-agnostic and lightweight ML lifecycle management

Caution:
- Lacks native Pipeline Orchestration and built-in Kubernetes integration compared to Kubeflow Setup. Also, focus is more experiment-centric rather than full workflow automation
- May not be suitable for teams looking for Enterprise-Grade model deployment, monitoring and cloud-based scaling

### AWS Sagemaker:

AWS Sagemaker is a fully managed, end-to-end platform that enables model building, training, deployment, and monitoring at scale in the AWS cloud

Key Features:
- One-stop environment: Integrates data preparation, feature engineering, model training, tuning, hosting, and monitoring within a unified AWS platform.
- Managed environments: Provides pre-built Jupyter/Studio environments, customizable containers, and infrastructure automation.
- Integrated MLOps: Built-in tools for CI/CD(Sagemaker Pipelines), automation, audit trails, and lineage for all ML artifacts and actions
    - Model Registry helps to Store, catalog, and manage model versions with approval workflows, lineage for all ML artifacts and actions
    - Sagemaker Pipelines provides Visual and Code Driven Pipeline creation enabling swift automation
    - Built-in MLFlow Integration

When to use:
- Preference for a fully managed, end-to-end ML Platform with built-in tools
- For Teams seeking minimal infrastructure management, user-friendly visual environments and enterprise support

Caution:
- Provider/Vendor Lock-In with AWS
- Learning Curve might be steep depending on the features selected

Demo - Example Notebook:
https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/linear_learner_mnist/linear_learner_mnist.ipynb

#### AWS Sagemaker Jargon:

Sagemaker Vs Bedrock: While Sagemaker is focussed more on traditional ML Models, Bedrock is focussed towards more GenAI and Large Language Models(LLMs)

- Studio: Comprehensive Web-Based IDE for Machine Learning end-to-end Development

- Notebooks: Stand-Alone instances of Jupyter Notebooks

- Canvas: AWS No-Code Platform for ML along with AI-powered assistance from Amazon Q Developer

- Domain: Covers all the above features in a single place. A domain is an environment for your team to access SageMaker resources. A domain consists of a list of authorized users and users within a domain can share notebook files and other artifacts with each other. One account can have either one or multiple domains

- HyperPod Clusters: SageMaker HyperPod clusters are purpose-built, scalable, and resilient clusters designed for accelerating large-scale distributed training and deployment of complex machine learning models like LLMs, diffusion models, and other foundation models

Other Tools:

Google Vertex AI, Azure Machine Learning, DVC for Data Version Control

##### References:
- [AWS Sagemaker Studio](https://aws.amazon.com/sagemaker/ai/studio/)
- [AWS Sagemaker Canvas](https://aws.amazon.com/sagemaker/ai/canvas/)
- [Studio Vs Notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-comparison.html)
- [Sagemaker Domain](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-onboard.html)
- [MLFlow Tracking with Sagemaker](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/sagemaker-experiments.xml.html)

### Demo Time:

[Placeholder for SageMaker Demo]

[Placeholder for SageMaker MLFlow]

## Deployment Methods:

Machine Learning Code can be deployed using the following methods:

1) Containers:
    - can be deployed to Sagemaker
    - can be deployed to any container based platform such as 
        - AWS: ECS, EKS, Beanstalk, Lightsail, Lambda, App Runner 
        - Azure: Container Instances, Container Apps, AKS, App Service, Azure Functions
        - GCP: Google CloudRun, GKE

More details here [ContainerDocs](src-container/Container-Demo.md)

2) AWS Sagemaker AI : called using SageMaker API Invoke Endpoint
    - Realtime / hosted endpoint
    - Serverless
    - Batch Inference

Alternative method:
Jupyter Notebooks on Sagemaker using Sagemaker Python SDK

More details here [SagemakerDocs](src-sagemaker/SageMaker-Demo.md)

3) Deploy to VM Instance:
    - On AWS, make sure to use DeepLearning or ML AMI (Images) as they are designed for ML Workloads

## CI-CD for ML Pipelines:

Some of the Popular Choice of tools that can facilitate CI-CD Process in ML are:

- Traditional CI-CD such as Github Actions, Azure Devops, Gitlab, Circle-CI
- SageMaker Pipelines
- KubeFlow Pipelines
- Google Vertex AI
- Continous Machine Learning (CML) (mostly used with DVC)
- ClearML, BentoML etc

[Placeholder for Sagemker CI-CD Demo using Github Actions]

**What is Github Actions ?**

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production

Github Actions Components:
![alt text](https://docs.github.com/assets/cb-25535/mw-1440/images/help/actions/overview-actions-simple.webp)

Workflow: a configurable automated process that runs one or more jobs

Events: An event is a specific activity in a repository that triggers a workflow run

Job: A job is a set of steps in a workflow that is executed on the same runner. Each step is either a shell script that will be executed, or an action that will be run

Action: An action is a pre-defined, reusable set of jobs or code that performs specific tasks within a workflow

Runner: A runner is a server that runs your workflows when they're triggered.

## Monitoring & Alerting:

### Drift Detection

**Data Drift:** It is the change in statistical properties or distribution of the input data used by machine learning model over time, while the relationship between inputs and the target variable remains the same.

Example: A Model trained on House Pricing

**Concept Drift:** Concept drift occurs when the relationship between the input data and the target variable changes over the time.

Example: Email Spam Detection

Both forms of drift are critical to monitor and address to keep the machine learning models to be effective in real-world environments.

### Metrics

Read more about Metrics [here](./Metrics.md)

## Additional Resources:
- https://www.datacamp.com/tutorial/ci-cd-for-machine-learning

