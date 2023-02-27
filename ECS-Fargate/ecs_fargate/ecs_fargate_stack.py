from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
)
from constructs import Construct

class EcsFargateStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "vpc", nat_gateways=1)

        cluster = ecs.Cluster(self, "Cluster", vpc=vpc)

        task_definistion = ecs.FargateTaskDefinition(
            self,
            "TaskDef",
        )
        task_definistion.add_container(
            "tester",
            image=ecs.ContainerImage.from_asset("../tester/"),
            logging=ecs.AwsLogDriver(stream_prefix="tester-fargate")
        )

        service = ecs.FargateService(
            self,
            "Service",
            cluster=cluster,
            task_definition=task_definistion
        )