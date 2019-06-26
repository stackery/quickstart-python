import os
import boto3

dynamodb = boto3.resource('dynamodb')

def handler(event, context):
  table_name = os.environ['TABLE_NAME'] # get the table name from the automatically populated environment variables
  table = dynamodb.Table(table_name)

  params = {
    'id': '5', # modify with each invoke so the id does not repeat
    'content': 'Whee' # modify content here
  }

  # Write a new item to the ItemTable
  item_id = params.get('id')
  print(f'Adding item {item_id} to table {table_name}')
  table.put_item(Item = params, ConditionExpression='attribute_not_exists(id)') # do not overwrite existing entries
  print('Item added to table, done')

  # Return a 200 response if no errors
  response = {
    'statusCode': 200,
    'body': 'Success!'
  }

  return response
