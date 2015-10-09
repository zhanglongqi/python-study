# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Thu May 22 17:26:36 2014
# by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!



from PyQt4 import QtCore, QtGui

__author__ = 'longqi'

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Form(object):
    click_count = 0
    """
    Declaring a dict outside of __init__ as you initially did is declaring a class-level variable. It is only created
    once at first, whenever you create new objects it will reuse this same dict. To create instance variables, you
    declare them with self in __init__; its as simple as that.
    """

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 380)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 30, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 571, 281))
        self.lineEdit.setText(str(self.click_count) + ' clicks\n')
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.slot1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QtGui.QApplication.translate("Form", "Form for testing, 测试窗体", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(
            QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

    def slot1(self):
        self.click_count += 1
        self.lineEdit.setText(str(self.click_count) + ' clicks\n')


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
