# -*- coding: utf-8 -*-
import pkg_resources
import scrapy
import json

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy_jsonschema.item import JsonSchemaItem

json_schema_str = pkg_resources.resource_string(
    "experiments_producer", "spiders/res/sku_schema.json"
).decode("utf8")


class WalmartGamesItem(JsonSchemaItem):
    jsonschema = json.loads(json_schema_str)


class WalmartGamesItemLoader(ItemLoader):
    default_item_class = WalmartGamesItem
    default_output_processor = TakeFirst()


class WalmartGamesSpider(scrapy.Spider):
    name = "walmart.com"
    start_urls = ["http://www.google.com"]

    def parse(self, response):
        data_path = pkg_resources.resource_string(
            "experiments_producer", "spiders/res/walmart_data.json"
        ).decode("utf8")
        data = json.loads(data_path)
        for result in data:
            yield result