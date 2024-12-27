import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('serverless_users')

def lambda_handler(event, context):
    # Determine the HTTP method
    http_method = event['httpMethod']

    if http_method == 'GET':
        # Retrieve all users
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }

    elif http_method == 'POST':
        # Add a new user
        user_data = json.loads(event['body'])
        table.put_item(Item=user_data)
        return {
            'statusCode': 200,
            'body': 'User added successfully'
        }

    elif http_method == 'DELETE':
        # Delete a user by user_id
        user_id = event['queryStringParameters']['user_id']
        table.delete_item(Key={'user_id': user_id})
        return {
            'statusCode': 200,
            'body': 'User deleted successfully'
        }

    else:
        # Unsupported HTTP method
        return {
            'statusCode': 400,
            'body': 'Unsupported HTTP method'
        }
