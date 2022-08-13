# How-to-build-streaming-data-pipelines


A step by step guide to building a highly scalable data streaming pipeline in Python.

Architecture


![image](https://user-images.githubusercontent.com/110036451/184506749-8fb2e303-815e-45cb-a0d5-47acc1c107ce.png)


Installation
Install the Redis and run it locally.

Clone the repository.

git clone https://github.com/Rameshei87/Data-Streaming-Pipeline.git
Install the requirements.

pip install -r requirements.txt

You are good to go!

Quick start

Start the producer quotes_spider:

cd producer

scrapy crawl quotes

Start the consumer quotes_consumer:

cd consumer
python quotes_consumer.py

See data flowing between pipeline as soon as data is generated from the producer.
