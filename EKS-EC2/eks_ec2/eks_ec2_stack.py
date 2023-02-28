import os
from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_ecr_assets as assets
)
from constructs import Construct


class EksEc2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "vpc", nat_gateways=1)

        cluster = eks.Cluster(
            self,
            "Cluster",
            vpc=vpc,
            version=eks.KubernetesVersion.V1_24
        )

        ecr_asset = assets.DockerImageAsset(self,
            "tester",
            directory= "../tester"
        )
        # image_url=ecr_asset.repository.repository_uri
        image_url=ecr_asset.image_uri
        
        print(image_url)
        cluster.add_manifest(
            "mypod",
            {
                "apiVersion": "v1",
                "kind": "Pod",
                "metadata": {"name": "mypod"},
                "spec":{
                    "containers": [{
                        "name": "tester",
                        "image": image_url
                    }]
                }
            },
            # instance_type=ec2.InstanceType("t2.micro")
        )






        # cluster.add

        # task_definistion = ecs.Ec2TaskDefinition(
        #     self,
        #     "TaskDef",
        #     network_mode=ecs.NetworkMode.BRIDGE
        # )
        # task_definistion.add_container(
        #     "tester",
        #     image=ecs.ContainerImage.from_asset("../tester/"),
        #     memory_limit_mib=256,
        #     logging=ecs.AwsLogDriver(stream_prefix="tester-fargate")
        # )

        # service = ecs.Ec2Service(
        #     self,
        #     "Service",
        #     cluster=cluster,
        #     task_definition=task_definistion
        # )