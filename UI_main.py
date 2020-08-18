# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

'''
This code made by Muhammad Wildan
release time: 19-08-2020, 04:07 WIB

nb: ini program tampilan/UI yang digenerate dari QTdesigner

'''



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 473)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 280, 91, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 200, 91, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 200, 91, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 120, 91, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 411, 441))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # biar gabisa hover pake arrow key
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_7.setFocusPolicy(QtCore.Qt.NoFocus)

        # shortcut button
        QtWidgets.QShortcut(QtCore.Qt.Key_Up, self.pushButton_4,
                            self.pushButton_7.animateClick)
        QtWidgets.QShortcut(QtCore.Qt.Key_Right, self.pushButton_4,
                            self.pushButton_5.animateClick)
        QtWidgets.QShortcut(QtCore.Qt.Key_Down, self.pushButton_4,
                            self.pushButton_4.animateClick)
        QtWidgets.QShortcut(QtCore.Qt.Key_Left, self.pushButton_4,
                            self.pushButton_6.animateClick)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Raspibot-PyQt5"))
        self.pushButton_4.setText(_translate("Form", "Mundur"))
        self.pushButton_5.setText(_translate("Form", "Kanan"))
        self.pushButton_6.setText(_translate("Form", "Kiri"))
        self.pushButton_7.setText(_translate("Form", "Maju"))
        self.label.setText(_translate("Form", "Mode Navigasi"))
