import unittest
import boto3
from translation_cache import Cache
from moto import mock_dynamodb2

class TestTranslationCache(unittest.TestCase):

    @mock_dynamodb2
    def test_cache_hit_returns_item(self):
        # Arrange
        dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')
        table = dynamodb.create_table(
            TableName='SindarinCache',
            KeySchema=[
                {'AttributeName': 'text',
                'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'text',
                'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.put_item(
                Item={
                    'text': 'friend',
                    'translation': 'mellon'
                }
            )

        # Act
        system_under_test = Cache(dynamodb)
        result = system_under_test.get_item('friend')

        # Assert
        assert result['translation'] == 'mellon'

    @mock_dynamodb2
    def test_cache_hit_case_insensitive(self):
        pass

    @mock_dynamodb2
    def test_cache_miss_returns_none(self):
        pass
