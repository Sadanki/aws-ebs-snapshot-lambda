import boto3
import datetime

# Replace with your EBS Volume ID
VOLUME_ID = 'vol-0e5b12ae3d1e23bb6'
REGION = 'ap-south-1'
RETENTION_DAYS = 0

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=REGION)

    # 1. Create snapshot
    snapshot = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description=f"Automated snapshot for {VOLUME_ID}",
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [{'Key': 'CreatedBy', 'Value': 'LambdaBackup'}]
            }
        ]
    )
    print(f"Created snapshot: {snapshot['SnapshotId']}")

    # 2. Get all snapshots created by this function
    snapshots = ec2.describe_snapshots(
        Filters=[
            {'Name': 'volume-id', 'Values': [VOLUME_ID]},
            {'Name': 'tag:CreatedBy', 'Values': ['LambdaBackup']}
        ],
        OwnerIds=['self']
    )['Snapshots']

    # 3. Delete old snapshots
    for snap in snapshots:
        start_time = snap['StartTime'].replace(tzinfo=None)
        age = (datetime.datetime.now() - start_time).days

        if age > RETENTION_DAYS:
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
            print(f"Deleted snapshot: {snap['SnapshotId']} (Age: {age} days)")
