import boto3

class Secrets:

    def __init__(self):
        self.ssm = boto3.client('ssm')

    def get_api_key(self):
        parameter_name = 'SindarinApiKey'
        try:
            response = self.ssm.get_parameter(
                Name=parameter_name,
                WithDecryption=True
            )
        
            api_key = response['Parameter']['Value']
        except:
            pass
