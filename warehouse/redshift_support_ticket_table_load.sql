CREATE database careplus_db

DROP TABLE IF EXISTS public.support_tickets;

CREATE TABLE public.support_tickets (
    ticket_id VARCHAR(50),
    created_at TIMESTAMP,
    resolved_at TIMESTAMP,
    agent VARCHAR(200),
    priority VARCHAR(50),
    num_interactions INTEGER,
    issue_category VARCHAR(100),
    channel VARCHAR(50),
    status VARCHAR(50)
)

COPY public.support_tickets
from 's3://careplus-data-storage-1-857110241767-ap-south-2-an/support-tickets/processed/'
IAM_ROLE 'arn:aws:iam::857110241767:role/service-role/AmazonRedshift-CommandsAccessRole-20260531T184605'
FORMAT as PARQUET
region 'ap-south-2';

select count(*) from public.support_tickets