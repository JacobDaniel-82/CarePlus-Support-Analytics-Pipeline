# CarePlus Support Analytics Pipeline

## End-to-End AWS Data Engineering Pipeline for Customer Support Analytics

This project demonstrates the design and implementation of a complete cloud-native data engineering pipeline on AWS. The solution ingests customer support tickets and backend support logs, transforms raw operational data into analytics-ready datasets, loads them into a cloud data warehouse, and delivers business insights through Power BI dashboards.

The pipeline was built to simulate a real-world support analytics platform using modern data engineering concepts such as incremental ingestion, event-driven processing, serverless ETL, data lake architecture, automated warehouse loading, and cloud-based reporting.

![AWS Pipeline](architecture/aws_pipeline.png)

---

## Architecture Overview

![AWS architecture](architecture/detailed_architecture_diagram.png)

---

## Project Objectives

* Build an end-to-end AWS Data Engineering pipeline.
* Implement incremental data ingestion.
* Store raw and processed datasets in Amazon S3.
* Transform raw data using AWS Lambda and AWS Glue.
* Convert datasets into Parquet format for efficient analytics.
* Validate transformed data using AWS Athena.
* Load processed data into Amazon Redshift Serverless.
* Implement automated incremental warehouse loading.
* Create reporting dashboards using Power BI.
* Gain hands-on experience with AWS IAM, CloudWatch, event triggers, and serverless services.

---

## Business Scenario

CarePlus is a customer support organization that manages support requests from multiple clients.

The organization receives:

### Support Tickets

Customer-reported issues submitted through:

* Email
* Chat
* Phone
* Web Forms

### Support Logs

Backend system logs generated during ticket processing, including:

* API activity
* System events
* Performance metrics
* Debug information
* Error tracking

The objective is to build a scalable analytics platform that can automatically process incoming support data and provide operational insights.

---

## Dataset Overview

### support_tickets

Contains customer support ticket information including:

* Ticket details
* Agents
* Priorities
* Statuses
* Channels
* Interaction counts

### support_logs

Contains backend operational logs including:

* Timestamps
* Components
* Response times
* CPU metrics
* Event types
* Error indicators

### Relationship

```text
support_tickets
       |
       | ticket_id
       |
       v
support_logs
```

One Ticket → Many Log Records

---

## End-to-End Workflow

![AWS Dataflow](architecture/data_flow_diagram.png)

```text
Support Logs (TXT)              Support Tickets (MySQL)
        |                                  |
        |                                  |
        +----------- Data Ingestion -------+
                           |
                           v
                    Amazon S3 Raw Zone
                           |
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
     AWS Lambda                      AWS Glue
 (Log Transformation)        (Ticket Transformation)
          |                                 |
          +----------------+----------------+
                           |
                           v
                 Amazon S3 Processed Zone
                       (Parquet)
                           |
                           v
                     AWS Athena
                    Data Validation
                           |
                           v
               Amazon Redshift Serverless
                           |
                           v
                     Power BI Dashboard
```

---

## AWS Services Used

| Service                    | Purpose                             |
| -------------------------- | ----------------------------------- |
| Amazon S3                  | Data Lake Storage                   |
| AWS Lambda                 | Serverless Transformation & Loading |
| AWS Glue                   | Managed ETL Processing              |
| AWS Glue Crawlers          | Schema Discovery                    |
| AWS Athena                 | Data Validation & Querying          |
| Amazon Redshift Serverless | Cloud Data Warehouse                |
| Amazon CloudWatch          | Monitoring & Logging                |
| AWS IAM                    | Access Control & Security           |
| Power BI                   | Reporting & Visualization           |

---

## Key Data Engineering Concepts Demonstrated

### Incremental Ingestion

Both support logs and support tickets are ingested incrementally using date-tracking mechanisms to simulate daily production data arrival.

### Event-Driven Processing

Amazon S3 Event Notifications automatically trigger downstream processing whenever new files arrive.

### Serverless ETL

The project leverages AWS Lambda and AWS Glue to process data without managing infrastructure.

### Data Lake Architecture

Raw and processed datasets are separated into dedicated zones within Amazon S3.

### Parquet Storage

Processed data is stored in Parquet format to improve storage efficiency and query performance.

### Automated Warehouse Loading

Processed datasets are automatically loaded into Amazon Redshift using Lambda-based incremental loading.

### Analytics & Reporting

Validated warehouse data is exposed through Power BI dashboards for business reporting.

---

## Repository Structure

```text
careplus-support-analytics-pipeline/
│
├── architecture/
├── ingestion/
├── transformation/
├── warehouse/
├── analytics/
├── screenshots/
│
└── README.md
```

### Folder Guide

| Folder         | Purpose                                           |
| -------------- | ------------------------------------------------- |
| architecture   | Architecture diagrams and data flow documentation |
| ingestion      | Raw data ingestion workflows and datasets         |
| transformation | AWS Lambda and AWS Glue ETL processes             |
| warehouse      | Amazon Redshift setup and incremental loading     |
| analytics      | Athena queries and Power BI dashboard             |
| screenshots    | AWS service screenshots and project evidence      |

Each folder contains its own README with implementation details and setup instructions.

---

## Architecture & Design Documents

Detailed diagrams are available in:

```text
architecture/
```

Including:

* AWS Pipeline Diagram
* Detailed Architecture Diagram
* Data Flow Diagram

---

## Screenshots

Project screenshots are available in:

```text
screenshots/
```

Including:

* Amazon S3
* AWS Lambda
* AWS Glue
* Athena
* Redshift
* CloudWatch
* IAM
* Event Triggers

---

## Dashboard

The final reporting layer is built using Power BI and connected directly to Amazon Redshift.

Features include:

### Support Ticket Insights

* Ticket Volume
* Status Distribution
* Priority Analysis
* Agent Activity
* Issue Categories

### Support Log Insights

* Event Monitoring
* System Activity
* Response Time Analysis
* Operational Trends

The dashboard automatically reflects newly ingested data after warehouse updates and refresh operations.

---

## Learning Outcomes

Through this project, I gained practical experience with:

* AWS Cloud Services
* Data Lake Architecture
* ETL Pipeline Development
* Event-Driven Systems
* Incremental Data Loading
* Amazon Redshift
* AWS Athena
* AWS Glue
* AWS Lambda
* IAM & Security Management
* Cloud Monitoring with CloudWatch
* Power BI Integration

---

## Future Enhancements

Potential improvements include:

* Workflow orchestration using Apache Airflow
* CI/CD deployment pipelines
* Infrastructure as Code using Terraform
* Data quality validation frameworks
* Real-time streaming ingestion
* Medallion Architecture implementation
* Automated dashboard refresh scheduling

---

## 🤝 Let's Connect!

If you found this project interesting, I'd love to connect and chat about Data Engineering, Data Analytics, and Business Intelligence.

* **Explore More:** This is just one part of my journey. Check out my [📂 Full Portfolio](https://github.com/JacobDaniel-82) to see my projects.
* **Professional Network:** Let's stay in touch on [💼 LinkedIn](https://www.linkedin.com/in/jacobdanielr) (I'm active here!).
* **Get in Touch:** Have a question or suggestion? Reach out via [📧 Email](mailto:jacobdanielr82@gmail.com)

*Designed and Engineered by **Jacob Daniel R** | 2026*

---

