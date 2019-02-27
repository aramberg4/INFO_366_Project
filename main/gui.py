import tkinter as tkr
from pprint import pprint

#Construct a dropdown list component
def dropDown(window, optionList, selection, r, c):	
	menuSet = tkr.OptionMenu(window, selection, *optionList)
	menuSet.configure(font=("Arial",14))
	menuSet.grid(row=r, column=c)
	return selection

#Submit button
def submit():
	#Add vars to query dictionary
	qd = {
		'class':characterClass.get(),
		'level':level.get()
	}
	for k in qd:
		print(k +": "+ qd[k])
	#print ("value is "+ input.get())

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
	levelList.append(str(i))	
level = tkr.StringVar()
levelDropDown = dropDown(window, levelList, level, 1, 1)

#School dropdown


button = tkr.Button(window, text="Submit", command=submit)
button.grid(row=2, column=0)

window.mainloop()