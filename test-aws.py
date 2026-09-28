import boto3

# AWS se connect karo
ec2 = boto3.client('ec2', region_name='ap-southeast-2')

# Instances ki list nikalo
response = ec2.describe_instances()

print("=" * 50)
print("AWS EC2 Instances")
print("=" * 50)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"State: {instance['State']['Name']}")
        print(f"Type: {instance['InstanceType']}")
        print("-" * 50)

print("Total instances found!")
