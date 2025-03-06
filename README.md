# CSV-file-processing-with-AWS

# AWS-Based Serverless CSV File Processing

## Overview
This project showcases a **serverless architecture** using AWS services to process CSV files dynamically. It integrates **Amazon S3, AWS Lambda, IAM Roles, DynamoDB, and CloudWatch** for automated event-driven processing.

![workflow diagram](https://github.com/user-attachments/assets/3fc27ff5-1179-4d12-b632-d7535d8deaf8)

## Architecture Workflow
1. **CSV file upload** triggers an event in an **S3 bucket**.
2. **AWS Lambda function** processes the CSV file and extracts relevant data.
3. **DynamoDB** stores metadata extracted from the file.
4. **CloudWatch** monitors logs and errors for the Lambda function.

## Technologies Used
- **Amazon S3** - Storage for CSV files.
- **AWS Lambda** - Serverless function execution.
- **IAM Roles** - Secure access control.
- **DynamoDB** - NoSQL database for storing file data.
- **CloudWatch** - Monitoring and logging service.

## Setup Guide

### 1. Create an S3 Bucket
- Go to **AWS Management Console** → **S3**.
- Click **Create Bucket**, configure settings, and set permissions.
- Upload a sample CSV file to trigger the workflow.
  
  ![S3 Bucket](https://github.com/user-attachments/assets/fd7e1722-9bcd-4f49-936c-226786e801a4)

### 2. Configure IAM Role for Lambda
- Open **AWS IAM** → **Roles**.
- Click **Create Role** and select **Lambda** as the trusted entity.
- Attach policies like:
  - `AmazonS3FullAccess`
  - `AWSLambdaBasicExecutionRole`
  - `AmazonDynamoDBFullAccess`
- Save the role and assign it to the Lambda function.

  ![IAM Role](https://github.com/user-attachments/assets/7a07cdaa-c7c8-43cc-920e-495e87733a8d)

### 3. Deploy AWS Lambda Function
- Navigate to **AWS Lambda** → **Create Function**.
- Choose **Author from Scratch**.
- Assign the IAM role created earlier.
- Write and deploy a Python function to process S3 events.
- Test the function using a sample file.

  ![LambdaFunction](https://github.com/user-attachments/assets/b83e6416-9242-47e9-8aee-0eb928183bbb)

### 4. Set Up DynamoDB
- Go to **AWS DynamoDB** → **Create Table**.
- Define a **Primary Key** (e.g., `FileName`).
- Configure additional attributes if needed.
  
![DynamoDB1](https://github.com/user-attachments/assets/40e5aa80-e7d8-4676-bb86-50f3f87f74ed)

### 5. Enable CloudWatch Monitoring
- Open **AWS CloudWatch** → **Logs**.
- Link Lambda logs to CloudWatch.
- Configure **CloudWatch Alarms** for failure alerts.

![CloudWatch](https://github.com/user-attachments/assets/c288a182-f150-4a51-a0fc-df447f3420c6)

## Conclusion
This project provides a **scalable, cost-efficient, and automated** way to process CSV files in the cloud. Using AWS serverless services ensures **minimal maintenance** while achieving **high availability**.








