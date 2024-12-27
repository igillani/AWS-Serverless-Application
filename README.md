# P4.1 - Serverless User Management Application

## Overview
This project demonstrates a serverless architecture for managing users using **AWS services**. It includes a backend powered by **AWS Lambda**, **API Gateway**, and **DynamoDB**, with a frontend hosted on **S3** for user interaction.

---

## Key Features
- **Backend**:
  - **AWS Lambda** for handling API requests (`GET`, `POST`, `DELETE`).
  - **DynamoDB** for persistent data storage.
  - **API Gateway** for exposing RESTful endpoints.
- **Frontend**:
  - A simple HTML/JavaScript-based user interface.
  - Hosted on an S3 bucket with public access enabled.

---

## Architecture
1. **DynamoDB Table**:
   - Used to store user information.
   - Table name: `serverless_users`.
2. **AWS Lambda**:
   - Deployed with the necessary execution role and policies for logging and DynamoDB access.
3. **API Gateway**:
   - Configured to route API requests to the Lambda function.
   - CORS settings applied for frontend access.
4. **S3 Bucket**:
   - Static website hosting enabled to serve the frontend.

---

## Deployment Steps
- **DynamoDB Table**:
  - Created a table with `user_id` as the primary key.
- **Lambda Function**:
  - Wrote and deployed the function to handle CRUD operations.
- **API Gateway**:
  - Configured REST API methods (`GET`, `POST`, `DELETE`) with proper integration.
- **Frontend**:
  - Designed and hosted a static HTML/JavaScript interface on an S3 bucket.
- **CloudFormation Template**:
  - Created a YAML template to automate the deployment of all resources.

---

## Lessons Learned
- **Serverless Integration**:
  - Gained experience in integrating Lambda, DynamoDB, and API Gateway for a seamless backend.
- **Frontend and API Interaction**:
  - Explored CORS configuration and its impact on API requests.
- **CloudFormation**:
  - Automated the infrastructure setup for reproducibility.

---

## Next Steps
- Enhance the frontend for better user interaction (e.g., form validation, error handling).
- Extend the application with additional features like user updates (`PUT` method).
- Explore further automation of deployments using CI/CD pipelines.

---

## Acknowledgments
Special thanks to AWS for providing free-tier services for development and deployment.
