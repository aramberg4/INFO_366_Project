# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Victoria Ta\Desktop\INFO366\Project\INFO_366_Project\main\window_editspell.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, QRegExp, QObject, pyqtSignal
from PyQt5.QtWidgets import QCheckBox, QMessageBox
import sys
sys.path.append("..")
from modules import mongoQuerier

class Ui_windowEdit(object):
    def setupUi(self, windowEdit):
        windowEdit.setObjectName("windowEdit")
        windowEdit.resize(800, 600)

        # Background
        oImage = QImage("background_editspell.jpg")
        sImage = oImage.scaled(QSize(800,600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))    # 10 = Windowrole
        windowEdit.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(windowEdit)
        self.centralwidget.setObjectName("centralwidget")

        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(610, 520, 75, 23))
        self.buttonSave.setObjectName("buttonSave")
        self.buttonSave.clicked.connect(lambda: self.saveSpell(windowEdit))
        self.buttonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCancel.setGeometry(QtCore.QRect(700, 520, 75, 23))
        self.buttonCancel.setObjectName("buttonCancel")
        self.buttonCancel.clicked.connect(lambda: self.closeWindow(windowEdit))

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 761, 451))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelConcentration = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelConcentration.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelConcentration.setObjectName("labelConcentration")
        self.gridLayout_2.addWidget(self.labelConcentration, 6, 0, 1, 1)
        self.labelClasses = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelClasses.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelClasses.setObjectName("labelClasses")
        self.gridLayout_2.addWidget(self.labelClasses, 5, 0, 1, 1)
        self.labelAddSpell = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelAddSpell.setFont(font)
        self.labelAddSpell.setObjectName("labelAddSpell")
        self.gridLayout_2.addWidget(self.labelAddSpell, 0, 0, 1, 1)
        self.labelSchool = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelSchool.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelSchool.setObjectName("labelSchool")
        self.gridLayout_2.addWidget(self.labelSchool, 4, 0, 1, 1)
        self.labelRitual = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelRitual.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelRitual.setObjectName("labelRitual")
        self.gridLayout_2.addWidget(self.labelRitual, 7, 0, 1, 1)
        self.labelName = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelName.setObjectName("labelName")
        self.gridLayout_2.addWidget(self.labelName, 1, 0, 1, 1)
        self.filterConcentration = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterConcentration.sizePolicy().hasHeightForWidth())
        self.filterConcentration.setSizePolicy(sizePolicy)
        self.filterConcentration.setMaximumSize(QtCore.QSize(60, 16777215))
        self.filterConcentration.setObjectName("filterConcentration")
        self.filterConcentration.addItem("")
        self.filterConcentration.setItemText(0, "")
        self.filterConcentration.addItem("")
        self.filterConcentration.addItem("")
        self.gridLayout_2.addWidget(self.filterConcentration, 6, 1, 1, 1)
        self.filterRitual = QtWidgets.QComboBox(self.gridLayoutWidget_2)
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
        self.gridLayout_2.addWidget(self.filterRitual, 7, 1, 1, 1)

        self.labelDescription = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelDescription.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelDescription.setObjectName("labelDescription")
        self.gridLayout_2.addWidget(self.labelDescription, 2, 0, 1, 1)
        self.labelLevel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelLevel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelLevel.setObjectName("labelLevel")
        self.gridLayout_2.addWidget(self.labelLevel, 3, 0, 1, 1)
        self.filterDescription = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterDescription.sizePolicy().hasHeightForWidth())
        self.filterDescription.setSizePolicy(sizePolicy)
        self.filterDescription.setMaximumSize(QtCore.QSize(125, 16777215))
        self.filterDescription.setObjectName("filterDescription")
        self.gridLayout_2.addWidget(self.filterDescription, 2, 1, 1, 1)
        self.filterName = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterName.sizePolicy().hasHeightForWidth())
        self.filterName.setSizePolicy(sizePolicy)
        self.filterName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.filterName.setObjectName("filterName")
        self.gridLayout_2.addWidget(self.filterName, 1, 1, 1, 1)
        self.filterLevel = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterLevel.sizePolicy().hasHeightForWidth())
        self.filterLevel.setSizePolicy(sizePolicy)
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
        self.gridLayout_2.addWidget(self.filterLevel, 3, 1, 1, 1)
        self.filterSchool = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterSchool.sizePolicy().hasHeightForWidth())
        self.filterSchool.setSizePolicy(sizePolicy)
        self.filterSchool.setMaximumSize(QtCore.QSize(125, 16777215))
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
        self.gridLayout_2.addWidget(self.filterSchool, 4, 1, 1, 1)

        # [START] CLASSES
        self.classLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.classLayoutWidget.setObjectName("classLayoutWidget")
        self.classLayout = QtWidgets.QGridLayout(self.classLayoutWidget)
        self.classLayout.setContentsMargins(0, 0, 0, 0)
        self.classLayout.setObjectName("classLayout")
        self.gridLayout_2.addWidget(self.classLayoutWidget, 5, 1, 1, 1)

        self.checkboxClassBard = QCheckBox("Bard")
        self.checkboxClassCleric = QCheckBox("Cleric")
        self.checkboxClassDruid = QCheckBox("Druid")
        self.checkboxClassPaladin = QCheckBox("Paladin")
        self.checkboxClassRanger = QCheckBox("Ranger")
        self.checkboxClassSorcerer = QCheckBox("Sorcerer")
        self.checkboxClassWarlock = QCheckBox("Warlock")
        self.checkboxClassWizard = QCheckBox("Wizard")
        self.classLayout.addWidget(self.checkboxClassBard, 0, 0, 1, 1)
        self.classLayout.addWidget(self.checkboxClassCleric, 0, 1, 1, 1)
        self.classLayout.addWidget(self.checkboxClassDruid, 1, 0, 1, 1)
        self.classLayout.addWidget(self.checkboxClassPaladin, 1, 1, 1, 1)
        self.classLayout.addWidget(self.checkboxClassRanger, 2, 0, 1, 1)
        self.classLayout.addWidget(self.checkboxClassSorcerer, 2, 1, 1, 1)
        self.classLayout.addWidget(self.checkboxClassWarlock, 3, 0, 1, 1)
        self.classLayout.addWidget(self.checkboxClassWizard, 3, 1, 1, 1)
        # [END] CLASSES

        # [START] COMPONENTS
        self.labelComponents = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelComponents.sizePolicy().hasHeightForWidth())
        self.labelComponents.setSizePolicy(sizePolicy)
        self.labelComponents.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelComponents.setObjectName("labelComponents")
        self.gridLayout_2.addWidget(self.labelComponents, 8, 0, 1, 1)

        self.componentLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.componentLayoutWidget.setObjectName("componentLayoutWidget")
        self.componentLayout = QtWidgets.QGridLayout(self.componentLayoutWidget)
        self.componentLayout.setContentsMargins(0, 0, 0, 0)
        self.componentLayout.setObjectName("componentLayout")
        self.gridLayout_2.addWidget(self.componentLayoutWidget, 8, 1, 1, 1)

        self.checkboxComponentV = QCheckBox("V")
        self.checkboxComponentS = QCheckBox("S")
        self.checkboxComponentM = QCheckBox("M")
        self.componentLayout.addWidget(self.checkboxComponentV, 0, 0, 1, 1)
        self.componentLayout.addWidget(self.checkboxComponentS, 0, 1, 1, 1)
        self.componentLayout.addWidget(self.checkboxComponentM, 0, 2, 1, 1)
        # [END] COMPONENTS

        self.nameData = {}

        self.msgBoxInvalidInput = QMessageBox()
        self.msgBoxAlreadyExists = QMessageBox()

        windowEdit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowEdit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        windowEdit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(windowEdit)
        self.statusbar.setObjectName("statusbar")
        windowEdit.setStatusBar(self.statusbar)

        self.retranslateUi(windowEdit)
        QtCore.QMetaObject.connectSlotsByName(windowEdit)

    def retranslateUi(self, windowEdit):
        _translate = QtCore.QCoreApplication.translate
        windowEdit.setWindowTitle(_translate("windowEdit", "Edit Spell | Mongo D&D"))
        self.buttonSave.setText(_translate("windowEdit", "Save"))
        self.buttonCancel.setText(_translate("windowEdit", "Cancel"))
        self.labelConcentration.setText(_translate("windowEdit", "Concentration"))
        self.labelClasses.setText(_translate("windowEdit", "Classes"))
        self.labelAddSpell.setText(_translate("windowEdit", "Edit Spell"))
        self.labelSchool.setText(_translate("windowEdit", "School"))
        self.labelRitual.setText(_translate("windowEdit", "Ritual"))
        self.labelName.setText(_translate("windowEdit", "Name"))
        self.filterConcentration.setItemText(1, _translate("windowEdit", "yes"))
        self.filterConcentration.setItemText(2, _translate("windowEdit", "no"))
        self.filterRitual.setItemText(1, _translate("windowEdit", "yes"))
        self.filterRitual.setItemText(2, _translate("windowEdit", "no"))
        self.labelDescription.setText(_translate("windowEdit", "Description"))
        self.labelLevel.setText(_translate("windowEdit", "Level"))
        self.filterLevel.setItemText(1, _translate("windowEdit", "0"))
        self.filterLevel.setItemText(2, _translate("windowEdit", "1"))
        self.filterLevel.setItemText(3, _translate("windowEdit", "2"))
        self.filterLevel.setItemText(4, _translate("windowEdit", "3"))
        self.filterLevel.setItemText(5, _translate("windowEdit", "4"))
        self.filterLevel.setItemText(6, _translate("windowEdit", "5"))
        self.filterLevel.setItemText(7, _translate("windowEdit", "6"))
        self.filterLevel.setItemText(8, _translate("windowEdit", "7"))
        self.filterLevel.setItemText(9, _translate("windowEdit", "8"))
        self.filterLevel.setItemText(10, _translate("windowEdit", "9"))
        self.filterSchool.setItemText(1, _translate("windowEdit", "Abjuration"))
        self.filterSchool.setItemText(2, _translate("windowEdit", "Conjuration"))
        self.filterSchool.setItemText(3, _translate("windowEdit", "Divination"))
        self.filterSchool.setItemText(4, _translate("windowEdit", "Enchantment"))
        self.filterSchool.setItemText(5, _translate("windowEdit", "Evocation"))
        self.filterSchool.setItemText(6, _translate("windowEdit", "Illusion"))
        self.filterSchool.setItemText(7, _translate("windowEdit", "Necromancy"))
        self.filterSchool.setItemText(8, _translate("windowEdit", "Transmutation"))
        self.labelComponents.setText(_translate("windowEdit", "Components"))

        self.labelAddSpell.setStyleSheet('color: white;'
                                        'font: 24pt "Arial";'
                                        'font-weight: bold;'
                                            )
        self.labelName.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelDescription.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelLevel.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelSchool.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelClasses.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelConcentration.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelRitual.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelComponents.setStyleSheet('color: white;' 'font-weight: bold;')
        self.checkboxClassBard.setStyleSheet('color: white;' 'font-weight: bold;')
        self.checkboxClassCleric.setStyleSheet('color: white;' 'font-weight: bold;')
        self.checkboxClassDruid.setStyleSheet('color: white;' 'font-weight: bold;')
        self.checkboxClassPaladin.setStyleSheet('color: white;' 'font-weight: bold;')
        self.checkboxClassRanger.setStyleSheet('color: white;' 'font-weight: bold;')
        self.checkboxClassSorcerer.setStyleSheet('color: white;' 'font-weight: bold;')
        self.checkboxClassWarlock.setStyleSheet('color: white;' 'font-weight: bold;')
        self.checkboxClassWizard.setStyleSheet('color: white;' 'font-weight: bold;')
        self.checkboxComponentV.setStyleSheet('color: white;' 'font-weight: bold;')
        self.checkboxComponentS.setStyleSheet('color: white;''font-weight: bold;')
        self.checkboxComponentM.setStyleSheet('color: white;' 'font-weight: bold;')

        self.msgBoxInvalidInput.setText('Missing input!')
        self.msgBoxInvalidInput.setInformativeText('Please fill out all fields for the spell before attempting to save.')
        self.msgBoxInvalidInput.setWindowTitle('Mongo D&D')

        self.msgBoxAlreadyExists.setText('Bah! Cannot add spell.')
        self.msgBoxAlreadyExists.setInformativeText('A spell with that name already exists! Please enter a unique name to save the spell.')
        self.msgBoxAlreadyExists.setWindowTitle('Mongo D&D')

    def closeWindow(self, windowEdit):
        windowEdit.close()

    def loadSpell(self, spellInfo):
        # Populate the fields with the values from spellInfo
        
        self.filterName.setText(spellInfo['name'])
        self.nameData['name'] = { '$regex': self.filterName.text(), '$options': 'i' }
        self.filterDescription.setText(spellInfo['desc'][0])

        # Fields utilizing combo boxes need index of item that it should be set to
        levelIndex = self.filterLevel.findText(str(spellInfo['level']), QtCore.Qt.MatchFixedString)
        if (levelIndex >= 0):
            self.filterLevel.setCurrentIndex(levelIndex)

        schoolIndex = self.filterSchool.findText(spellInfo['school']['name'], QtCore.Qt.MatchFixedString)
        if (schoolIndex >= 0):
            self.filterSchool.setCurrentIndex(schoolIndex)

        classesArray = spellInfo['classes']
        classes = []
        for c in classesArray:
            classes.append(c['name'])

        for checkboxClass in self.classLayout.parentWidget().findChildren(QCheckBox):
            checkboxClassText = checkboxClass.text()
            if (checkboxClassText in classes):
                checkboxClass.setCheckState(2)

        concentrationIndex = self.filterConcentration.findText(spellInfo['concentration'], QtCore.Qt.MatchFixedString)
        if (concentrationIndex >= 0):
            self.filterConcentration.setCurrentIndex(concentrationIndex)

        ritualIndex = self.filterRitual.findText(spellInfo['ritual'], QtCore.Qt.MatchFixedString)
        if (ritualIndex >= 0):
            self.filterRitual.setCurrentIndex(ritualIndex)

        components = spellInfo['components']
        for checkboxComponent in self.componentLayout.parentWidget().findChildren(QCheckBox):
            checkboxComponentText = checkboxComponent.text()
            if (checkboxComponentText in components):
                checkboxComponent.setCheckState(2)


    def saveSpell(self, windowEdit):
        # Check which classes are selected
        chosenClasses = []
        # Iterating through classLayout and returns list of classes selected
        for checkboxClass in self.classLayout.parentWidget().findChildren(QCheckBox):
            if checkboxClass.isChecked():
                chosenClasses.append({ 'name': checkboxClass.text() })

        # Check which components are selected
        chosenComponents = []
        # Iterating through componentLayout and returns list of components selected
        for checkboxComponent in self.componentLayout.parentWidget().findChildren(QCheckBox):
            if checkboxComponent.isChecked():
                chosenComponents.append(checkboxComponent.text())

        # Compile values for each field into a doc
        # Check for any inputs that have not not been entered, in which case it should
        # not allow for insertion of spell.
        self.insertData = {}
        validInput = True
        if self.filterName.text() is not '':
            self.insertData['name'] = self.filterName.text()
        else: validInput = False
        if self.filterDescription.text() is not '':
            self.insertData['desc'] = self.filterDescription.text()
        else: validInput = False
        if self.filterLevel.currentText() is not '':
            self.insertData['level'] = int(self.filterLevel.currentText())
        else: validInput = False
        if self.filterSchool.currentText() is not '':
            self.insertData['school'] = { 'name': self.filterSchool.currentText()}
        else: validInput = False
        if len(chosenClasses) > 0:
            for chosenClass in chosenClasses:
                self.insertData['classes'] = chosenClasses
        else: validInput = False
        if self.filterConcentration.currentText() is not '':
            self.insertData['concentration'] = self.filterConcentration.currentText()
        else: validInput = False
        if self.filterRitual.currentText() is not '':
            self.insertData['ritual'] = self.filterRitual.currentText()
        else: validInput = False
        if len(chosenComponents) > 0:
            self.insertData['components'] = chosenComponents
        else: validInput = False

        self.mq = mongoQuerier.MongoQuerier()

        print(self.nameData)

        if (validInput == False):
            # All inputs not filled out---show message box.
            self.msgBoxInvalidInput.exec_()
        else:
            # Insert data into the database.
            self.mq.updateOne(self.nameData, {'$set': self.insertData}, True)
            self.closeWindow(windowEdit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowEdit = QtWidgets.QMainWindow()
    ui = Ui_windowEdit()
    ui.setupUi(windowEdit)
    windowEdit.show()
    sys.exit(app.exec_())

