<!-- # Real-Time Weather Big Data Pipeline

## Project Overview
This project implements an end-to-end real-time Big Data pipeline to ingest, process, store, and visualize weather data using distributed systems.

The pipeline uses Apache Kafka for real-time data ingestion, Apache Spark Structured Streaming running on YARN for stream processing, InfluxDB for time-series storage, and Grafana for monitoring and visualization.  
The system is deployed on a distributed cluster running on Azure Virtual Machines.

---

## Author Information
- **Name:** Abhilash  
- **Institution:** ESILV  
- **Course:** Big Data Distributed Systems  
- **Academic Year:** 2025–2026
 -->



 ---

## Project Objectives
The main objectives of this project are:

- To ingest real-time weather data continuously using Apache Kafka.
- To decouple data producers and consumers using a message-based streaming system.
- To process streaming data in near real time using Apache Spark Structured Streaming.
- To execute stream processing jobs on a distributed cluster managed by YARN.
- To store processed results in a time-series database (InfluxDB).
- To visualize real-time and historical weather metrics using Grafana dashboards.
- To demonstrate a complete distributed Big Data pipeline running on multiple nodes.

---

## System Architecture

### Logical Architecture
The pipeline follows a layered architecture where each component has a well-defined responsibility:

Weather API  
→ Kafka Producer (Python)  
→ Kafka Topic (`weather`)  
→ Spark Structured Streaming (running on YARN)  
→ InfluxDB (`weather_data`)  
→ Grafana Dashboard

### Component Responsibilities

- **Kafka Producer:** Fetches weather data and publishes JSON messages to Kafka.
- **Kafka Broker:** Buffers and streams real-time data reliably.
- **Spark Structured Streaming:** Consumes Kafka messages, processes them in micro-batches, and prepares structured output.
- **YARN:** Manages cluster resources and schedules Spark jobs.
- **InfluxDB:** Stores processed weather data as time-series records.
- **Grafana:** Visualizes metrics such as temperature, humidity, and wind speed.

### Worker Node (adm-mcsc@worker)

The following services are running on the worker node:

DataNode

NodeManager

This was verified using:

jps


This confirms that HDFS and YARN are running in distributed mode across multiple hosts.

How to Start Hadoop, Spark, and Kafka Services
Start Hadoop (HDFS)
start-dfs.sh

Start YARN
start-yarn.sh

Start Kafka (Executed on Master Node)
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties


Kafka service availability is verified using:

jps

How to Run Your Function

The implemented function demonstrates streaming data consumption using Kafka.

Kafka Topic Consumption

Kafka Console Consumer is used to consume weather data from the Kafka topic:

kafka-console-consumer.sh \
--bootstrap-server localhost:9092 \
--topic weather \
--from-beginning


The presence of ConsoleConsumer in the jps output confirms that the function is actively running.

Commands to Execute Your Pipeline or Job

Main execution command used in this project:

kafka-console-consumer.sh \
--bootstrap-server localhost:9092 \
--topic weather \
--from-beginning


This command validates real-time data ingestion through Kafka on the cluster.

Dependencies

The following software and versions are used in the project environment:

Component	Version
Operating System	Linux (Ubuntu)
Java	OpenJDK 11
Hadoop	3.x
Kafka	3.x
Spark	3.x
Python	3.8+

Additional Python libraries are listed in requirements.txt.

Monitoring
Hadoop & YARN Monitoring

YARN ResourceManager Web UI is used to monitor cluster resources:

http://<master-node-ip>:8088


This interface is used to verify active NodeManagers and resource utilization.

Grafana Monitoring

Grafana is used for cluster and system monitoring.

Access Grafana dashboard:

http://<grafana-ip>:3000


The dashboard displays system-level metrics such as memory usage and node status.

Demo Video Link

📌 To be added

(The final video will demonstrate the distributed cluster, service verification using jps, Kafka execution, YARN monitoring, and Grafana dashboard.)

License

MIT License

Author

**Abhilash Tarigopula**
**M2 Computer Science & Data Science**


 









