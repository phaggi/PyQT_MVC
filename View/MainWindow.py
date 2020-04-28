# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimpleMVC/View/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 49)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_c = QtWidgets.QLineEdit(self.centralwidget)
        self.le_c.setObjectName("le_c")
        self.horizontalLayout.addWidget(self.le_c)
        self.lbl_plus = QtWidgets.QLabel(self.centralwidget)
        self.lbl_plus.setObjectName("lbl_plus")
        self.horizontalLayout.addWidget(self.lbl_plus)
        self.le_d = QtWidgets.QLineEdit(self.centralwidget)
        self.le_d.setObjectName("le_d")
        self.horizontalLayout.addWidget(self.le_d)
        self.lbl_equal = QtWidgets.QLabel(self.centralwidget)
        self.lbl_equal.setObjectName("lbl_equal")
        self.horizontalLayout.addWidget(self.lbl_equal)
        self.le_result = QtWidgets.QLineEdit(self.centralwidget)
        self.le_result.setObjectName("le_result")
        self.horizontalLayout.addWidget(self.le_result)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_plus.setText(_translate("MainWindow", "+"))
        self.lbl_equal.setText(_translate("MainWindow", "="))
