CREATE database careplus_db

DROP TABLE IF EXISTS public.support_logs;

CREATE TABLE public.support_logs (
    timestamp TIMESTAMP,
    log_level VARCHAR(20),
    component VARCHAR(100),
    ticket_id VARCHAR(50),
    session_id VARCHAR(50),
    ip VARCHAR(50),
    response_time BIGINT,
    cpu DOUBLE PRECISION,
    event_type VARCHAR(50),
    error BOOLEAN,
    user_agent VARCHAR(300),
    message VARCHAR(1000),
    debug VARCHAR(1000)
);

COPY public.support_logs
from 's3://careplus-data-storage-1-857110241767-ap-south-2-an/support-logs/processed/'
IAM_ROLE 'arn:aws:iam::857110241767:role/service-role/AmazonRedshift-CommandsAccessRole-20260531T184605'
FORMAT as PARQUET
region 'ap-south-2';

select * from public.support_logs
