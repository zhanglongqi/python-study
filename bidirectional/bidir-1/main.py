__author__ = 'longqi'
import sys
from PyQt4 import QtCore, QtGui

from bidirUI import Ui_Form


class MainWindow(QtGui.QWidget, Ui_Form):
    # custom slot
    def apply(self):
        print ('Hello World')
        self.setWindowTitle('test')

    def __init__(self):
        QtGui.QWidget.__init__(self)

        # set up User Interface (widgets, layout...)
        self.setupUi(self)
        # custom slots connections
        # one way to connect signal/slot connection
        self.apply_but.connect(self.apply_but, QtCore.SIGNAL("released()"), self.apply)
        # second way to build connection
        #QtCore.QObject.connect(self.apply_but, QtCore.SIGNAL("released()"), self.apply)


def main(argv):
    # create Qt application
    app = QtGui.QApplication(argv, True)

    # create main window
    wnd = MainWindow()  # classname
    wnd.show()
    wnd2 = MainWindow()  # classname
    wnd2.show()
    # Connect signal for app finish
    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))

    # Start the app up
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
'''
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = bidirUI.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
'''