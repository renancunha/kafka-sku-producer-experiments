# -*- coding: utf-8 -*-
import pkg_resources

from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

from experiments_producer.settings import KAFKA_SETTINGS

value_schema_str = pkg_resources.resource_string(
    "experiments_producer", "spiders/res/sku_schema.avsc"
).decode("utf8")

key_schema = avro.loads('{"type": "string"}')
value_schema = avro.loads(value_schema_str)


class KafkaProducerPipeline(object):
    def __init__(self, default_value=None):

        # create the kafka avro producer
        self.producer = AvroProducer({
                'bootstrap.servers': KAFKA_SETTINGS["bootstrap.servers"],
                'on_delivery': self.on_delivery,
                'schema.registry.url': KAFKA_SETTINGS["schema.registry.url"],
            }, default_key_schema=key_schema, default_value_schema=value_schema)

    def on_delivery(self, err, msg):
        if err is not None:
            print("Message delivery failed: {}".format(err))
        else:
            print("Message delivered to {} [{}]".format(msg.topic(), msg.partition()))

    def process_item(self, item, spider):
        value = dict(item)

        # produce the item at the "out_topic" topic
        self.producer.produce(topic=KAFKA_SETTINGS["out_topic"], value=value, key=value["name"])
        self.producer.flush()

        return item
