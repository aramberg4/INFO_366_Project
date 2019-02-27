import sys
sys.path.append("..")
from modules import mongoQuerier
from pprint import pprint

def main():
	#queryDict = {'classes':{'name':'Wizard', 'url': 'http://www.dnd5eapi.co/api/classes/12'}}
	#queryDict = {'classes':{'$elemMatch':{'name':'Wizard'}}}
	queryDict = {
		'classes':{'$elemMatch':{'name':'Wizard'}},
		'level':1
	}
	#queryDict = {'level': 1}
	myMongo = mongoQuerier.MongoQuerier()
	cursor = myMongo.find(queryDict)
	for doc in cursor:
		pprint(doc)

if __name__ == "__main__":
	main()