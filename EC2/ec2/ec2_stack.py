from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct


class Ec2Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "vpc", nat_gateways=1)

        instance = ec2.Instance(
            self,
            "Instance",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                kernel=ec2.AmazonLinuxKernel.KERNEL5_X
            ),
            vpc=vpc,
        )


        ssmagent_url = "https://s3." + self.region +".amazonaws.com/amazon-ssm-" + self.region + "/latest/linux_amd64/amazon-ssm-agent.rpm"
        userdata_txt = "sudo yum install -y " + ssmagent_url
        instance.user_data.for_linux()
        instance.user_data.add_commands(userdata_txt)
        instance.user_data.add_commands("dig guarddutyc2activityb.com")

