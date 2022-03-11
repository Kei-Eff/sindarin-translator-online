import unittest
import boto3
from translation_cache import Cache
from moto import mock_dynamodb2


@mock_dynamodb2
class TestTranslationCache(unittest.TestCase):

    # Setup test DynamoDB table
    def setUp(self) -> None:
        self.dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')
        self.table = self.dynamodb.create_table(
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

    def test_cache_hit_returns_item(self):
        """Given a key that exists in the cache, cache should return an item.
        """
        # Arrange
        self.table.put_item(
                Item={
                    'text': 'friend',
                    'translation': 'mellon'
                }
            )

        # Act
        system_under_test = Cache(self.dynamodb)
        result = system_under_test.get_item('friend')

        # Assert
        assert result['translation'] == 'mellon'


    def test_cache_hit_case_insensitive(self):
        """Given a key that exists in the cache, in lowercase; and message is sent in uppercase/titlecase, cache should return an item regardless of case.
        """
        # Arrange
        self.table.put_item(
                Item={
                    'text': 'friend',
                    'translation': 'mellon'
                }
            )

        # Act
        system_under_test = Cache(self.dynamodb)
        result = system_under_test.get_item('FrIeNd')

        # Assert
        assert result['translation'] == 'mellon'


    def test_cache_miss_returns_none(self):
        """Given a key that does not exist in the cache, cache should return None.
        """
        # Arrange
        
        # Empty table

        # Act
        system_under_test = Cache(self.dynamodb)
        result = system_under_test.get_item('friend')

        # Assert
        assert result == None
