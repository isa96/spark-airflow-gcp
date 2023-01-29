### Data Pipeline with Apache Spark, Apache Airflow, Google Cloud Plaform, and Docker

The example dataset is a record of trips made by for-hire vehicle (FHV) that have been recorded and provided to the TLC since 2015.
This project contains scripts that help you to load the example dataset from data sources to your Google BigQuery.
It will run four SQL scripts that query data from Google BigQuery and load the results into Google BigQuery.
The query jobs will be done by Apache Spark and scheduled by Apache Airflow. 
All required tools and dependencies are compiled into the bash script and Docker Compose file.

##### Clone this repository and enter the directory
```bash
git clone https://github.com/isa96/spark-airflow-gcp-docker && cd spark-airflow-gcp-docker
```

##### Create a file named "service-account.json" containing your Google service account credentials
```json
{
  "type": "service_account",
  "project_id": "[PROJECT_ID]",
  "private_key_id": "[KEY_ID]",
  "private_key": "-----BEGIN PRIVATE KEY-----\n[PRIVATE_KEY]\n-----END PRIVATE KEY-----\n",
  "client_email": "[SERVICE_ACCOUNT_EMAIL]",
  "client_id": "[CLIENT_ID]",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/[SERVICE_ACCOUNT_EMAIL]"
}
```

##### Create big data tools stack with Docker Compose
```bash
sudo docker compose up -d
```

##### Open Spark to monitor Spark master and Spark workers
```bash
localhost:8080
```

##### Open Airflow with username and password "airflow" to run the DAG
```bash
localhost:8090
```