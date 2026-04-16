import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_id = 'i-0ea5dd1b4c2b171fb'  # Replace with your EC2 instance ID
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"EC2 instance {instance_id} stopped")