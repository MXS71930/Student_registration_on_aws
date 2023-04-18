import boto3


ec2 = boto3.client('ec2')

# Create the instance
# response = ec2.run_instances(
#     ImageId='ami-0a695f0d95cefc163',
#     InstanceType='t2.micro',
#     MinCount=1,
#     MaxCount=1,
#     KeyName='reyaan-python',
#     SecurityGroupIds=['sg-039cd7ecc26cd9b7a'],
#     SubnetId='subnet-04715334606a844ca',
#     TagSpecifications=[
#         {
#             'ResourceType': 'instance',
#             'Tags': [
#                 {
#                     'Key': 'Name',
#                     'Value': 'Studentregistration'
#                 },
#             ]
#         },
#     ]
# )

# Print the instance ID
#print(response['Instances'][0]['InstanceId'])


# Start the instance
response = ec2.start_instances(InstanceIds=['i-020ab453d491fb1fb'])

# Print the response
print(response)