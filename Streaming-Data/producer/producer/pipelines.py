# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pipeline.redis_client import RedisClient


class ProducerPipeline:
    redis_client = RedisClient()

    def process_item(self, item, spider):
        self.redis_client.send_data_to_pipeline(item)
        return item
