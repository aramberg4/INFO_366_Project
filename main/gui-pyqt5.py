# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Victoria Ta\Desktop\INFO366\Project\INFO_366_Project\main\gui-pyqt5.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_windowMain(object):
    def setupUi(self, windowMain):
        windowMain.setObjectName("windowMain")
        windowMain.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(windowMain)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 15, 1241, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayout.addWidget(self.filterClass, 3, 7, 1, 1)
        self.filterSchool = QtWidgets.QComboBox(self.gridLayoutWidget)
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
        self.gridLayout.addWidget(self.filterSchool, 3, 6, 1, 1)
        self.labelLevel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelLevel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelLevel.setObjectName("labelLevel")
        self.gridLayout.addWidget(self.labelLevel, 2, 4, 1, 1)
        self.labelName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelName.setObjectName("labelName")
        self.gridLayout.addWidget(self.labelName, 2, 0, 1, 1)
        self.buttonName = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonName.sizePolicy().hasHeightForWidth())
        self.buttonName.setSizePolicy(sizePolicy)
        self.buttonName.setMaximumSize(QtCore.QSize(30, 16777215))
        self.buttonName.setObjectName("buttonName")
        self.gridLayout.addWidget(self.buttonName, 3, 1, 1, 1)
        self.buttonDescription = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDescription.sizePolicy().hasHeightForWidth())
        self.buttonDescription.setSizePolicy(sizePolicy)
        self.buttonDescription.setMaximumSize(QtCore.QSize(30, 16777215))
        self.buttonDescription.setObjectName("buttonDescription")
        self.gridLayout.addWidget(self.buttonDescription, 3, 3, 1, 1)
        self.filterDescription = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterDescription.sizePolicy().hasHeightForWidth())
        self.filterDescription.setSizePolicy(sizePolicy)
        self.filterDescription.setMaximumSize(QtCore.QSize(125, 16777215))
        self.filterDescription.setObjectName("filterDescription")
        self.gridLayout.addWidget(self.filterDescription, 3, 2, 1, 1)
        self.filterName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterName.sizePolicy().hasHeightForWidth())
        self.filterName.setSizePolicy(sizePolicy)
        self.filterName.setMaximumSize(QtCore.QSize(125, 16777215))
        self.filterName.setObjectName("filterName")
        self.gridLayout.addWidget(self.filterName, 3, 0, 1, 1)
        self.filterLevel = QtWidgets.QComboBox(self.gridLayoutWidget)
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
        self.gridLayout.addWidget(self.filterLevel, 3, 4, 1, 1)
        self.labelDescription = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelDescription.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelDescription.setObjectName("labelDescription")
        self.gridLayout.addWidget(self.labelDescription, 2, 2, 1, 1)
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
        self.gridLayout.addWidget(self.filterRange, 3, 5, 1, 1)
        self.labelRange = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelRange.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelRange.setObjectName("labelRange")
        self.gridLayout.addWidget(self.labelRange, 2, 5, 1, 1)
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
        self.gridLayout.addWidget(self.filterRitual, 3, 9, 1, 1)
        self.labelSchool = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelSchool.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelSchool.setObjectName("labelSchool")
        self.gridLayout.addWidget(self.labelSchool, 2, 6, 1, 1)
        self.labelConcentration = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelConcentration.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelConcentration.setObjectName("labelConcentration")
        self.gridLayout.addWidget(self.labelConcentration, 2, 8, 1, 1)
        self.labelClasses = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelClasses.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelClasses.setObjectName("labelClasses")
        self.gridLayout.addWidget(self.labelClasses, 2, 7, 1, 1)
        self.labelRitual = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelRitual.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelRitual.setObjectName("labelRitual")
        self.gridLayout.addWidget(self.labelRitual, 2, 9, 1, 1)
        self.filterConcentration = QtWidgets.QComboBox(self.gridLayoutWidget)
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
        self.gridLayout.addWidget(self.filterConcentration, 3, 8, 1, 1)
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
        self.filterComponents.addItem("")
        self.gridLayout.addWidget(self.filterComponents, 3, 10, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 11, 1, 1)
        self.labelComponents = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelComponents.sizePolicy().hasHeightForWidth())
        self.labelComponents.setSizePolicy(sizePolicy)
        self.labelComponents.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelComponents.setObjectName("labelComponents")
        self.gridLayout.addWidget(self.labelComponents, 2, 10, 1, 2)
        self.labelMongoDD = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelMongoDD.setFont(font)
        self.labelMongoDD.setObjectName("labelMongoDD")
        self.gridLayout.addWidget(self.labelMongoDD, 0, 0, 1, 1)
        self.buttonClear = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonClear.sizePolicy().hasHeightForWidth())
        self.buttonClear.setSizePolicy(sizePolicy)
        self.buttonClear.setObjectName("buttonClear")
        self.gridLayout.addWidget(self.buttonClear, 3, 11, 1, 1)
        windowMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
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
        self.filterClass.setItemText(1, _translate("windowMain", "Bard"))
        self.filterClass.setItemText(2, _translate("windowMain", "Cleric"))
        self.filterClass.setItemText(3, _translate("windowMain", "Druid"))
        self.filterClass.setItemText(4, _translate("windowMain", "Paladin"))
        self.filterClass.setItemText(5, _translate("windowMain", "Ranger"))
        self.filterClass.setItemText(6, _translate("windowMain", "Sorcerer"))
        self.filterClass.setItemText(7, _translate("windowMain", "Warlock"))
        self.filterClass.setItemText(8, _translate("windowMain", "Wizard"))
        self.filterSchool.setItemText(1, _translate("windowMain", "Abjuration"))
        self.filterSchool.setItemText(2, _translate("windowMain", "Conjuration"))
        self.filterSchool.setItemText(3, _translate("windowMain", "Divination"))
        self.filterSchool.setItemText(4, _translate("windowMain", "Enchantment"))
        self.filterSchool.setItemText(5, _translate("windowMain", "Evocation"))
        self.filterSchool.setItemText(6, _translate("windowMain", "Illusion"))
        self.filterSchool.setItemText(7, _translate("windowMain", "Necromancy"))
        self.filterSchool.setItemText(8, _translate("windowMain", "Transmutation"))
        self.labelLevel.setText(_translate("windowMain", "Level"))
        self.labelName.setText(_translate("windowMain", "Name"))
        self.buttonName.setText(_translate("windowMain", ">"))
        self.buttonDescription.setText(_translate("windowMain", ">"))
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
        self.labelDescription.setText(_translate("windowMain", "Description"))
        self.filterRange.setItemText(1, _translate("windowMain", "Self"))
        self.filterRange.setItemText(2, _translate("windowMain", "Touch"))
        self.filterRange.setItemText(3, _translate("windowMain", "Sight"))
        self.filterRange.setItemText(4, _translate("windowMain", "Special"))
        self.labelRange.setText(_translate("windowMain", "Range"))
        self.filterRitual.setItemText(1, _translate("windowMain", "yes"))
        self.filterRitual.setItemText(2, _translate("windowMain", "no"))
        self.labelSchool.setText(_translate("windowMain", "School"))
        self.labelConcentration.setText(_translate("windowMain", "Concentration"))
        self.labelClasses.setText(_translate("windowMain", "Classes"))
        self.labelRitual.setText(_translate("windowMain", "Ritual"))
        self.filterConcentration.setItemText(1, _translate("windowMain", "yes"))
        self.filterConcentration.setItemText(2, _translate("windowMain", "no"))
        self.filterComponents.setItemText(1, _translate("windowMain", "no verbal"))
        self.filterComponents.setItemText(2, _translate("windowMain", "no somatic"))
        self.filterComponents.setItemText(3, _translate("windowMain", "no material"))
        self.filterComponents.setItemText(4, _translate("windowMain", "no cost"))
        self.pushButton.setText(_translate("windowMain", "+ Add Spell"))
        self.labelComponents.setText(_translate("windowMain", "Components"))
        self.labelMongoDD.setText(_translate("windowMain", "Mongo D&D"))
        self.buttonClear.setText(_translate("windowMain", "Clear Filters"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowMain = QtWidgets.QMainWindow()
    ui = Ui_windowMain()
    ui.setupUi(windowMain)
    windowMain.show()
    sys.exit(app.exec_())

