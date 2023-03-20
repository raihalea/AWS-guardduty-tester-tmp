from aws_cdk import (
    # Duration,
    Stack,
    aws_lightsail as lightsail,
)
from constructs import Construct

class LightsailInstanceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        instance = lightsail.CfnInstance(
            self,
            "Instance",
            blueprint_id="amazon_linux_2",
            bundle_id="nano_2_0",
            instance_name="tester",
            user_data="dig guarddutyc2activityb.com > /home/ec2-user/result.txt"
        )