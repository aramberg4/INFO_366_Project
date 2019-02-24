import pymongo

class MongoQuerier():
	def __init__(self):
		self.__client = pymongo.MongoClient("localhost", 27017)
		self.__db = self.__client['dnd']
		self.__collection = self.__db['spells']

	#getters
	def getClient(self):
		return slef.__client

	def getDb(self):
		return self.__db

	def getCollection(self):
		return self.__collection

	#setters

	#query methods

	def find(self, queryString):
		data = self.__collection.find({queryString})
		return data