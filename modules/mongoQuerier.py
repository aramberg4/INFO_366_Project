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

	###CRUD Methods###

	#create

	# purpose: insert one document to collection
	# doc:     dictionary representing BSON document
	def insertOne(self, doc):
		self.__collection.insert_one(doc)

	# purpose: insert multiple documents to collection at the same time
	# docList: list of dictionaries representing BSON documents
	def insertMany(self, doclist):
		self.__collection.insert_many(docList)

	#read

	# purpose:   find one document
	# queryDict: dictionary for query filter
	def findOne(self, queryDict):
		data = self.__collection.find_one(queryDict)
		return data

	# purpose:   find documents
	# queryDict: dictionary for query filter
	def find(self, queryDict):
		data = self.__collection.find(queryDict)
		return data

	#update

	# purpose: 	 update one document
	# queryDict: dictionary for query filter
	# setDict: 	 dictionary with fields/values to be changed
	# upsert:    boolean
	def updateOne(self, queryDict, setDict, upsert):
		self.__collection.update_one(queryDict, setDict, upsert)

	# purpose: 	 update many documents at the same time
	# queryDict: dictionary for query filter
	# setDict: 	 dictionary with fields/values to be changed
	# upsert:    boolean
	def updateMany(self, queryDict, setDict, upsert):
		self.__collection.update_many(queryDict, setDict, upsert)


	#delete

	# purpose: 	 delete one document
	# queryDict: dictionary for query filter
	def deleteOne(self, queryDict):
		data = self.__collection.delete_one(queryDict)

	# purpose: 	 delete many documents at the same time
	# queryDict: dictionary for query filter
	def deleteMany(self, queryDict):
		data = self.__collection.delete_many(queryDict)
		print(data.deleted_count, " documents deleted.")

