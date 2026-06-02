import json
import re
import io
import boto3
import pandas as pd
from io import StringIO
import pyarrow as pa
import pyarrow.parquet as pq
import io

def save_parquet_to_s3(df, bucket, key):
    # Convert DataFrame to Parquet
    table = pa.Table.from_pandas(df, preserve_index=False)
    
    # Create a buffer to hold the Parquet data
    parquet_buffer = io.BytesIO()
    pq.write_table(table, parquet_buffer)

    # Initialize S3 client and upload the Parquet file
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=key, Body=parquet_buffer.getvalue())
    print(f"✅ Parquet saved to s3://{bucket}/{key}")

def read_log_from_s3(bucket, key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    log_data = response['Body'].read().decode('utf-8')
    return log_data

def lambda_handler(event, context):
    bucket = "careplus-data-storage-1-857110241767-ap-south-2-an"
    key = "support-logs/raw/support_logs_2025-07-01.log"

    # 1. Fetch the data from S3
    raw_logs = read_log_from_s3(bucket, key)
    
    # 2. Split entries
    entries = [entry.strip() for entry in raw_logs.split('---') if entry.strip()]
    
    # 3. Compile your Regex pattern
    log_pattern = re.compile(
        r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<log_level>[A-Za-z0-9_]+)\] '
        r'(?P<component>[^\s]+) - TicketID=(?P<ticket_id>[^\s]+) SessionID=(?P<session_id>[^\s]+)\s*'
        r'IP=(?P<ip>.*?) \| ResponseTime=(?P<response_time>-?\d+)ms \| CPU=(?P<cpu>[\d.]+)% \| EventType=(?P<event_type>.*?) \| Error=(?P<error>\w+)\s*'
        r'UserAgent="(?P<user_agent>.*?)"\s*'
        r'Message="(?P<message>.*?)"\s*'
        r'Debug="(?P<debug>.*?)"\s*'
        r'TraceID=(?P<trace_id>.*)'
    )

    # 4. Extract structured data
    parsed_entries = []
    for entry in entries:
        match = log_pattern.search(entry)
        if match:
            parsed_entries.append(match.groupdict())
            
    # 5. Build DataFrame and perform transformations
    df = pd.DataFrame(parsed_entries)
    
    # Drop trace_id here
    df = df.drop('trace_id', axis=1)
    
    # Convert data types
    df = df.astype({
        "response_time": "int",
        "cpu": "float"
    })
    
    # Filter out negative response times
    df = df[df.response_time >= 0]
    
    # Normalize log levels
    fix_log_level = {'INF0': 'INFO', 'DEBG': 'DEBUG', 'warnING': 'WARNING', 'EROR': 'ERROR'}
    df['log_level'] = df['log_level'].replace(fix_log_level)
    
    # Drop duplicates
    df = df.drop_duplicates()
    
    # 6. Final Outputs (Will show up directly in CloudWatch Logs)
    print("--- FINAL DATAFRAME SHAPE ---")
    print(df.shape)
    print("\n--- FINAL DATAFRAME HEAD ---")
    print(df.head())

    # Save the data (Upload Parquet to S3)
    output_key = 'support-logs/processed/support_logs_2025-07-01.parquet'
    save_parquet_to_s3(df, "careplus-data-storage-1-857110241767-ap-south-2-an", output_key)

