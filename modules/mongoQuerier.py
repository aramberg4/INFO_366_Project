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

	#create


	#read
	def find(self, queryDict):
		data = self.__collection.find(queryDict)
		return data

	def find_one(self, queryDict):
		data = self.__collection.find_one(queryDict)
		return data

	#update


	#delete
	def deleteOne(self, queryDict):
		data = self.__collection.delete_one(queryDict)

	def deleteMany(self, queryDict):
		data = self.__collection.delete_many(queryDict)
		print(data.deleted_count, " documents deleted.")

