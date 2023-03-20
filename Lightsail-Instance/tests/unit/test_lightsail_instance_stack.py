import aws_cdk as core
import aws_cdk.assertions as assertions

from lightsail_instance.lightsail_instance_stack import LightsailInstanceStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lightsail_instance/lightsail_instance_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LightsailInstanceStack(app, "lightsail-instance")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
