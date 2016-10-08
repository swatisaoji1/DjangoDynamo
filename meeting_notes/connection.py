import boto3


class DynamoDB:

    def __init__(self, region='us-west-2'):
        self.dynamodb = boto3.resource('dynamodb', region_name=region)


    def get_table(self, table_name):
        return self.dynamodb.Table(table_name)