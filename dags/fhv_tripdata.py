from airflow import DAG
from airflow.decorators import task
from google.cloud import storage, bigquery
from pyspark.sql import SparkSession
from urllib.request import urlopen
from datetime import datetime
import sqlparse
import os

with DAG(dag_id='fhv_tripdata', start_date=datetime.now(), schedule='@once'):

    @task
    def remote_to_gcs():

        client = storage.Client()
        bucket = client.get_bucket('fhv_tripdata')

        file = urlopen('https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2021-02.parquet')
        blob = bucket.blob('fhv_tripdata_2021-02.parquet')

        blob.upload_from_string(file.read())

    @task
    def gcs_to_bigquery():

        client = bigquery.Client()
        dataset = client.dataset('fhv_tripdata')

        source_uris = 'gs://fhv_tripdata/fhv_tripdata_2021-02.parquet'
        table_ref = bigquery.TableReference(dataset, 'fhv_tripdata_2021-02')
        job_config = bigquery.LoadJobConfig(source_format='PARQUET', autodetect=True, write_disposition='WRITE_TRUNCATE')

        client.load_table_from_uri(source_uris, table_ref, job_config=job_config)

    @task
    def bigquery_with_spark():

        spark = SparkSession \
                .builder \
                .master('spark://spark:7077') \
                .appName('fhv_tripdata') \
                .config('spark.jars', 'spark-bigquery.jar') \
                .getOrCreate()
        
        for file in os.listdir('queries'):

            query = sqlparse.format(open(f'queries/{file}', 'r'))

            df = spark.read \
                .format('bigquery') \
                .option('viewsEnabled', 'true') \
                .option('materializationDataset', 'fhv_tripdata') \
                .load(query)

            df.write \
                .format('bigquery') \
                .mode('overwrite') \
                .option('writeMethod', 'direct') \
                .save('fhv_tripdata.' + file.split('.', 1)[0])

    remote_to_gcs() >> gcs_to_bigquery() >> bigquery_with_spark()