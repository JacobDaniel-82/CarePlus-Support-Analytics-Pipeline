import psycopg2

# Redshift Serverless configuration
REDSHIFT_HOST = '' # your serverless endpoint
REDSHIFT_PORT = '' # your serverless port
REDSHIFT_DATABASE = 'careplus_db'  # Replace with your Redshift database name
REDSHIFT_USER = 'admin'  # Replace with your Redshift username
REDSHIFT_PASSWORD = ''  # Replace with your Redshift password
REDSHIFT_TABLE = 'public.support_tickets'  # Replace with your table name
IAM_ROLE = ''  # Your IAM role ARN

def lambda_handler(event, context):
    # # 1: read data from the bucket
    # # # Get bucket and object key from the S3 event trigger
    record = event['Records'][0]
    bucket_name = record['s3']['bucket']['name']
    input_key = record['s3']['object']['key']

    print(f"📥 Triggered by: s3://{bucket_name}/{input_key}")

    s3_input_path = f's3://{bucket_name}/{input_key}'

    #s3_input_path = 's3://careplus-data-storage-1-857110241767-ap-south-2-an/support-tickets/processed/run-1780305332479-part-block-0-r-00000-snappy.parquet'

    # Connect to Redshift Serverless using psycopg2
    conn = psycopg2.connect(
            host=REDSHIFT_HOST,
            port=REDSHIFT_PORT,
            dbname=REDSHIFT_DATABASE,
            user=REDSHIFT_USER,
            password=REDSHIFT_PASSWORD
    )

    cursor = conn.cursor()

    # COPY SQL query to load data from S3 into the Redshift table
    copy_sql = f"""
        COPY {REDSHIFT_TABLE}
        FROM '{s3_input_path}'
        IAM_ROLE '{IAM_ROLE}'
        FORMAT AS PARQUET
        REGION 'ap-south-2';
        """

    # Execute the query
    cursor.execute(copy_sql)

    # Commit the changes (important for COPY operations)
    conn.commit()

    # Log success
    print(f"Data successfully copied from {s3_input_path} to {REDSHIFT_TABLE}")


    # Close the cursor and the connection
    cursor.close()
    conn.close()
