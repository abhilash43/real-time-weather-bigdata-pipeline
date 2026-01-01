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
