# This file is deprecated after switching to new dataset
import json
from pprint import pprint
import csv
import pymongo

def main():
    #files
    jsonFile = 'C:\\Users\\Ausbo\\Documents\\GitHub\\5e-spells\\spells.json'
    csvfile = 'C:\\Users\\Ausbo\\Documents\\GitHub\\5e-spells\\spellsAndClasses.csv'
    #initialize dictionary of class lists for each spell
    d = dict()

    #read in csv file
    with open(csvFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        #for spell in excel file, look at  value in class column and add to the appropriate list
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                spellName = row[0]
                spellClass = row[1]
                if spellName in d:
                    d[spellName].append(spellClass)
                else:
                    d[spellName] = [spellClass]
    print(f'Processed {line_count} lines.')
    print('Here is what the dictionary looks like: ')
    for entry in d:
        print(entry + ':')
        for c in d[entry]:
            print(c)

    #Connect to MongoDB with Pymongo
    client = pymongo.MongoClient("localhost", 27017)
    db = client.dnd
    collection_spells = db['spells']

    #Create colletion with json file
    with open(jsonFile) as f:
        file_data = json.load(f)
    collection_spells.insert(file_data)

    #Add new class field to each document with list as value
    for key in d:
      db.spells.updateOne(
        {name:key},
        {$set:{"classes":d{key}}}
      )  

    client.close()

if __name__ == "__main__":
    main()