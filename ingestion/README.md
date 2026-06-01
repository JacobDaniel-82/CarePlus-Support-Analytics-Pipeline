# Data Ingestion

This folder contains all resources required to ingest raw support ticket and support log data into Amazon S3 as part of the CarePlus Support Analytics Pipeline.

## Folder Structure

```text
ingestion/
│
├── support_logs/
│   ├── day-wise logs data/
│   ├── log_date_tracker.txt
│   ├── sample.env
│   └── support_log_ingestion_to_s3.ipynb
│
├── support_tickets/
│   ├── CarePlus_support_DB.sql
│   ├── ticket_date_tracker.txt
│   ├── sample.env
│   └── support_ticket_ingestion_to_s3.ipynb
│
└── README.md
```

---

# Dataset Overview

The ingestion layer works with two datasets:

1. **support_tickets** – Customer support ticket records stored in a MySQL database.
2. **support_logs** – Backend system log files generated for support ticket activities.

These datasets are ingested incrementally into Amazon S3 Raw Storage.

---

# Table 1: support_tickets

This table captures customer support ticket data, including both resolved and unresolved cases.

Each record represents a support issue submitted by a customer and handled by a support agent.

| Column           | Description                            |
| ---------------- | -------------------------------------- |
| ticket_id        | Unique identifier for a support ticket |
| created_at       | Date and time the ticket was created   |
| resolved_at      | Resolution timestamp (nullable)        |
| agent            | Assigned support agent                 |
| priority         | Priority level (Low, Medium, High)     |
| issue_category   | Type of issue reported                 |
| num_interactions | Number of customer-agent interactions  |
| status           | Current ticket status                  |
| channel          | Submission channel                     |

### Status Values

* Resolved
* Open
* Escalated

---

# Table 2: support_logs

This dataset contains backend system logs generated during ticket processing.

Each record represents a system event associated with a support ticket.

| Column        | Description                           |
| ------------- | ------------------------------------- |
| timestamp     | Event timestamp                       |
| log_level     | Log severity level                    |
| component     | System component generating the event |
| ticket_id     | Associated support ticket             |
| session_id    | Session identifier                    |
| ip            | Client IP address                     |
| response_time | Response time in milliseconds         |
| cpu           | CPU utilization at event time         |
| event_type    | Event category                        |
| error         | Error indicator (True/False)          |
| user_agent    | Browser or client information         |
| message       | Event description                     |
| debug         | Internal debugging information        |

---

# Dataset Relationship

The two datasets are connected through the `ticket_id` field.

```text
support_tickets
       |
       | ticket_id
       |
       v
support_logs
```

Relationship Type:

* One-to-Many

Meaning:

* One support ticket can generate multiple backend log events.
* Each log event belongs to a single support ticket.

---

# Support Logs Ingestion

The `support_logs` folder contains raw daily log files and the notebook used to ingest them into Amazon S3.

### Files

| File                              | Purpose                                        |
| --------------------------------- | ---------------------------------------------- |
| day-wise logs data                | Raw support log files                          |
| log_date_tracker.txt              | Tracks the last ingested date                  |
| sample.env                        | Template for AWS credentials and configuration |
| support_log_ingestion_to_s3.ipynb | Incremental ingestion notebook                 |

### Setup

1. Populate the values in `sample.env`.
2. Configure your AWS credentials.
3. Update bucket information if required.
4. Run `support_log_ingestion_to_s3.ipynb`.

The notebook reads the next available log file and uploads it to the S3 Raw Zone.

---

# Support Tickets Ingestion

The `support_tickets` folder contains the database setup scripts and notebook used for incremental ingestion.

### Files

| File                                 | Purpose                                   |
| ------------------------------------ | ----------------------------------------- |
| CarePlus_support_DB.sql              | Database creation and data loading script |
| ticket_date_tracker.txt              | Tracks the last ingested date             |
| sample.env                           | Template for AWS and database credentials |
| support_ticket_ingestion_to_s3.ipynb | Incremental ingestion notebook            |

### Setup

1. Create a MySQL database.
2. Execute `CarePlus_support_DB.sql`.
3. Update database credentials in the notebook and `.env` file.
4. Configure AWS credentials.
5. Run `support_ticket_ingestion_to_s3.ipynb`.

The notebook extracts ticket records for the next ingestion date and uploads them as CSV files into the S3 Raw Zone.

---

# Incremental Ingestion Strategy

Both ingestion pipelines use date tracker files to support incremental loading.

Workflow:

1. Read the last processed date.
2. Determine the next available date.
3. Extract data for that date only.
4. Upload data to Amazon S3.
5. Update the tracker file.

This approach prevents reprocessing previously ingested data and simulates a daily production ingestion workflow.

---

# Output

After successful execution, raw data is stored in the Amazon S3 Raw Zone and becomes available for downstream transformation processes using AWS Lambda and AWS Glue.

