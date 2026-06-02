# Analytics & Reporting

This folder contains the analytics and reporting components of the **CarePlus Support Analytics Pipeline**.

After data is transformed and loaded into Amazon Redshift, it becomes available for querying, validation, and business reporting.

This stage focuses on:

* Data validation using AWS Athena
* Querying processed datasets
* Connecting Power BI to Amazon Redshift
* Building reporting dashboards
* Monitoring incremental data updates

---

# Folder Contents

| File                   | Description                                                             |
| ---------------------- | ----------------------------------------------------------------------- |
| athena_queries.sql     | Collection of validation and exploratory queries executed in AWS Athena |
| Careplus_Insights.pbix | Power BI dashboard connected to Amazon Redshift                         |
| Careplus_Insights.pdf  | Exported PDF version of the dashboard                                   |
| README.md              | Folder documentation                                                    |

---

# Analytics Workflow

```text id="s4xp0f"
Amazon S3 Processed Zone
          ↓
AWS Glue Crawler
          ↓
AWS Athena
          ↓
Data Validation
          ↓
Amazon Redshift
          ↓
Power BI Dashboard
```

The analytics layer serves two primary purposes:

1. Validate transformed data before loading into the warehouse.
2. Create business reports and visualizations for end users.

---

# AWS Athena

AWS Athena was used as an ad-hoc analytics and validation tool during the project.

Before querying data, AWS Glue Crawlers were configured to:

* Scan processed Parquet files stored in Amazon S3
* Detect schema information
* Create queryable tables
* Make datasets available within Athena

Once the crawler completed its scan, Athena was used to run SQL queries directly on the processed data.

---

# Why Athena?

Athena was used to:

* Verify transformation outputs
* Validate schema correctness
* Check data quality
* Perform quick exploratory analysis
* Query S3 data without loading it into a warehouse

This helped ensure that the processed datasets were accurate before being loaded into Amazon Redshift.

---

# Athena Queries

The file:

```text id="2i8nzl"
athena_queries.sql
```

contains a collection of SQL queries used during development and validation.

Examples include:

* Record count verification
* Data quality checks
* Ticket status analysis
* Support activity summaries
* Log event exploration

The primary objective was to learn how Athena integrates with AWS Glue Crawlers and Amazon S3 in a modern data lake architecture.

---

# Power BI Dashboard

The final reporting layer was built using Microsoft Power BI.

Dashboard file:

```text id="j6s52x"
Careplus_Insights.pbix
```

PDF export:

```text id="74p0qi"
Careplus_Insights.pdf
```

The dashboard consumes data directly from Amazon Redshift and provides insights into:

### Support Tickets

* Ticket volume
* Ticket status distribution
* Priority breakdown
* Issue categories
* Agent activity

### Support Logs

* Log activity trends
* Event types
* System performance indicators
* Response time metrics
* Operational monitoring insights

---

# Redshift Integration

The dashboard is connected directly to Amazon Redshift.

This allows Power BI to retrieve the latest warehouse data whenever a refresh is performed.

```text id="fnwxz4"
Amazon Redshift
          ↓
Power BI Refresh
          ↓
Updated Dashboard
```

---

# Incremental Data Refresh

The dashboard demonstrates the complete end-to-end pipeline workflow.

When new data is ingested:

```text id="w6v53v"
New Data
    ↓
Amazon S3
    ↓
Transformation
    ↓
Amazon Redshift
    ↓
Power BI Refresh
    ↓
Updated Dashboard
```

New records automatically become available in Redshift after the incremental loading process.

Upon refreshing Power BI, the latest data is reflected in the dashboard without requiring any dashboard modifications.

This validates the successful operation of the entire pipeline from ingestion through reporting.

---

# Learning Outcomes

This stage of the project provided hands-on experience with:

* AWS Glue Crawlers
* AWS Athena
* Querying data directly from Amazon S3
* Data validation workflows
* Amazon Redshift connectivity
* Power BI integration with cloud data warehouses
* End-to-end reporting pipelines

---

# Technologies Used

* AWS Athena
* AWS Glue Crawlers
* Amazon S3
* Amazon Redshift Serverless
* Microsoft Power BI
* SQL

---

This folder represents the final analytics and reporting layer of the CarePlus Support Analytics Pipeline, where transformed and warehouse-ready data is validated, explored, and visualized to generate business insights.
