# Data Warehouse

This folder contains the data warehousing components of the **CarePlus Support Analytics Pipeline**.

After data is transformed and stored as Parquet files in the Amazon S3 Processed Zone, it is loaded into **Amazon Redshift Serverless**, which serves as the centralized analytics warehouse for reporting and business intelligence.

This stage is responsible for:

* Schema generation
* Table creation
* Incremental data loading
* Redshift integration
* Automated warehouse updates

The warehouse acts as the final analytical layer before data is consumed by Power BI dashboards.

---

# Folder Contents

| File                                      | Description                                                                                             |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| lambda_incremental_load_logs.py           | Lambda function for incremental loading of processed support log files into Redshift                    |
| lambda_incremental_load_tickets.py        | Lambda function for incremental loading of processed support ticket files into Redshift                 |
| psycopg2_lambda_layer.zip                 | Custom Lambda layer containing the psycopg2 library required for Redshift connectivity                  |
| redshift_support_log_table_load.sql       | SQL script for creating and loading the support logs table                                              |
| redshift_support_ticket_table_load.sql    | SQL script for creating and loading the support tickets table                                           |
| schema_extract_from_ticket_and_logs.ipynb | Notebook used to extract schemas from transformed Parquet files and generate Redshift table definitions |
| support_logs_2025-07-02.parquet           | Sample processed support logs file                                                                      |
| support_ticket_2025-07-01.parquet         | Sample processed support tickets file                                                                   |
| README.md                                 | Folder documentation                                                                                    |

---

# Warehouse Workflow

The warehouse layer begins after the transformation stage is completed.

```text id="vx5vr3"
Processed Parquet Files
          ↓
Schema Extraction
          ↓
Redshift Table Creation
          ↓
Incremental Loading
          ↓
Amazon Redshift Serverless
          ↓
Power BI Dashboard
```

The transformed datasets are loaded into Redshift where they become available for reporting and analytics.

---

# Schema Extraction

Before creating Redshift tables, the schema of the transformed datasets must be identified.

To accomplish this:

```text id="4c8i4t"
schema_extract_from_ticket_and_logs.ipynb
```

was used to inspect the Parquet files and determine:

* Column names
* Data types
* Table structure

The extracted schema was then used to generate the Redshift table creation scripts.

---

# Redshift Table Setup

Two analytical tables were created:

### Support Logs Table

Stores structured backend log information such as:

* ticket_id
* timestamp
* response_time
* cpu
* event_type
* error

### Support Tickets Table

Stores customer support ticket information such as:

* ticket_id
* created_at
* resolved_at
* agent
* priority
* status

Table creation and loading logic is included in:

```text id="kkbtg8"
redshift_support_log_table_load.sql
redshift_support_ticket_table_load.sql
```

---

# Why Amazon Redshift?

Amazon Redshift was chosen because:

* It is a cloud-native data warehouse.
* It is optimized for analytical workloads.
* It integrates seamlessly with Amazon S3.
* It supports high-performance SQL querying.
* It provides direct connectivity with Power BI.

The project uses **Amazon Redshift Serverless**, eliminating the need to manage warehouse infrastructure.

---

# Incremental Loading Strategy

The project implements an incremental loading approach.

Instead of reloading all historical data, only newly processed files are loaded into Redshift.

Benefits include:

* Reduced processing time
* Lower compute costs
* Preservation of historical data
* Improved scalability

The workflow follows:

```text id="4sp19d"
New Processed File
          ↓
S3 Processed Zone
          ↓
S3 Event Notification
          ↓
AWS Lambda
          ↓
Redshift COPY Command
          ↓
Append New Records
```

This ensures that newly transformed data becomes available in the warehouse automatically.

---

# Automated Warehouse Loading

Two Lambda functions were created:

### Logs Pipeline

```text id="dntwcm"
lambda_incremental_load_logs.py
```

Responsible for loading processed support log files into Redshift.

### Tickets Pipeline

```text id="iw7v2n"
lambda_incremental_load_tickets.py
```

Responsible for loading processed support ticket files into Redshift.

Whenever a new Parquet file is placed into the S3 Processed Zone, an S3 event notification triggers the appropriate Lambda function.

The Lambda function then executes a Redshift COPY command to load the file into the target table.

---

# Redshift Connectivity

AWS Lambda does not include the required PostgreSQL driver by default.

To enable Redshift connectivity:

```text id="qqn6ys"
psycopg2_lambda_layer.zip
```

was created and attached as a custom Lambda Layer.

This allows the Lambda functions to:

* Connect to Redshift
* Execute SQL commands
* Trigger COPY operations
* Handle incremental loading

---

# Sample Processed Data

The following sample files are included to demonstrate the output produced by the transformation layer:

```text id="5tnzja"
support_logs_2025-07-02.parquet
support_ticket_2025-07-01.parquet
```

These files were used during schema extraction and warehouse setup.

---

# End-to-End Warehouse Flow

```text id="s3d6r7"
Raw Data
    ↓
Transformation Layer
(Lambda / Glue)
    ↓
Processed Parquet Files
    ↓
Amazon S3 Processed Zone
    ↓
S3 Event Notification
    ↓
Lambda Incremental Loader
    ↓
Amazon Redshift Serverless
    ↓
Power BI Dashboard
```

---

# Technologies Used

* Amazon Redshift Serverless
* Amazon S3
* AWS Lambda
* S3 Event Notifications
* SQL
* Python
* psycopg2
* Apache Parquet

---

This folder represents the warehousing layer of the CarePlus Support Analytics Pipeline, where transformed datasets are automatically loaded into Amazon Redshift and prepared for analytics and business intelligence reporting.

