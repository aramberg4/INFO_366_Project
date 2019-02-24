# INFO_366_Project
Repo for Info 366 group project

# Github Repo
https://github.com/aramberg4/INFO_366_Project

# MongoDB
1. Install MongoDB:
https://www.mongodb.com/download-center/community
2. Add Mongo to your PATH:
https://www.youtube.com/watch?v=FwMwO8pXfq0

# Import data
Requirements:
1. Must have MongoDB installed
2. Must have Git repo cloned locally

1. Open up command prompt or terminal 
2. Run: mongod
3. Open up new command prompt or terminal 
4. Run: mongo
5. Run: use dnd
6. Open up new command prompt or terminal 
7. cd to ..\INFO_366_Project\data
8. Run: mongoimport --jsonArray --db dnd --collection spells --file spells.json

# Download PyMongo
Requirements:
1. Must have Python 3.x installed
2. Must have pip installed

1. Open up command prompt or terminal
2. Run: python -m pip install pymongo
