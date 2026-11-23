import boto3
import os

rds = boto3.client('rds')

def lambda_handler(event, context):
    db_id = os.environ['DB_INSTANCE_ID']
    print(f"Health Alert: Initiating self-healing for {db_id}")
    
    try:
        # Executing a non-destructive reboot to clear connection bottlenecks
        rds.reboot_db_instance(
            DBInstanceIdentifier=db_id, 
            ForceFailover=False
        )
        return {"statusCode": 200, "status": "Healed"}
    except Exception as e:
        print(f"Healing Failed: {str(e)}")
        return {"statusCode": 500, "status": "Failed"}
