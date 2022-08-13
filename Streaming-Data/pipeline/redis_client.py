import json

import redis


class RedisClient:
    """
    Custom Redis client with all the wrapper funtions. This client implements FIFO for pipeline.
    """
    connection = redis.Redis(host='localhost', port=6379, db=0)
    key = 'DATA-PIPELINE-KEY'

    def _convert_data_to_json(self, data):
        try:
            return json.dumps(data)
        except Exception as e:
            print(f'Failed to convert data into json with error: {e}')
            raise e

    def _convert_data_from_json(self, data):
        try:
            return json.loads(data)
        except Exception as e:
            print(f'Failed to convert data from json to dict with error: {e}')
            raise e

    def send_data_to_pipeline(self, data):
        data = self._convert_data_to_json(data)
        self.connection.lpush(self.key, data)

    def get_data_from_pipeline(self):
        try:
            data = self.connection.rpop(self.key)
            return self._convert_data_from_json(data)
        except Exception as e:
            print(f'Failed to get more data from pipeline with error: {e}')

    def get_items_in_pipeline(self):
        return self.connection.llen(self.key)
