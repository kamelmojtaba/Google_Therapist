# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Score(object):
    def setupUi(self, Score):
        Score.setObjectName("Score")
        Score.resize(806, 407)
        Score.setMinimumSize(QtCore.QSize(806, 407))
        Score.setMaximumSize(QtCore.QSize(806, 407))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Score.setFont(font)
        Score.setStyleSheet("background-color:#F2F5C8;\n"
"")
        self.verticalLayoutWidget = QtWidgets.QWidget(Score)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 821, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(193, 222, 174);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(Score)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(700, 330, 101, 71))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 42))
        self.pushButton_2.setStyleSheet("background-color: rgb(33, 159, 148);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_14.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Score)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(330, 70, 160, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Score)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 160, 2366, 141))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setMinimumSize(QtCore.QSize(2364, 139))
        self.label_3.setMaximumSize(QtCore.QSize(2364, 139))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)

        self.retranslateUi(Score)
        QtCore.QMetaObject.connectSlotsByName(Score)

    def retranslateUi(self, Score):
        _translate = QtCore.QCoreApplication.translate
        Score.setWindowTitle(_translate("Score", "Score"))
        self.label.setText(_translate("Score", "Your Score"))
        self.pushButton_2.setAccessibleName(_translate("Score", "NextButton"))
        self.pushButton_2.setText(_translate("Score", "OK"))
        self.label_2.setText(_translate("Score", "0"))
        self.label_3.setText(_translate("Score", "Severe, Immediate initiation of pharmacotheray and, if severe impairment\n"
"                        or poor resonse to therapy, expedited referral to a mental health\n"
"                        specialist for psychtherapy and/or collabrative mangement"))
