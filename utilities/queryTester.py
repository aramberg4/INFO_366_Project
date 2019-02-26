import sys
sys.path.append("..")
from modules import mongoQuerier
from pprint import pprint

def main():
	queryDict = {'name':'Barkskin'}
	myMongo = mongoQuerier.MongoQuerier()
	cursor = myMongo.find(queryDict)
	for doc in cursor:
		pprint(doc)

if __name__ == "__main__":
	main()