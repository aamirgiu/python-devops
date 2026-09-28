import boto3
import sys

ec2 = boto3.client('ec2', region_name='ap-southeast-2')

action = sys.argv[1] if len(sys.argv) > 1 else 'list'
instance_id = sys.argv[2] if len(sys.argv) > 2 else None

if action == 'list':
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']}")
            print(f"State: {instance['State']['Name']}")
            print(f"Type: {instance['InstanceType']}")

elif action == 'start' and instance_id:
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Starting instance: {instance_id}")

elif action == 'stop' and instance_id:
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Stopping instance: {instance_id}")

else:
    print("Usage:")
    print("  python3 manage-ec2.py list")
    print("  python3 manage-ec2.py start <instance-id>")
    print("  python3 manage-ec2.py stop <instance-id>")
