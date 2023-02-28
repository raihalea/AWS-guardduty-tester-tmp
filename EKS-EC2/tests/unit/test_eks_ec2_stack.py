import aws_cdk as core
import aws_cdk.assertions as assertions

from eks_ec2.eks_ec2_stack import EksEc2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in eks_ec2/eks_ec2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EksEc2Stack(app, "eks-ec2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
