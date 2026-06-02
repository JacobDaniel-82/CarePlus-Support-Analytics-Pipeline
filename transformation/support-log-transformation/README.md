# Support Log Transformation

This folder contains the transformation logic for the **support_logs** dataset used in the CarePlus Support Analytics Pipeline.

The raw support logs are stored as unstructured text files and are transformed into a structured, analytics-ready format before being stored in Amazon S3 as Parquet files.

---

## Files

| File                            | Description                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------ |
| lambda_etl_logs.py              | AWS Lambda script used for automated log transformation and Parquet generation |
| log_transformation_script.ipynb | Jupyter Notebook used to develop, test, and validate the transformation logic  |
| support_logs_2025-07-01.log     | Sample raw support log file used during development and testing                |
| README.md                       | Folder documentation                                                           |

---

## Transformation Process

The transformation pipeline performs the following steps:

1. Reads raw log data.
2. Splits individual log entries.
3. Extracts structured fields using regular expressions.
4. Converts log records into a tabular format.
5. Cleans and standardizes data values.
6. Removes invalid and duplicate records.
7. Applies appropriate data types.
8. Converts the final dataset into Parquet format.
9. Stores the processed output in the Amazon S3 Processed Zone.

---

## Development Workflow

The transformation logic was initially developed and tested using:

```text
log_transformation_script.ipynb
```

The validated transformation logic was then migrated into:

```text
lambda_etl_logs.py
```

for automated execution through AWS Lambda whenever new log files arrive in the S3 Raw Zone.

---

## Sample Input

```text
support_logs_2025-07-01.log
```

This sample file represents the raw log format used by the transformation process and can be used to test or understand the parsing logic.

---

## Output

The transformation produces a structured dataset containing fields such as:

* timestamp
* ticket_id
* session_id
* response_time
* cpu
* event_type
* error
* user_agent
* message
* debug

The final output is stored in **Parquet format** for efficient analytics and downstream processing.

---

## Usage

### Explore the Transformation Logic

Open:

```text
log_transformation_script.ipynb
```

to understand and test the transformation process step-by-step.

### AWS Lambda Execution

Deploy:

```text
lambda_etl_logs.py
```

as an AWS Lambda function and configure an S3 event trigger to automatically process newly ingested log files.

---

This folder represents the log processing component of the CarePlus ETL pipeline, transforming raw operational logs into structured, analytics-ready data.

