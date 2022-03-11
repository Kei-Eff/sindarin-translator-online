import boto3


class Secrets:
    """Class that retrieves secrets from AWS SSM Parameter Store.
    """

    def __init__(self):
        self.ssm = boto3.client('ssm')

    def get_api_key(self):
        """Gets the API key from Parameter Store.

        Returns:
            The API key.
        """

        parameter_name = 'SindarinApiKey'

        try:
            response = self.ssm.get_parameter(
                Name=parameter_name,
                WithDecryption=True
            )

            api_key = response['Parameter']['Value']
        except:
            pass
