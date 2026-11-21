# restaurant-kitchen-monitoring# Restaurant Kitchen Monitoring

This project monitors live order processing and preparation performance inside high-volume commercial kitchens and restaurant chains.

The pipeline collects order events, cleans and transforms them using Apache NiFi, analyzes them in real time using Apache Spark Streaming, stores the results in PostgreSQL, and displays them in a dashboard.

## Project Pipeline

Producer → Kafka → NiFi → Kafka → Spark Streaming → PostgreSQL → Dashboard

## Project Components

- Kafka
- Apache NiFi
- Apache Spark Streaming
- PostgreSQL
- Dashboard

## Dataset

The dataset used in this project is the Food Delivery Order History Data from Kaggle.

Dataset source:  
https://www.kaggle.com/datasets/sujalsuthar/food-delivery-order-history-data/versions/1

The cleaned dataset is stored in:

data/food_delivery_orders_cleaned.csv

## Data Cleaning

The raw dataset was cleaned and prepared before being used in the pipeline.

The following columns were added:

- menu_category
- kitchen_station
- prep_started_at
- prep_completed_at

The preparation time is based on the column:

KPT duration (minutes)

## Kafka Topics

The project uses the following Kafka topics:

- kitchen-orders-raw
- kitchen-orders-cleaned
- kitchen-alerts

## NiFi Role

Apache NiFi is used as the ETL layer.

It performs the following tasks:

- Consumes raw events from Kafka
- Validates JSON data
- Cleans and normalizes fields
- Adds missing fields such as menu_category and kitchen_station
- Publishes cleaned events to another Kafka topic

## Spark Role

Apache Spark Streaming is used for real-time analytics.

It performs the following tasks:

- Consumes cleaned events from Kafka
- Calculates preparation duration
- Calculates average preparation time per menu category
- Calculates real-time queue length for each kitchen station
- Determines kitchen station status
- Generates alerts when preparation time exceeds the service-level limit
- Stores results in PostgreSQL

## Database

PostgreSQL is used to store processed data and alerts.

The main tables are:

- orders
- order_events
- kitchen_station_metrics
- prep_time_alerts

## Dashboard

The dashboard displays:

- Average preparation time per menu category
- Real-time queue length per kitchen station
- Kitchen station status
- Alerts for delayed orders

## Project Structure

restaurant-kitchen-monitoring/
├── data/
│   └── food_delivery_orders_cleaned.csv
├── producer/
│   ├── producer.py
│   └── requirements.txt
├── nifi-flow/
│   ├── nifi_flow_template.xml
│   └── README.txt
├── spark-job/
│   ├── streaming_job.py
│   └── requirements.txt
├── database/
│   ├── init.sql
│   └── README.txt
├── dashboard/
│   ├── app.py
│   └── requirements.txt
├── docker-compose.yaml
├── README.md
└── .gitignore

## How to Run

1. Install Docker Desktop.

2. Start the project:

docker compose up -d

3. Check running containers:

docker compose ps

4. Run the Kafka producer:

cd producer  
pip install -r requirements.txt  
python producer.py

5. Open NiFi:

https://localhost:8443/nifi

6. Open Kafka UI:

http://localhost:8080

7. Open Spark UI:

http://localhost:4040

8. Open PostgreSQL:

localhost:5432

## Team Roles

- Data Source / Kafka Producer: Reads the cleaned dataset and sends order events to Kafka.
- NiFi ETL: Consumes raw events, cleans and transforms them, then publishes cleaned events.
- Spark Streaming: Performs real-time analytics, queue tracking, and alert generation.
- Database / PostgreSQL: Stores processed results and alerts.
- Dashboard: Displays KPIs and alerts.
- DevOps / Docker: Manages Docker Compose, containers, and project deployment.

## Important Notes

- The Producer sends raw events to Kafka.
- NiFi performs ETL and sends cleaned events to another Kafka topic.
- Spark consumes cleaned events and performs analytics.
- Spark calculates preparation duration, average preparation time, queue length, station status, and alerts.
- PostgreSQL stores the final results.
- The dashboard displays the results.

## Requirements

- Docker Desktop
- Python 3.10 or later
- Kafka
- Apache NiFi
- Apache Spark
- PostgreSQL
