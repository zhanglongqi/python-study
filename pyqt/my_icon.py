# icon.py
import sys
from PyQt4 import QtGui


class My_Widget(QtGui.QWidget):

    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        #set icon for widget
        self.setWindowIcon(QtGui.QIcon('icons/earth.gif'))
        #set tool tip for widget
        self.setToolTip("I'm <b>tooltip</b> of widget. <br>""Nice to meet you.")
      #  QtGui.QToolTip.setFont(QtGui.QFont('Ubuntu', 15))
        self.centre()

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',"Are you sure to quit?",
                                           QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def centre(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(screen.width()/2-size.width()/2, (screen.height()-self.height())/2)

app = QtGui.QApplication(sys.argv)
my = My_Widget()

my.show()
app.exec_()
sys.exit(app.exec_())