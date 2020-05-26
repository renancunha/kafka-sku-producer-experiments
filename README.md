# Kafka SKU Producer - Experiments

This repository contains the source code of a Scrapy project that yields product data scraped from walmart.com. It also has
an item pipeline that connects to a Kafka broker and produces the SKU items in a pre-defined Kafka topic.

## Kafka settings

You should set up the Kafka settings at the project ``settings.py``.

````
KAFKA_SETTINGS = {
    "bootstrap.servers": "localhost:9092",
    "schema.registry.url": "http://localhost:8081",
    "out_topic": "scraped-products"
}
````

## Avro schema

The Avro schema that is used to serialize/deserialize the items is located at ``experiments_producer/spiders/res/sku_schema.avsc``.
