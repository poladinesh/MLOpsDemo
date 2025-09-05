# TBD

## AWS Sagemaker AI : called using SageMaker API Invoke Endpoint
    - Realtime / hosted endpoint or hosted endpoint with ASG (underlying sagemaker using ec2 instances with docker to host the ml app): Real-time inference is ideal for inference workloads where you have interactive, low latency requirements.
    - Serverless: Use Serverless Inference to deploy models without configuring or managing any of the underlying infrastructure. This option is ideal for workloads which have idle periods between traffic spurts and can tolerate cold starts.
    - Batch Inference: Used for long-running Batch Transform jobs to handle large payloads using a batch strategy (mini-batches of up to 100 MB each)
    - Asynchronous Inference: Queues incoming requests and processes them asynchronously. This option is ideal for requests with large payload sizes (up to 1GB), long processing times (up to one hour), and near real-time latency requirements.

### Key Concepts:

Estimator: Encapsulates training on Sagemaker
    - You start your training script by calling fit on Estimator

Predictor: Deploy Model & make Predictions
    - Provide real-time inference and transformation using Python data-types against a SageMaker endpoint

Session: Provides a collection of methods for working with SageMaker resources

Sagemaker Python SDK:
https://sagemaker.readthedocs.io/en/stable/overview.html#using-the-sagemaker-python-sdk

https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html

Using Sci-Kit Learn with Sagemaker Python SDK:
https://sagemaker.readthedocs.io/en/stable/frameworks/sklearn/using_sklearn.html

Other ML Frameworks supported by Sagemaker Python SDK:
https://sagemaker.readthedocs.io/en/stable/frameworks/index.html

Autoscaling:
https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html

