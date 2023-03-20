from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
    aws_ec2 as ec2,
    aws_logs as logs,
    aws_route53resolver as route53resolver
)
from constructs import Construct

class LambdaVpcStack(Stack):

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

        fn = lambda_.Function(
            self,
            "tester",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="tester.lambda_handler",
            code=lambda_.Code.from_asset("../tester"),
            vpc=vpc
        )