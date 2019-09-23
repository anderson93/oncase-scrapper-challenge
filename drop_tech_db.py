from pymongo import MongoClient

client = MongoClient()
# Droppando a database
client.drop_database('tech_news')

client.close()