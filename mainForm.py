# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainForm.ui'
#
# Created: Wed Apr 22 17:31:18 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Sender(object):
    def setupUi(self, Sender):
        Sender.setObjectName(_fromUtf8("Sender"))
        Sender.resize(383, 584)
        Sender.setMinimumSize(QtCore.QSize(383, 584))
        Sender.setMaximumSize(QtCore.QSize(383, 584))
        self.textEdit_history = QtGui.QTextEdit(Sender)
        self.textEdit_history.setGeometry(QtCore.QRect(10, 10, 361, 391))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei"))
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_history.setFont(font)
        self.textEdit_history.setReadOnly(True)
        self.textEdit_history.setObjectName(_fromUtf8("textEdit_history"))
        self.textEdit_send = QtGui.QTextEdit(Sender)
        self.textEdit_send.setGeometry(QtCore.QRect(10, 445, 361, 96))
        self.textEdit_send.setObjectName(_fromUtf8("textEdit_send"))
        self.pushButton_openfile = QtGui.QPushButton(Sender)
        self.pushButton_openfile.setGeometry(QtCore.QRect(150, 550, 98, 27))
        self.pushButton_openfile.setObjectName(_fromUtf8("pushButton_openfile"))
        self.pushButton_sendmsg = QtGui.QPushButton(Sender)
        self.pushButton_sendmsg.setGeometry(QtCore.QRect(270, 550, 98, 27))
        self.pushButton_sendmsg.setObjectName(_fromUtf8("pushButton_sendmsg"))
        self.label = QtGui.QLabel(Sender)
        self.label.setGeometry(QtCore.QRect(10, 415, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Sender)
        self.lineEdit.setGeometry(QtCore.QRect(80, 410, 291, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Sender)
        QtCore.QMetaObject.connectSlotsByName(Sender)

    def retranslateUi(self, Sender):
        Sender.setWindowTitle(_translate("Sender", "Dialog", None))
        self.pushButton_openfile.setText(_translate("Sender", "Send file", None))
        self.pushButton_sendmsg.setText(_translate("Sender", "Send Text", None))
        self.label.setText(_translate("Sender", "Send to: ", None))
        self.lineEdit.setText(_translate("Sender", "127.0.0.1", None))

