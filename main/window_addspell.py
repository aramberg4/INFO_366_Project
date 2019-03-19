# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Victoria Ta\Desktop\INFO366\Project\INFO_366_Project\main\windowAddSpell.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtWidgets import QCheckBox, QMessageBox
import sys
sys.path.append("..")
from modules import mongoQuerier

class Ui_windowAdd(object):
    def setupUi(self, windowAdd):
        windowAdd.setObjectName("windowAdd")
        windowAdd.resize(800, 600)

        # Background
        oImage = QImage("background_addspell.jpg")
        sImage = oImage.scaled(QSize(800,600))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))    # 10 = Windowrole
        windowAdd.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(windowAdd)
        self.centralwidget.setObjectName("centralwidget")

        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(610, 520, 75, 23))
        self.buttonSave.setObjectName("buttonSave")
        self.buttonSave.clicked.connect(lambda: self.saveSpell(windowAdd))
        self.buttonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCancel.setGeometry(QtCore.QRect(700, 520, 75, 23))
        self.buttonCancel.setObjectName("buttonCancel")
        self.buttonCancel.clicked.connect(lambda: self.closeWindow(windowAdd))

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 761, 451))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelConcentration = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelConcentration.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelConcentration.setObjectName("labelConcentration")
        self.gridLayout_2.addWidget(self.labelConcentration, 7, 0, 1, 1)
        self.labelClasses = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelClasses.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelClasses.setObjectName("labelClasses")
        self.gridLayout_2.addWidget(self.labelClasses, 6, 0, 1, 1)
        self.labelAddSpell = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelAddSpell.setFont(font)
        self.labelAddSpell.setObjectName("labelAddSpell")
        self.gridLayout_2.addWidget(self.labelAddSpell, 0, 0, 1, 1)
        self.labelRange = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelRange.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelRange.setObjectName("labelRange")
        self.gridLayout_2.addWidget(self.labelRange, 4, 0, 1, 1)
        self.filterRange = QtWidgets.QComboBox(self.gridLayoutWidget_2)
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
        self.gridLayout_2.addWidget(self.filterRange, 4, 1, 1, 1)
        self.labelSchool = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelSchool.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelSchool.setObjectName("labelSchool")
        self.gridLayout_2.addWidget(self.labelSchool, 5, 0, 1, 1)
        self.labelRitual = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelRitual.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelRitual.setObjectName("labelRitual")
        self.gridLayout_2.addWidget(self.labelRitual, 8, 0, 1, 1)
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
        self.gridLayout_2.addWidget(self.filterConcentration, 7, 1, 1, 1)
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
        self.gridLayout_2.addWidget(self.filterRitual, 8, 1, 1, 1)

        # [START] CASTING TIME

        self.labelCastingTime = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelCastingTime.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelCastingTime.setObjectName("labelCastingTime")
        self.gridLayout_2.addWidget(self.labelCastingTime, 9, 0, 1, 1)

        self.filterCastingTime = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterRitual.sizePolicy().hasHeightForWidth())
        self.filterCastingTime.setSizePolicy(sizePolicy)
        self.filterCastingTime.setMaximumSize(QtCore.QSize(16777215, 20))
        self.filterCastingTime.setObjectName("filterCastingTime")
        self.filterCastingTime.addItem("")
        self.filterCastingTime.setItemText(0, "")
        self.filterCastingTime.addItem("")
        self.filterCastingTime.addItem("")
        self.filterCastingTime.addItem("")
        self.gridLayout_2.addWidget(self.filterCastingTime, 9, 1, 1, 1)

        # [END] CASTING TIME

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
        self.gridLayout_2.addWidget(self.filterSchool, 5, 1, 1, 1)

        # [START] CLASSES
        self.classLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.classLayoutWidget.setObjectName("classLayoutWidget")
        self.classLayout = QtWidgets.QGridLayout(self.classLayoutWidget)
        self.classLayout.setContentsMargins(0, 0, 0, 0)
        self.classLayout.setObjectName("classLayout")
        self.gridLayout_2.addWidget(self.classLayoutWidget, 6, 1, 1, 1)

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
        self.gridLayout_2.addWidget(self.labelComponents, 10, 0, 1, 1)

        self.componentLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.componentLayoutWidget.setObjectName("componentLayoutWidget")
        self.componentLayout = QtWidgets.QGridLayout(self.componentLayoutWidget)
        self.componentLayout.setContentsMargins(0, 0, 0, 0)
        self.componentLayout.setObjectName("componentLayout")
        self.gridLayout_2.addWidget(self.componentLayoutWidget, 10, 1, 1, 1)

        self.checkboxComponentV = QCheckBox("V")
        self.checkboxComponentS = QCheckBox("S")
        self.checkboxComponentM = QCheckBox("M")
        self.componentLayout.addWidget(self.checkboxComponentV, 0, 0, 1, 1)
        self.componentLayout.addWidget(self.checkboxComponentS, 0, 1, 1, 1)
        self.componentLayout.addWidget(self.checkboxComponentM, 0, 2, 1, 1)
        # [END] COMPONENTS

        # [START] DURATION
        self.labelDuration = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDuration.sizePolicy().hasHeightForWidth())
        self.labelDuration.setSizePolicy(sizePolicy)
        self.labelDuration.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelDuration.setObjectName("labelDuration")
        self.gridLayout_2.addWidget(self.labelDuration, 11, 0, 1, 1)
        self.filterDuration = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterDuration.sizePolicy().hasHeightForWidth())
        self.filterDuration.setSizePolicy(sizePolicy)
        self.filterDuration.setMaximumSize(QtCore.QSize(125, 16777215))
        self.filterDuration.setObjectName("filterDuration")
        self.filterDuration.addItem("")
        self.filterDuration.setItemText(0, "")
        self.filterDuration.addItem("")
        self.filterDuration.addItem("")
        self.filterDuration.addItem("")
        self.filterDuration.addItem("")
        self.filterDuration.addItem("")
        self.filterDuration.addItem("")
        self.filterDuration.addItem("")
        self.gridLayout_2.addWidget(self.filterDuration, 11, 1, 1, 1)
        # [END] DURATION

        self.msgBoxInvalidInput = QMessageBox()
        self.msgBoxAlreadyExists = QMessageBox()

        windowAdd.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowAdd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        windowAdd.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(windowAdd)
        self.statusbar.setObjectName("statusbar")
        windowAdd.setStatusBar(self.statusbar)

        self.retranslateUi(windowAdd)
        QtCore.QMetaObject.connectSlotsByName(windowAdd)

    def retranslateUi(self, windowAdd):
        _translate = QtCore.QCoreApplication.translate
        windowAdd.setWindowTitle(_translate("windowAdd", "Add Spell | Mongo D&D"))
        self.buttonSave.setText(_translate("windowAdd", "Save"))
        self.buttonCancel.setText(_translate("windowAdd", "Cancel"))
        self.labelConcentration.setText(_translate("windowAdd", "Concentration"))
        self.labelClasses.setText(_translate("windowAdd", "Classes"))
        self.labelAddSpell.setText(_translate("windowAdd", "Add Spell"))
        self.labelRange.setText(_translate("windowAdd", "Range"))
        self.filterRange.setItemText(1, _translate("windowAdd", "Self"))
        self.filterRange.setItemText(2, _translate("windowAdd", "Touch"))
        self.filterRange.setItemText(3, _translate("windowAdd", "Sight"))
        self.filterRange.setItemText(4, _translate("windowAdd", "Special"))
        self.labelSchool.setText(_translate("windowAdd", "School"))
        self.labelRitual.setText(_translate("windowAdd", "Ritual"))
        self.labelCastingTime.setText(_translate("windowAdd", "Casting Time"))
        self.filterCastingTime.setItemText(1, _translate("windowAdd", "1 action"))
        self.filterCastingTime.setItemText(2, _translate("windowAdd", "1 bonus action"))
        self.filterCastingTime.setItemText(3, _translate("windowAdd", "1 reaction"))
        self.labelName.setText(_translate("windowAdd", "Name"))
        self.filterConcentration.setItemText(1, _translate("windowAdd", "yes"))
        self.filterConcentration.setItemText(2, _translate("windowAdd", "no"))
        self.filterRitual.setItemText(1, _translate("windowAdd", "yes"))
        self.filterRitual.setItemText(2, _translate("windowAdd", "no"))
        self.labelDescription.setText(_translate("windowAdd", "Description"))
        self.labelLevel.setText(_translate("windowAdd", "Level"))
        self.filterLevel.setItemText(1, _translate("windowAdd", "0"))
        self.filterLevel.setItemText(2, _translate("windowAdd", "1"))
        self.filterLevel.setItemText(3, _translate("windowAdd", "2"))
        self.filterLevel.setItemText(4, _translate("windowAdd", "3"))
        self.filterLevel.setItemText(5, _translate("windowAdd", "4"))
        self.filterLevel.setItemText(6, _translate("windowAdd", "5"))
        self.filterLevel.setItemText(7, _translate("windowAdd", "6"))
        self.filterLevel.setItemText(8, _translate("windowAdd", "7"))
        self.filterLevel.setItemText(9, _translate("windowAdd", "8"))
        self.filterLevel.setItemText(10, _translate("windowAdd", "9"))
        self.filterSchool.setItemText(1, _translate("windowAdd", "Abjuration"))
        self.filterSchool.setItemText(2, _translate("windowAdd", "Conjuration"))
        self.filterSchool.setItemText(3, _translate("windowAdd", "Divination"))
        self.filterSchool.setItemText(4, _translate("windowAdd", "Enchantment"))
        self.filterSchool.setItemText(5, _translate("windowAdd", "Evocation"))
        self.filterSchool.setItemText(6, _translate("windowAdd", "Illusion"))
        self.filterSchool.setItemText(7, _translate("windowAdd", "Necromancy"))
        self.filterSchool.setItemText(8, _translate("windowAdd", "Transmutation"))
        self.labelComponents.setText(_translate("windowAdd", "Components"))
        self.labelDuration.setText(_translate("windowAdd", "Duration"))
        self.filterDuration.setItemText(1, _translate("windowAdd", "Instantaneous"))
        self.filterDuration.setItemText(2, _translate("windowAdd", "Until dispelled"))
        self.filterDuration.setItemText(3, _translate("windowAdd", "Special"))
        self.filterDuration.setItemText(4, _translate("windowAdd", "1 minute"))
        self.filterDuration.setItemText(5, _translate("windowAdd", "1 hour"))
        self.filterDuration.setItemText(6, _translate("windowAdd", "8 hours"))
        self.filterDuration.setItemText(7, _translate("windowAdd", "24 hours"))

        self.labelAddSpell.setStyleSheet('color: white;'
                                        'font: 24pt "Arial";'
                                        'font-weight: bold;'
                                            )
        self.labelName.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelDescription.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelLevel.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelRange.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelSchool.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelClasses.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelConcentration.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelRitual.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelComponents.setStyleSheet('color: white;' 'font-weight: bold;')
        self.labelDuration.setStyleSheet('color: white;' 'font-weight: bold;')
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

    def closeWindow(self, windowAdd):
        windowAdd.close()

    def saveSpell(self, windowAdd):
        # Check which classes are selected
        i = 0
        chosenClasses = []
        # Iterating through classLayout and returns list of classes selected
        for checkboxClass in self.classLayout.parentWidget().findChildren(QCheckBox):
            if checkboxClass.isChecked():
                chosenClasses.append({ 'name': checkboxClass.text() })
                i += 1
        print(chosenClasses)

        # Check which components are selected
        j = 0
        chosenComponents = []
        # Iterating through componentLayout and returns list of components selected
        for checkboxComponent in self.componentLayout.parentWidget().findChildren(QCheckBox):
            if checkboxComponent.isChecked():
                chosenComponents.append(checkboxComponent.text())
                j += 1
        print(chosenComponents)

        # Compile values for each field into a doc
        # Check for any inputs that have not not been entered, in which case it should
        # not allow for insertion of spell.
        self.insertData = {}
        self.nameData = {}
        validInput = True
        if self.filterName.text() is not '':
            self.insertData['name'] = self.filterName.text()
            self.nameData['name'] = { '$regex': self.filterName.text(), '$options': 'i' }
        else: validInput = False
        if self.filterDescription.text() is not '':
            self.insertData['desc'] = self.filterDescription.text()
        else: validInput = False
        if self.filterLevel.currentText() is not '':
            self.insertData['level'] = int(self.filterLevel.currentText())
        else: validInput = False
        if self.filterRange.currentText() is not '':
            self.insertData['range'] = self.filterRange.currentText()
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
        if self.filterCastingTime.currentText() is not '':
            self.insertData['casting_time'] = self.filterCastingTime.currentText()
        else: validInput = False
        if len(chosenComponents) > 0:
            self.insertData['components'] = chosenComponents
        else: validInput = False
        if self.filterDuration.currentText() is not '':
            self.insertData['duration'] = self.filterDuration.currentText()
        else: validInput = False

        self.mq = mongoQuerier.MongoQuerier()

        # Querying database to see if spell with the same name already exists.
        self.cursor = self.mq.find(self.nameData)

        if (validInput == False):
            # All inputs not filled out---show message box.
            self.msgBoxInvalidInput.exec_()
        elif (self.cursor.count() == 1):
            # Spell with same name already exists---show message box.
            self.msgBoxAlreadyExists.exec_()
        else:
            # Insert data into the database.
            self.mq.insertOne(self.insertData)
            self.closeWindow(windowAdd)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowAdd = QtWidgets.QMainWindow()
    ui = Ui_windowAdd()
    ui.setupUi(windowAdd)
    windowAdd.show()
    sys.exit(app.exec_())

