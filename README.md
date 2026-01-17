# Real-Time Weather Big Data Pipeline

## Project Title and Description
This project implements an end-to-end Big Data pipeline deployed on a distributed cluster to ingest, process, and monitor weather data. The objective of the project is to demonstrate the use of core Big Data technologies such as Hadoop, Kafka, and monitoring tools running on multiple nodes (not locally).

The pipeline focuses on real-time data ingestion using Kafka, distributed storage and resource management using Hadoop (HDFS and YARN), and system monitoring using Grafana.

---

## Author Information
- Name: Abhilash Tarigopula
- Institution: ESILV
- Course: Big Data Distributed Systems
- Academic Year: 2025–2026

---

## Project Objectives
- Ingest weather data using Apache Kafka.
- Demonstrate a distributed Hadoop cluster using HDFS and YARN.
- Decouple data producers and consumers using a message-based streaming system.
- Validate real-time data flow through Kafka topics.
- Monitor cluster and system metrics using Grafana.
- Demonstrate a complete Big Data pipeline running on multiple nodes.

---

## Cluster Setup Instructions

The project is deployed on a distributed cluster consisting of one master node and one worker node.

### Master Node (adm-mcsc@master)
The following services are running on the master node:
- NameNode
- SecondaryNameNode
- ResourceManager
- NodeManager
- Kafka
- ConsoleConsumer

Verified using:
jps

### Worker Node (adm-mcsc@worker)
The following services are running on the worker node:
- DataNode
- NodeManager

Verified using:
jps

This confirms that HDFS and YARN are running in distributed mode across multiple hosts.

---

## How to Start Hadoop and Kafka Services

### Start Hadoop (HDFS)
start-dfs.sh

### Start YARN
start-yarn.sh

### Start Kafka (Executed on Master Node)
zookeeper-server-start.sh config/zookeeper.properties  
kafka-server-start.sh config/server.properties

Kafka service availability is verified using:
jps

---

## How to Run Your Function

The implemented function demonstrates streaming data consumption using Kafka.

### Kafka Topic Consumption
kafka-console-consumer.sh \
--bootstrap-server localhost:9092 \
--topic weather \
--from-beginning

The presence of ConsoleConsumer in the jps output confirms that the function is actively running.

---

## Commands to Execute Your Pipeline or Job
kafka-console-consumer.sh \
--bootstrap-server localhost:9092 \
--topic weather \
--from-beginning

This command validates real-time data ingestion through Kafka on the distributed cluster.

---

## Dependencies

Component | Version
--------- | --------
Operating System | Linux (Ubuntu)
Java | OpenJDK 11
Hadoop | 3.x
Kafka | 3.x
Spark | 3.x
Python | 3.8+

Additional Python libraries are listed in requirements.txt.

---

## Sample Data

A small sample dataset is provided to test the pipeline.

File location:
sample_data/weather_sample.json

This file contains example weather records and can be used to validate data ingestion without relying on live data sources.

---

## Monitoring

### Hadoop & YARN Monitoring
YARN ResourceManager Web UI:
http://<master-node-ip>:8088

### Grafana Monitoring
Grafana dashboard:
http://<grafana-ip>:3000

The dashboard displays system-level metrics such as memory usage and node status.

---

## Demo Video Link
To be added

---

## License
MIT License

---

## Author
Abhilash Tarigopula  
M2 Computer Science & Data Science
