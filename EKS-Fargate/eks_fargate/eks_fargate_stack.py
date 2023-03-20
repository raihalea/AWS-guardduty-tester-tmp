from aws_cdk import (
    # Duration,
    Stack, CfnOutput,
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_ecr_assets as assets,
    aws_iam as iam,
    aws_logs as logs,
    aws_route53resolver as route53resolver
)
from constructs import Construct

class EksFargateStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "vpc", nat_gateways=1)

        log_group = logs.LogGroup(
            self,
            "Log Group",
            log_group_name = "/guardduty-tester/" + self.stack_name,
            retention=logs.RetentionDays.ONE_WEEK
        )

        resolver_logging = route53resolver.CfnResolverQueryLoggingConfig(
            self,
            "DNSlogging",
            destination_arn=log_group.log_group_arn
        )

        resolver_logging_associate = route53resolver.CfnResolverQueryLoggingConfigAssociation(
            self,
            "DNSloggingAssociate",
            resolver_query_log_config_id=resolver_logging.attr_id,
            resource_id=vpc.vpc_id
        )

        cluster = eks.FargateCluster(
            self,
            "Cluster",
            vpc=vpc,
            version=eks.KubernetesVersion.V1_24,
            
        )
        # cluster.aws_auth.add_account(self.account)

        cluster.admin_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                resources=["*"],
                actions=["eks:*"]
            )
        )

        ecr_asset = assets.DockerImageAsset(self,
            "tester",
            directory= "../tester"
        )
        # image_url=ecr_asset.repository.repository_uri
        image_url=ecr_asset.image_uri
        
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

        # cluster.add_manifest(
        #     "logging",
        #     {
        #         "apiVersion": "v1",
        #         "kind": "Namespace",
        #         "metadata": {"name": "amazon-cloudwatch"},
        #         "labels": {"name": "amazon-cloudwatch"},
        #     }
        # )

        CfnOutput(self, "EKSclusterRole", value=cluster.admin_role.role_name)