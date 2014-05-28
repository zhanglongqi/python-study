__author__ = 'longqi'
import sys
from PyQt4 import QtCore, QtGui

from bidirUI import Ui_Form

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
Bus_Monitoring_mode = 0
Power_Dispatchin_mode = 1


class MainWindow(QtGui.QWidget, Ui_Form):
    # custom slot
    def vdc_ref_bus_changed(self):
        print 'vdc_ref_bus_changed'
        self.vdc_ref_bus.setText(QtCore.QString.number(self.horizontalSlider_vdc_ref_bus.value() / 100.0))

    def iq_ref_bus_changed(self):
        print 'iq_ref_bus_changed'
        self.iq_ref_bus.setText(QtCore.QString.number((self.horizontalSlider_iq_ref_bus.value() - 1000) / 100.0))

    def apply(self):
        print 'apply'
        if self.tabWidget.currentIndex() == Bus_Monitoring_mode:
            self.tabWidget.setTabEnabled(Power_Dispatchin_mode, False)
        elif self.tabWidget.currentIndex() == Power_Dispatchin_mode:
            self.tabWidget.setTabEnabled(Bus_Monitoring_mode, False)
        self.start_but.setEnabled(True)

    def start_or_stop(self):
        print 'start_or_stop'
        if self.start_but.text() == 'Start':
            self.start_but.setText('Stop')
        elif self.start_but.text() == 'Stop':
            self.start_but.setText('Start')
            self.tabWidget.setTabEnabled(Bus_Monitoring_mode, True)
            self.tabWidget.setTabEnabled(Power_Dispatchin_mode, True)
            self.start_but.setEnabled(False)

    def id_ref_pow_changed(self):
        print 'id_ref_pow_changed'
        self.id_ref_pow.setText(QtCore.QString.number((self.horizontalSlider_id_ref_pow.value() - 1000) / 100.0))

    def iq_ref_pow_changed(self):
        print 'iq_ref_pow_changed'
        self.iq_ref_pow.setText(QtCore.QString.number((self.horizontalSlider_iq_ref_pow.value() - 1000) / 100.0))

    def low_vdc_bus(self):
        print 'low_vdc_bus'
        self.horizontalSlider_vdc_ref_bus.triggerAction(QtGui.QAbstractSlider.SliderSingleStepSub)

    def low_iq_bus(self):
        print 'low_iq_bus'
        self.horizontalSlider_iq_ref_bus.triggerAction(QtGui.QAbstractSlider.SliderSingleStepSub)

    def raise_iq_bus(self):
        print 'raise_iq_bus'
        self.horizontalSlider_iq_ref_bus.triggerAction(QtGui.QAbstractSlider.SliderSingleStepAdd)

    def raise_vdc_bus(self):
        print 'raise_vdc_bus'
        self.horizontalSlider_vdc_ref_bus.triggerAction(QtGui.QAbstractSlider.SliderSingleStepAdd)

    def low_id_pow(self):
        print 'low_id_pow'
        self.horizontalSlider_id_ref_pow.triggerAction(QtGui.QAbstractSlider.SliderSingleStepSub)

    def low_iq_pow(self):
        print 'low_iq_pow'
        self.horizontalSlider_iq_ref_pow.triggerAction(QtGui.QAbstractSlider.SliderSingleStepSub)

    def raise_id_pow(self):
        print 'raise_id_pow'
        self.horizontalSlider_id_ref_pow.triggerAction(QtGui.QAbstractSlider.SliderSingleStepAdd)

    def raise_iq_pow(self):
        print 'raise_iq_pow'
        self.horizontalSlider_iq_ref_pow.triggerAction(QtGui.QAbstractSlider.SliderSingleStepAdd)

    def select_mode(self, index):
        print 'select_mode', index

    '''
    def make_conn(self):
        QtCore.QObject.connect(self.horizontalSlider_vdc_ref_bus,
                               QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.vdc_ref_bus_changed)
        QtCore.QObject.connect(self.horizontalSlider_iq_ref_bus,
                               QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.iq_ref_bus_changed)
        QtCore.QObject.connect(self.apply_but, QtCore.SIGNAL(_fromUtf8("clicked()")), self.apply)
        QtCore.QObject.connect(self.start_but, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_or_stop)
        QtCore.QObject.connect(self.horizontalSlider_id_ref_pow,
                               QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.id_ref_pow_changed)
        QtCore.QObject.connect(self.horizontalSlider_iq_ref_pow,
                               QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.iq_ref_pow_changed)
        QtCore.QObject.connect(self.pushButton_low_vdc_bus, QtCore.SIGNAL(_fromUtf8("clicked()")), self.low_vdc_bus)
        QtCore.QObject.connect(self.pushButton_low_iq_bus, QtCore.SIGNAL(_fromUtf8("clicked()")), self.low_iq_bus)
        QtCore.QObject.connect(self.pushButton_raise_iq_bus, QtCore.SIGNAL(_fromUtf8("clicked()")), self.raise_iq_bus)
        QtCore.QObject.connect(self.pushButton_raise_vdc_bus, QtCore.SIGNAL(_fromUtf8("clicked()")), self.raise_vdc_bus)
        QtCore.QObject.connect(self.pushButton_low_id_pow, QtCore.SIGNAL(_fromUtf8("clicked()")), self.low_id_pow)
        QtCore.QObject.connect(self.pushButton_low_iq_pow, QtCore.SIGNAL(_fromUtf8("clicked()")), self.low_iq_pow)
        QtCore.QObject.connect(self.pushButton_raise_id_pow, QtCore.SIGNAL(_fromUtf8("clicked()")), self.raise_id_pow)
        QtCore.QObject.connect(self.pushButton_raise_iq_pow, QtCore.SIGNAL(_fromUtf8("clicked()")), self.raise_iq_pow)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), self.select_mode)
    '''

    def __init__(self):
        QtGui.QWidget.__init__(self)

        # set up User Interface (widgets, layout...)
        self.setupUi(self)
        # custom slots connections
        # one way to connect signal/slot connection
        #self.apply_but.connect(self.apply_but, QtCore.SIGNAL("released()"), self.apply)
        # second way to build connection
        #QtCore.QObject.connect(self.apply_but, QtCore.SIGNAL("released()"), self.apply)
        # third way to build connection
        #self.apply_but.clicked.connect(self.vdc_id_ref_changed)
        # self.make_conn()


def main(argv):
    # create Qt application
    app = QtGui.QApplication(argv)

    # create main window
    wnd = MainWindow()  # classname
    wnd.show()

    # Connect signal for app finish
    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))

    # Start the app up
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
    print sys.argv
'''
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = bidirUI.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
'''