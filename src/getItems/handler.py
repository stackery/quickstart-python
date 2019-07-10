import os
import boto3

dynamodb = boto3.resource('dynamodb')

def handler(event, context):
  table_name = os.environ['TABLE_NAME'] # get the table name from the automatically populated environment variables
  table = dynamodb.Table(table_name)

  # Use dynamodb to get items from the Item table
  result = table.scan()
  result_count = result['Count']
  items = result['Items']

  for item in items:
    item_id = item['id']
    content = item['content']
    print(f'Item {item_id}: {content}')

  # Return a 200 response if no errors
  response = {
    'statusCode': 200,
    'body': f'{result_count} items found'
  }

  return response
  