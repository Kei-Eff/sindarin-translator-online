import boto3

class Cache:

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('SindarinCache')

    def get_item(self, text):
        response = self.table.get_item(
            Key={
                'text': text.lower()
            }
        )

        if 'Item' in response:            
            item = response['Item']
            return item
        
        pass

    def save_item(self, text, translation):
        self.table.put_item(
            Item={
                'text': text.lower(),
                'translation': translation
            }
        ) 
    
    # For personal reference
    def print_table(self):
        return self.table.table_name