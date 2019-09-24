# -*- coding: utf-8 -*-
import pymongo

class MongoConnector(object):

    def __init__(self, uri, database):
        self.mongo_uri = uri
        self.mongo_db = database or 'tech_news'

    def get_collection(self, collection):
        self.client = pymongo.MongoClient(self.mongo_uri)
        return self.client[self.mongo_db][collection]

    def close_connection(self):
        self.client.close()