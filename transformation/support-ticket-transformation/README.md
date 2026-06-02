# Support Ticket Transformation

This folder contains the transformation components for the **support_tickets** dataset used in the CarePlus Support Analytics Pipeline.

Unlike the support log transformation, which uses AWS Lambda for data processing, the support ticket transformation is implemented using **AWS Glue** to demonstrate managed ETL workflows and serverless data transformation.

---

## Files

| File                                    | Description                                                                                  |
| --------------------------------------- | -------------------------------------------------------------------------------------------- |
| glue_visual_script_transform_tickets.py | AWS Glue script generated from the visual ETL workflow used during development and testing   |
| glue_automate_etl_script.py             | Automated AWS Glue ETL script used in the production workflow                                |
| lambda_trigger_etl.py                   | AWS Lambda function that triggers the Glue ETL job when new ticket files arrive in Amazon S3 |
| README.md                               | Folder documentation                                                                         |

---

## Transformation Process

The support ticket transformation pipeline performs the following operations:

1. Reads raw CSV ticket files from the Amazon S3 Raw Zone.
2. Applies data cleansing and transformation rules using AWS Glue.
3. Validates and standardizes data formats.
4. Prepares the dataset for analytical workloads.
5. Converts the output into Parquet format.
6. Writes the transformed data to the Amazon S3 Processed Zone.

---

## Development Workflow

The transformation logic was initially created using the AWS Glue Visual ETL interface.

```text
glue_visual_script_transform_tickets.py
```

This script represents the visual workflow used to design and validate the transformation process.

After testing, the workflow was converted into a fully automated Glue script:

```text
glue_automate_etl_script.py
```

which processes incoming files without manual intervention.

---

## Automation Workflow

The transformation process is event-driven.

```text
New Ticket CSV File
          ↓
Amazon S3 Raw Zone
          ↓
S3 Event Trigger
          ↓
AWS Lambda
(lambda_trigger_etl.py)
          ↓
AWS Glue ETL Job
          ↓
Transform & Convert to Parquet
          ↓
Amazon S3 Processed Zone
```

When a new ticket file is uploaded to the S3 Raw Zone, an S3 event notification invokes the Lambda function, which then starts the AWS Glue ETL job.

---

## Usage

### Review Visual ETL Logic

Open:

```text
glue_visual_script_transform_tickets.py
```

to inspect the transformation logic generated from the AWS Glue Visual ETL workflow.

### Run Automated ETL Process

Deploy:

```text
glue_automate_etl_script.py
```

as an AWS Glue Job.

### Configure Event-Based Execution

Deploy:

```text
lambda_trigger_etl.py
```

as an AWS Lambda function and configure an S3 event trigger to automatically launch the Glue job whenever new ticket data is ingested.

---

## Output

The transformation produces a clean, structured, analytics-ready support ticket dataset containing information such as:

* ticket_id
* created_at
* resolved_at
* agent
* priority
* issue_category
* num_interactions
* status
* channel

The final output is stored in **Parquet format** within the Amazon S3 Processed Zone and is later loaded into Amazon Redshift for analytics and reporting.

---

This folder represents the AWS Glue-based transformation layer of the CarePlus ETL pipeline, converting raw ticket data into a warehouse-ready format through an automated serverless workflow.

