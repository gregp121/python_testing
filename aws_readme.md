# Pre-Reqs:

- Create a SAM account

# Setup AWS CLI

Link: https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-prereqs

Note: Check you IAM Identity Center for the AWS Access Portal URL
Note 2: The return key can be sticky

1. run "aws configure sso"

# Overview of Lmabda --> RDS

Link: https://docs.aws.amazon.com/lambda/latest/dg/services-rds-tutorial.html

Several steps are required.
- Create RDS database. Get info:
  - Database Endpoint:
  - Database VPC:
  - You can set "name" in Advanced Configuration, will be used to connect
- Create function execution role
  - Can use default
- Create deployment pacakge (aws_lambda)
  - Code should be a flat structure. (You have your function file in same folder as all other libraries. See Notes)

## Create Deployment Package

For this, we can put our code into a seprate file. Requirements can be included in the bundle

    mkdir package
    pip install --target package pymysql

We can then deploy our code either through the AWS Function console or the AWS CLI
- If we create via AWS CLI, we can pass in our variables in through a EnvVars.json file (Probably not super secure)
- TODO: Look into using SecretsManager instead

## Setup Function

Start by uploading your created zip
  - You will want to add your execution role to permissoins
  - Add the VPC to the connectivity

#### Note on Zip Structure:

Your .zip file should have a flat directory structure, with your function's handler code and all your dependency folders installed at the root as follows.

  my_deployment_package.zip
  |- bin
  |  |-jp.py
  |- boto3
  |  |-compat.py
  |  |-data
  |  |-docs
  ...
  |- lambda_function.py

## Best Practives:

1. It might be best to have one lambda-per-endpoint
- Builds technical debt
- Deployment now impact multiple endpoints (increased blast radius)
- One error hits all endpoints
- Messier logging
- Bugs are harder to find
- Capacity/Usage is harder to track
- Access to permissions is murkier

2. Create API through the gateway, use Method to sort endpoints
- Heirarchy is resource -> method

3. Rememebr to deploy APIs
- This is particularly true to get endpoints for Lambda integrations.

## Test JSON

{
  "Records": [
    {
      "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
      "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
      "body": "{\n     \"CustID\": 1021,\n     \"Name\": \"Martha Rivera\"\n}",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1545082649183",
        "SenderId": "AIDAIENQZJOLO23YVJ4VO",
        "ApproximateFirstReceiveTimestamp": "1545082649185"
      },
      "messageAttributes": {},
      "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-west-2:123456789012:my-queue",
      "awsRegion": "us-west-2"
    }
  ]
}