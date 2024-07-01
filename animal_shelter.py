import os
from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        self.user = os.getenv('MONGODB_USER', 'aacuser')
        self.password = os.getenv('MONGODB_PASS', 'your_password_here')
        self.host = os.getenv('MONGODB_HOST', 'nv-desktop-services.apporto.com')
        self.port = int(os.getenv('MONGODB_PORT', 30976))
        self.db = os.getenv('MONGODB_DB', 'AAC')
        self.collection_name = os.getenv('MONGODB_COLLECTION', 'animals')

        # Initialize Connection
        self.client = MongoClient(f'mongodb://{self.user}:{self.password}@{self>
        self.database = self.client[self.db]
        self.collection = self.database[self.collection_name]

    def create(self, data):
	""" Insert a document into the collection """
        if data:
            try:
                insert_result = self.collection.insert_one(data)
                return insert_result.acknowledged
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        """ Query for documents in the collection """
        if query:
            try:
                cursor = self.collection.find(query)
                results = [document for document in cursor]
                return results
            except Exception as e:
            print(f"An error occurred: {e}")
                return []
        else:
            raise Exception("Query parameter is empty")

    def update(self, query, new_values):
        """ Update a document in the collection """
        if query and new_values:
            try:
                update_result = self.collection.update_one(query, {'$set': new_>
                return update_result.modified_count > 0
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise Exception("Query and new_values parameters are required")

    def delete(self, query):
        """ Delete a document from the collection """
        if query:
            try:
                delete_result = self.collection.delete_one(query)
                return delete_result.deleted_count > 0
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise Exception("Query parameter is required")


