# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ausbo\Documents\GitHub\INFO_366_Project\main\gui-pyqt5.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, QObject, pyqtSignal
from PyQt5.QtWidgets import *
import sys
sys.path.append("..")
from modules import mongoQuerier
from pprint import pprint
from window_addspell import Ui_windowAdd
from window_editspell import Ui_windowEdit

class Ui_windowMain(QObject):
    editSpellInfo = pyqtSignal(dict)

    def setupUi(self, windowMain):
        windowMain.setObjectName("windowMain")
        windowMain.resize(1920, 1010)
        windowMain.setMaximumSize(QtCore.QSize(1980, 16777215))
        #background
        oImage = QImage("background.jpg")
        sImage = oImage.scaled(QSize(1920,1010))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))    # 10 = Windowrole
        windowMain.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(windowMain)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 1861, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelClasses = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelClasses.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelClasses.setObjectName("labelClasses")
        self.gridLayout.addWidget(self.labelClasses, 3, 4, 1, 1)
        self.labelConcentration = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelConcentration.setMinimumSize(QtCore.QSize(130, 0))
        self.labelConcentration.setMaximumSize(QtCore.QSize(135, 20))
        self.labelConcentration.setObjectName("labelConcentration")
        self.gridLayout.addWidget(self.labelConcentration, 3, 5, 1, 1)
        self.filterComponents = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterComponents.sizePolicy().hasHeightForWidth())
        self.filterComponents.setSizePolicy(sizePolicy)
        self.filterComponents.setMaximumSize(QtCore.QSize(125, 16777215))
        self.filterComponents.setObjectName("filterComponents")
        self.filterComponents.addItem("")
        self.filterComponents.setItemText(0, "")
        self.filterComponents.addItem("")
        self.filterComponents.addItem("")
        self.filterComponents.addItem("")
        self.gridLayout.addWidget(self.filterComponents, 4, 7, 1, 1)
        self.buttonClear = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonClear.sizePolicy().hasHeightForWidth())
        self.buttonClear.setSizePolicy(sizePolicy)
        self.buttonClear.setMinimumSize(QtCore.QSize(100, 0))
        self.buttonClear.setObjectName("buttonClear")
        self.gridLayout.addWidget(self.buttonClear, 4, 8, 1, 1)
        self.buttonSubmit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buttonSubmit.setObjectName("buttonSubmit")
        self.gridLayout.addWidget(self.buttonSubmit, 4, 9, 1, 1)
        self.labelSchool = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelSchool.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelSchool.setObjectName("labelSchool")
        self.gridLayout.addWidget(self.labelSchool, 3, 3, 1, 1)
        self.labelRitual = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelRitual.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelRitual.setObjectName("labelRitual")
        self.gridLayout.addWidget(self.labelRitual, 3, 6, 1, 1)
        self.labelComponents = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelComponents.sizePolicy().hasHeightForWidth())
        self.labelComponents.setSizePolicy(sizePolicy)
        self.labelComponents.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelComponents.setObjectName("labelComponents")
        self.gridLayout.addWidget(self.labelComponents, 3, 7, 1, 3)
        self.buttonAddSpell = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buttonAddSpell.setObjectName("buttonAddSpell")
        self.buttonAddSpell.clicked.connect(self.addSpell)
        self.gridLayout.addWidget(self.buttonAddSpell, 1, 9, 1, 1)
        self.filterName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterName.sizePolicy().hasHeightForWidth())
        self.filterName.setSizePolicy(sizePolicy)
        self.filterName.setMinimumSize(QtCore.QSize(130, 0))
        self.filterName.setMaximumSize(QtCore.QSize(500, 16777215))
        self.filterName.setObjectName("filterName")
        self.gridLayout.addWidget(self.filterName, 4, 0, 1, 1)
        self.filterRitual = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterRitual.sizePolicy().hasHeightForWidth())
        self.filterRitual.setSizePolicy(sizePolicy)
        self.filterRitual.setMaximumSize(QtCore.QSize(60, 16777215))
        self.filterRitual.setObjectName("filterRitual")
        self.filterRitual.addItem("")
        self.filterRitual.setItemText(0, "")
        self.filterRitual.addItem("")
        self.filterRitual.addItem("")
        self.gridLayout.addWidget(self.filterRitual, 4, 6, 1, 1)
        self.filterRange = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterRange.sizePolicy().hasHeightForWidth())
        self.filterRange.setSizePolicy(sizePolicy)
        self.filterRange.setMaximumSize(QtCore.QSize(125, 16777215))
        self.filterRange.setObjectName("filterRange")
        self.filterRange.addItem("")
        self.filterRange.setItemText(0, "")
        self.filterRange.addItem("")
        self.filterRange.addItem("")
        self.filterRange.addItem("")
        self.filterRange.addItem("")
        self.gridLayout.addWidget(self.filterRange, 4, 2, 1, 1)
        self.labelRange = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelRange.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelRange.setObjectName("labelRange")
        self.gridLayout.addWidget(self.labelRange, 3, 2, 1, 1)
        self.labelName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelName.setObjectName("labelName")
        self.gridLayout.addWidget(self.labelName, 3, 0, 1, 1)
        self.labelLevel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelLevel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelLevel.setObjectName("labelLevel")
        self.gridLayout.addWidget(self.labelLevel, 3, 1, 1, 1)
        self.filterClass = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterClass.sizePolicy().hasHeightForWidth())
        self.filterClass.setSizePolicy(sizePolicy)
        self.filterClass.setMaximumSize(QtCore.QSize(125, 16777215))
        self.filterClass.setObjectName("filterClass")
        self.filterClass.addItem("")
        self.filterClass.setItemText(0, "")
        self.filterClass.addItem("")
        self.filterClass.addItem("")
        self.filterClass.addItem("")
        self.filterClass.addItem("")
        self.filterClass.addItem("")
        self.filterClass.addItem("")
        self.filterClass.addItem("")
        self.filterClass.addItem("")
        self.gridLayout.addWidget(self.filterClass, 4, 4, 1, 1)
        self.filterConcentration = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterConcentration.sizePolicy().hasHeightForWidth())
        self.filterConcentration.setSizePolicy(sizePolicy)
        self.filterConcentration.setMinimumSize(QtCore.QSize(130, 0))
        self.filterConcentration.setMaximumSize(QtCore.QSize(135, 16777215))
        self.filterConcentration.setObjectName("filterConcentration")
        self.filterConcentration.addItem("")
        self.filterConcentration.setItemText(0, "")
        self.filterConcentration.addItem("")
        self.filterConcentration.addItem("")
        self.gridLayout.addWidget(self.filterConcentration, 4, 5, 1, 1)
        self.filterSchool = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterSchool.sizePolicy().hasHeightForWidth())
        self.filterSchool.setSizePolicy(sizePolicy)
        self.filterSchool.setMinimumSize(QtCore.QSize(130, 0))
        self.filterSchool.setMaximumSize(QtCore.QSize(135, 16777215))
        self.filterSchool.setObjectName("filterSchool")
        self.filterSchool.addItem("")
        self.filterSchool.setItemText(0, "")
        self.filterSchool.addItem("")
        self.filterSchool.addItem("")
        self.filterSchool.addItem("")
        self.filterSchool.addItem("")
        self.filterSchool.addItem("")
        self.filterSchool.addItem("")
        self.filterSchool.addItem("")
        self.filterSchool.addItem("")
        self.gridLayout.addWidget(self.filterSchool, 4, 3, 1, 1)
        self.filterLevel = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterLevel.sizePolicy().hasHeightForWidth())
        self.filterLevel.setSizePolicy(sizePolicy)
        self.filterLevel.setMinimumSize(QtCore.QSize(50, 0))
        self.filterLevel.setMaximumSize(QtCore.QSize(40, 16777215))
        self.filterLevel.setObjectName("filterLevel")
        self.filterLevel.addItem("")
        self.filterLevel.setItemText(0, "")
        self.filterLevel.addItem("")
        self.filterLevel.addItem("")
        self.filterLevel.addItem("")
        self.filterLevel.addItem("")
        self.filterLevel.addItem("")
        self.filterLevel.addItem("")
        self.filterLevel.addItem("")
        self.filterLevel.addItem("")
        self.filterLevel.addItem("")
        self.filterLevel.addItem("")
        self.gridLayout.addWidget(self.filterLevel, 4, 1, 1, 1)
        self.labelMongoDD = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelMongoDD.setMinimumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelMongoDD.setFont(font)
        self.labelMongoDD.setObjectName("labelMongoDD")
        self.gridLayout.addWidget(self.labelMongoDD, 1, 0, 1, 1)

        # Edit and delete spell buttons
        self.layoutOptionsWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.layoutOptionsWidget.setObjectName("layoutOptionsWidget")
        self.layoutOptions = QtWidgets.QGridLayout(self.layoutOptionsWidget)
        self.layoutOptions.setContentsMargins(0, 0, 0, 0)
        self.layoutOptions.setObjectName("layoutOptions")

        self.buttonEditSpell = QPushButton(self.layoutOptionsWidget)
        self.buttonEditSpell.clicked.connect(self.editSpell)
        self.buttonEditSpell.setEnabled(False)

        self.editWindow = QtWidgets.QMainWindow()
        self.editUI = Ui_windowEdit()
        self.editUI.setupUi(self.editWindow)
        self.editSpellInfo.connect(self.editUI.loadSpell)

        self.buttonDeleteSpell = QPushButton(self.layoutOptionsWidget)
        self.buttonDeleteSpell.clicked.connect(self.deleteSpell)
        self.buttonDeleteSpell.setEnabled(False)

        self.msgBoxConfirmDelete = QMessageBox()
        self.msgBoxConfirmDelete.addButton('Yes', QMessageBox.AcceptRole)
        self.msgBoxConfirmDelete.addButton('No', QMessageBox.RejectRole)

        self.layoutOptions.addWidget(self.buttonEditSpell, 0, 0, 1, 1)
        self.layoutOptions.addWidget(self.buttonDeleteSpell, 0, 1, 1, 1)

        self.gridLayout.addWidget(self.layoutOptionsWidget, 5, 9, 1, 1)

        # Spell selection table
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 230, 660, 771))
        self.tableWidget.setObjectName("spellTable")

        # Spell details
        self.spellBox = QtWidgets.QTextEdit(self.centralwidget)
        self.spellBox.setGeometry(QtCore.QRect(770, 230, 1121, 771))
        self.spellBox.setObjectName("spellBox")
        self.spellBox.setReadOnly(True)

        windowMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        windowMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(windowMain)
        self.statusbar.setObjectName("statusbar")
        windowMain.setStatusBar(self.statusbar)

        self.retranslateUi(windowMain)
        QtCore.QMetaObject.connectSlotsByName(windowMain)

    def retranslateUi(self, windowMain):
        _translate = QtCore.QCoreApplication.translate
        windowMain.setWindowTitle(_translate("windowMain", "MongoD&D"))
        self.labelClasses.setText(_translate("windowMain", "Classes"))
        self.labelConcentration.setText(_translate("windowMain", "Concentration"))
        self.filterComponents.setItemText(1, _translate("windowMain", "V"))
        self.filterComponents.setItemText(2, _translate("windowMain", "S"))
        self.filterComponents.setItemText(3, _translate("windowMain", "M"))
        self.buttonClear.setText(_translate("windowMain", "Clear Filters"))
        self.buttonSubmit.setText(_translate("windowMain", "Submit"))
        self.labelSchool.setText(_translate("windowMain", "School"))
        self.labelRitual.setText(_translate("windowMain", "Ritual"))
        self.labelComponents.setText(_translate("windowMain", "Components"))
        self.buttonAddSpell.setText(_translate("windowMain", "+ Add Spell"))
        self.filterRitual.setItemText(1, _translate("windowMain", "yes"))
        self.filterRitual.setItemText(2, _translate("windowMain", "no"))
        self.filterRange.setItemText(1, _translate("windowMain", "Self"))
        self.filterRange.setItemText(2, _translate("windowMain", "Touch"))
        self.filterRange.setItemText(3, _translate("windowMain", "Sight"))
        self.filterRange.setItemText(4, _translate("windowMain", "Special"))
        self.labelRange.setText(_translate("windowMain", "Range"))
        self.labelName.setText(_translate("windowMain", "Name"))
        self.labelLevel.setText(_translate("windowMain", "Level"))
        self.filterClass.setItemText(1, _translate("windowMain", "Bard"))
        self.filterClass.setItemText(2, _translate("windowMain", "Cleric"))
        self.filterClass.setItemText(3, _translate("windowMain", "Druid"))
        self.filterClass.setItemText(4, _translate("windowMain", "Paladin"))
        self.filterClass.setItemText(5, _translate("windowMain", "Ranger"))
        self.filterClass.setItemText(6, _translate("windowMain", "Sorcerer"))
        self.filterClass.setItemText(7, _translate("windowMain", "Warlock"))
        self.filterClass.setItemText(8, _translate("windowMain", "Wizard"))
        self.filterConcentration.setItemText(1, _translate("windowMain", "yes"))
        self.filterConcentration.setItemText(2, _translate("windowMain", "no"))
        self.filterSchool.setItemText(1, _translate("windowMain", "Abjuration"))
        self.filterSchool.setItemText(2, _translate("windowMain", "Conjuration"))
        self.filterSchool.setItemText(3, _translate("windowMain", "Divination"))
        self.filterSchool.setItemText(4, _translate("windowMain", "Enchantment"))
        self.filterSchool.setItemText(5, _translate("windowMain", "Evocation"))
        self.filterSchool.setItemText(6, _translate("windowMain", "Illusion"))
        self.filterSchool.setItemText(7, _translate("windowMain", "Necromancy"))
        self.filterSchool.setItemText(8, _translate("windowMain", "Transmutation"))
        self.filterLevel.setItemText(1, _translate("windowMain", "0"))
        self.filterLevel.setItemText(2, _translate("windowMain", "1"))
        self.filterLevel.setItemText(3, _translate("windowMain", "2"))
        self.filterLevel.setItemText(4, _translate("windowMain", "3"))
        self.filterLevel.setItemText(5, _translate("windowMain", "4"))
        self.filterLevel.setItemText(6, _translate("windowMain", "5"))
        self.filterLevel.setItemText(7, _translate("windowMain", "6"))
        self.filterLevel.setItemText(8, _translate("windowMain", "7"))
        self.filterLevel.setItemText(9, _translate("windowMain", "8"))
        self.filterLevel.setItemText(10, _translate("windowMain", "9"))
        self.labelMongoDD.setText(_translate("windowMain", "Mongo D&D"))
        #Make labels white
        self.labelMongoDD.setStyleSheet('color: white;'
                                        'font: 24pt "Arial";'
                                        'font-weight: bold;'
                                            )
        self.labelName.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelLevel.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelRange.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelSchool.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelClasses.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelConcentration.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelRitual.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelComponents.setStyleSheet('color: white;''font-weight: bold;')
        #spellBox style
        self.spellBox.setStyleSheet('background-color: rgb(0, 0, 0, 99);'
                                     'border-color: rgb(18, 18, 18);'
                                     'color: rgb(255, 255, 255);'
                                     'font: 16pt "Arial";'
                                     'padding: 16px;'
                                        )

        self.buttonEditSpell.setText(_translate("windowMain", "Edit Spell"))
        self.buttonDeleteSpell.setText(_translate("windowMain", "Delete Spell"))

        self.msgBoxConfirmDelete.setText('Please confirm:')
        self.msgBoxConfirmDelete.setInformativeText('Are you sure you want to delete this spell?')
        self.msgBoxConfirmDelete.setWindowTitle('Mongo D&D')

        self.buttonSubmit.clicked.connect(self.submitQuery)
        self.tableWidget.cellClicked.connect(self.populateSpellBox)
        self.buttonClear.clicked.connect(self.clearFilters)

    def submitQuery(self):
        print('class:' + '\'' + self.filterClass.currentText() + '\'')
        #Add vars to query dictionary
        self.qd = {}
        if self.filterName.text() is not '':
            self.qd['name'] = { '$regex': self.filterName.text(), '$options': 'i' }
        if self.filterLevel.currentText() is not '':
            self.qd['level'] = int(self.filterLevel.currentText())
        if self.filterRange.currentText() is not '':
            self.qd['range'] = self.filterRange.currentText()
        if self.filterSchool.currentText() is not '':
            self.qd['school.name'] = self.filterSchool.currentText()
        if self.filterClass.currentText() is not '':
            print('class:' + '\'' + self.filterClass.currentText() + '\'')
            self.qd['classes'] = {'$elemMatch':{'name': self.filterClass.currentText()}}
            print('added classes to query')
        if self.filterConcentration.currentText() is not '':
            self.qd['concentration'] = self.filterConcentration.currentText()
        if self.filterRitual.currentText() is not '':
            self.qd['ritual'] = self.filterRitual.currentText()
        if self.filterComponents.currentText() is not '':
            self.qd['components'] = self.filterComponents.currentText()

        print('Attempting query...')

        print('Instantiating MongoQuerier...')
        self.mq = mongoQuerier.MongoQuerier()
        print('Executing query...')
        self.cursor = self.mq.find(self.qd)
        print(self.cursor)
        print('Printing query...')
        #for doc in self.cursor:
        #    pprint(doc)
        self.populateTable()

    def populateTable(self):
        # Populate table
        self.tableWidget.setRowCount(self.cursor.count())
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Level', 'School', 'Components', 'Concentration', 'Ritual'])
        i = 0
        for doc in self.cursor:
            print('name: ' + doc["name"])
            self.tableWidget.setItem(i,0, QTableWidgetItem(str(doc['name'])))
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(doc['level'])))
            self.tableWidget.setItem(i,2, QTableWidgetItem(doc['school']['name']))
            components = str(doc['components']).replace('\'', '').replace('[', '').replace(']', '')
            self.tableWidget.setItem(i,3, QTableWidgetItem(components))
            self.tableWidget.setItem(i,4, QTableWidgetItem(str(doc['concentration'])))
            self.tableWidget.setItem(i,5, QTableWidgetItem(str(doc['ritual'])))
            i += 1

    def populateSpellBox(self, row, column):
        #self.cursor.rewind()
        self.spellBox.clear()
        item = self.tableWidget.item(row, column)
        print(str(row) + ',' + str(column))
        print(item.text())
        if column == 0:
            self.buttonEditSpell.setEnabled(True)
            self.buttonDeleteSpell.setEnabled(True)

            spellName = item.text()
            spell = self.mq.findOne({'name': spellName})           
            cleanDesc = str(spell['desc']).replace('[', '')
            cleanDesc = cleanDesc.replace(']', '')
            cleanDesc = cleanDesc.replace('\'', '')
            cleanDesc = cleanDesc.replace('â€™','\'')
            self.spellBox.setHtml(
                '<h3>' + str(spell["name"]) + '</h3>' + '<br />' 
                + '<b>Level</b> ' + str(spell['level']) +' '+ spell['school']['name'] + '<br />' 
                + '<b>Casting Time:</b> ' +str(spell['casting_time']) + '<br />' 
                + '<b>Range:</b> ' +str(spell['range']) + '<br />' 
                + '<b>Components:</b> '+ ', '.join(spell['components']) + '<br />' 
                + '<b>Duration:</b> ' + str(spell['duration']) + '<br /><br />'
                + '<b>Description:</b> ' + cleanDesc + '<br />'
                )
        else:
            self.buttonEditSpell.setEnabled(False)
            self.buttonDeleteSpell.setEnabled(False)

    def clearFilters(self):
        self.filterName.clear()
        self.filterLevel.setCurrentIndex(0)
        self.filterRange.setCurrentIndex(0)
        self.filterSchool.setCurrentIndex(0)
        self.filterClass.setCurrentIndex(0)
        self.filterConcentration.setCurrentIndex(0)
        self.filterRitual.setCurrentIndex(0)
        self.filterComponents.setCurrentIndex(0)

    def addSpell(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_windowAdd()
        self.ui.setupUi(self.window)
        self.window.show()

    def editSpell(self):
        # Retrieve the selected spell's information
        spellName = self.tableWidget.currentItem().text()
        self.mq = mongoQuerier.MongoQuerier()
        spellInfo = self.mq.findOne({'name': spellName})

        # Emit signal so that editWindow has the spell information needed to load the spell
        self.editSpellInfo.emit(spellInfo)
        self.editWindow.show()

    def deleteSpell(self):
        response = self.msgBoxConfirmDelete.exec_()
        spell = {}
        if (response == 0):
            # User reponds "Yes" to confirmation
            spell['name'] = self.tableWidget.currentItem().text()
            self.mq = mongoQuerier.MongoQuerier()
            self.mq.deleteOne(spell)
            # Submit query again to refresh the spell list
            self.submitQuery()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowMain = QtWidgets.QMainWindow()
    ui = Ui_windowMain()
    ui.setupUi(windowMain)
    windowMain.show()
    sys.exit(app.exec_())

