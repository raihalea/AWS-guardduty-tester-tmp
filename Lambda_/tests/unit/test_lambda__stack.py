import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_.lambda__stack import LambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_/lambda__stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaStack(app, "lambda-")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
