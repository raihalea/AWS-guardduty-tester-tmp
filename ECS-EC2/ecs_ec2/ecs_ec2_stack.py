from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
)
from constructs import Construct

class EcsEc2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "vpc", nat_gateways=1)

        cluster = ecs.Cluster(self, "Cluster", vpc=vpc)
        cluster.add_capacity(
            "capacity", 
            instance_type=ec2.InstanceType("t2.micro")
        )

        task_definistion = ecs.Ec2TaskDefinition(
            self,
            "TaskDef",
            network_mode=ecs.NetworkMode.BRIDGE
        )
        task_definistion.add_container(
            "tester",
            image=ecs.ContainerImage.from_asset("../tester/"),
            memory_limit_mib=256,
            logging=ecs.AwsLogDriver(stream_prefix="tester-fargate")
        )

        service = ecs.Ec2Service(
            self,
            "Service",
            cluster=cluster,
            task_definition=task_definistion
        )