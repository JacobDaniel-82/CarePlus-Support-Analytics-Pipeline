# Architecture

This folder contains the architecture and data flow diagrams for the **CarePlus Support Analytics Pipeline**.

These diagrams provide a high-level and detailed view of how data moves through the AWS ecosystem, from ingestion to analytics and reporting.

---

# Architecture Artifacts

| File                              | Description                                                                                                           |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| aws_pipeline.png                  | Simplified end-to-end AWS pipeline overview                                                                           |
| detailed_architecture_diagram.png | Detailed architecture showing all AWS services, storage layers, transformations, automation, and reporting components |
| data_flow_diagram.png             | Data flow representation showing how data moves across the pipeline                                                   |
| README.md                         | Documentation for architecture diagrams                                                                               |

---

# 1. Simplified AWS Pipeline

This diagram provides a quick overview of the complete pipeline and is the best starting point for understanding the project.

![AWS Pipeline](./aws_pipeline.png)

### Highlights

* Daily incremental data ingestion
* Amazon S3 Raw and Processed Zones
* AWS Lambda transformations
* AWS Glue ETL processing
* Amazon Athena validation layer
* Amazon Redshift Serverless warehouse
* Power BI reporting layer

---

# 2. Detailed Architecture Diagram

This diagram illustrates all major AWS services, event triggers, storage locations, transformation components, and reporting layers used in the project.

![Detailed Architecture](./detailed_architecture_diagram.png)

### Components Covered

#### Data Sources

* Support Logs (TXT Files)
* MySQL Support Tickets Database

#### Ingestion Layer

* Jupyter Notebook ingestion processes
* Incremental date-based loading

#### Storage Layer

* Amazon S3 Raw Zone
* Amazon S3 Processed Zone

#### Transformation Layer

* AWS Lambda
* AWS Glue

#### Analytics Layer

* AWS Athena
* AWS Glue Crawlers

#### Warehouse Layer

* Amazon Redshift Serverless

#### Reporting Layer

* Power BI Dashboard

#### Automation Layer

* Amazon S3 Event Notifications
* AWS Lambda Triggers
* Incremental Redshift Loading

---

# 3. Data Flow Diagram

This diagram focuses on how data moves throughout the pipeline and how each stage processes the incoming datasets.

![Data Flow Diagram](./data_flow_diagram.png)

### Data Flow Summary

```text
Support Logs (TXT)
            \
             \
              --> Amazon S3 Raw
             /
MySQL Tickets
      |
      v
AWS Lambda / AWS Glue
      |
      v
Amazon S3 Processed (Parquet)
      |
      v
Amazon Athena
      |
      v
Amazon Redshift Serverless
      |
      v
Power BI Dashboard
```

---

# Architectural Design Goals

The solution was designed to demonstrate key data engineering concepts:

* Incremental data ingestion
* Event-driven processing
* Serverless transformation
* Data lake architecture
* Columnar storage using Parquet
* Automated warehouse loading
* Cloud-native analytics
* End-to-end reporting

---

# Technology Stack

### Storage

* Amazon S3

### Processing

* AWS Lambda
* AWS Glue

### Query & Validation

* AWS Athena
* AWS Glue Crawlers

### Data Warehouse

* Amazon Redshift Serverless

### Visualization

* Microsoft Power BI

### Programming

* Python
* SQL

---

These diagrams serve as the visual reference for understanding the complete CarePlus Support Analytics Pipeline architecture and data movement across AWS services.

