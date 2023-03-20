from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = lambda_.Function(
            self,
            "tester",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="tester.lambda_handler",
            code=lambda_.Code.from_asset("../tester"),
        )