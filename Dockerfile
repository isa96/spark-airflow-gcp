FROM apache/airflow:latest
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
USER root
RUN apt update -y
RUN apt upgrade -y
RUN apt install default-jdk -y
RUN apt install git -y
USER airflow
RUN pip install pyspark