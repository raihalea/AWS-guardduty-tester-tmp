import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_guardduty_tester.aws_guardduty_tester_stack import AwsGuarddutyTesterStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_guardduty_tester/aws_guardduty_tester_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsGuarddutyTesterStack(app, "aws-guardduty-tester")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
