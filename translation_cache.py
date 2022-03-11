import boto3


class Cache:
    """
    Class that stores the translation of a word in a DynamoDB table.
    """
    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table('SindarinCache')


    def get_item(self, text):
        """
        Returns an item from the DynamoDB table for the given text.
        If there is no matching item, this returns None.
        
        Args:
            text: The text of the item to be retrieved.
        Returns:
            A dictionary of the item that was retrieved from the DynamoDB table.
        """
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
        """
        Saves the item into the DynamoDB table, with the given text and translation.
        
        Args:
            text: The text to be translated.
            translation: The translation of the word.
        """
        self.table.put_item(
            Item={
                'text': text.lower(),
                'translation': translation
            }
        )
    
    # For personal reference/testing
    def print_table(self):
        return self.table.table_name
