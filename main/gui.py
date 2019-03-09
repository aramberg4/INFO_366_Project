import tkinter as tkr
from pprint import pprint
import sys
sys.path.append("..")
from modules import mongoQuerier

#Construct a dropdown list component
def dropDown(window, optionList, selection, r, c):	
	menuSet = tkr.OptionMenu(window, selection, *optionList)
	menuSet.configure(font=("Arial",14))
	menuSet.grid(row=r, column=c)
	return selection

#Submit button
def submit():
	#Add vars to query dictionary
	qd = {}
	if characterClass.get() is not '':
		qd['classes'] = {'$elemMatch':{'name':characterClass.get()}}
	if level.get() is not '':
		qd['level'] = level.get()

	try:
		myMongo = mongoQuerier.MongoQuerier()
		cursor = myMongo.find(qd)
		for doc in cursor:
			pprint(doc)
	except Exception as e:
		print("Error:" + str(e))

window = tkr.Tk()
window.title("5e Spells")
window.geometry("800x600")
#qd = {}

#Class dropdown
classList = ['Wizard', 'Fighter', 'Rogue', 'Cleric']
characterClass = tkr.StringVar()
classDropDown = dropDown(window, classList, characterClass, 1, 0)

#Level dropdown
levelList = []
for i in range(1,10):
	levelList.append(i)	
level = tkr.IntVar()
levelDropDown = dropDown(window, levelList, level, 1, 1)

#School dropdown


button = tkr.Button(window, text="Submit", command=submit)
button.grid(row=2, column=0)

window.mainloop()