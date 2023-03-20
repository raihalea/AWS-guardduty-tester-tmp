#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_guardduty_tester.aws_guardduty_tester_base_stack import AwsGuarddutyTesterBaseStack


app = cdk.App()
base = AwsGuarddutyTesterBaseStack(app, "AwsGuarddutyTesterBaseStack",)


app.synth()
