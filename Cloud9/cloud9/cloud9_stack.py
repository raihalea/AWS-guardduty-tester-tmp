from aws_cdk import (
    # Duration,
    Stack,RemovalPolicy,CfnOutput,
    aws_ec2 as ec2,
    aws_logs as logs,
    aws_route53resolver as route53resolver,
    aws_cloud9 as cloud9,
    aws_iam as iam,
)
from constructs import Construct
import boto3

class Cloud9Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "vpc", nat_gateways=1)

        log_group = logs.LogGroup(
            self,
            "Log Group",
            log_group_name = "/guardduty-tester/" + self.stack_name,
            removal_policy=RemovalPolicy.DESTROY
            # retention=logs.RetentionDays.ONE_WEEK
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

        sts = boto3.client("sts")
        whoami = sts.get_caller_identity().get("Arn")
        # user = iam.User.from_user_arn(self, "Cloud9User", whoami)

        cloud9_instance = cloud9.CfnEnvironmentEC2(
            self,
            "Cloud9Env",
            # image_id=cloud9.ImageId.AMAZON_LINUX_2,
            # vpc=vpc,
            # owner=cloud9.Owner.user(user),
            instance_type="t2.micro",
            subnet_id=vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC).subnet_ids[0],
            # owner_arn="arn:aws:sts::" + self.account +":*"
            owner_arn=whoami
            # owner=cloud9.Owner.account_root(self.account)
        )

        # CfnOutput(self, "URL", value=cloud9_instance.ide_url)
