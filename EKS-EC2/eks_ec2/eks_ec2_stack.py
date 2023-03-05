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
            }
        )
