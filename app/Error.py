# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(402, 173)
        Error.setStyleSheet("background-color:#F2F5C8;")
        self.verticalLayoutWidget = QtWidgets.QWidget(Error)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-10, -1, 421, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(201, 63, 63);\n"
"color:#FFF;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(Error)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(310, 110, 91, 71))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 42))
        self.pushButton_2.setStyleSheet("background-color: rgb(33, 159, 148);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_14.addWidget(self.pushButton_2)

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Error"))
        self.label.setText(_translate("Error", "Please Select Un Option"))
        self.pushButton_2.setAccessibleName(_translate("Error", "NextButton"))
        self.pushButton_2.setText(_translate("Error", "OK"))
