# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bidirUI.ui'
#
# Created: Wed May 28 19:02:10 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 430)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Singapore))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 661, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_bus = QtGui.QWidget()
        self.tab_bus.setObjectName(_fromUtf8("tab_bus"))
        self.horizontalSlider_vdc_ref_bus = QtGui.QSlider(self.tab_bus)
        self.horizontalSlider_vdc_ref_bus.setGeometry(QtCore.QRect(70, 30, 521, 29))
        self.horizontalSlider_vdc_ref_bus.setMinimum(30000)
        self.horizontalSlider_vdc_ref_bus.setMaximum(40000)
        self.horizontalSlider_vdc_ref_bus.setProperty("value", 38000)
        self.horizontalSlider_vdc_ref_bus.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_vdc_ref_bus.setObjectName(_fromUtf8("horizontalSlider_vdc_ref_bus"))
        self.horizontalSlider_iq_ref_bus = QtGui.QSlider(self.tab_bus)
        self.horizontalSlider_iq_ref_bus.setGeometry(QtCore.QRect(70, 100, 521, 29))
        self.horizontalSlider_iq_ref_bus.setMaximum(2000)
        self.horizontalSlider_iq_ref_bus.setProperty("value", 1000)
        self.horizontalSlider_iq_ref_bus.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_iq_ref_bus.setObjectName(_fromUtf8("horizontalSlider_iq_ref_bus"))
        self.label_25 = QtGui.QLabel(self.tab_bus)
        self.label_25.setGeometry(QtCore.QRect(40, 70, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.tab_bus)
        self.label_26.setGeometry(QtCore.QRect(40, 140, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.tab_bus)
        self.label_27.setGeometry(QtCore.QRect(580, 140, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.tab_bus)
        self.label_28.setGeometry(QtCore.QRect(580, 70, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_33 = QtGui.QLabel(self.tab_bus)
        self.label_33.setGeometry(QtCore.QRect(210, 70, 110, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.iq_ref_bus = QtGui.QLabel(self.tab_bus)
        self.iq_ref_bus.setGeometry(QtCore.QRect(340, 140, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.iq_ref_bus.setFont(font)
        self.iq_ref_bus.setObjectName(_fromUtf8("iq_ref_bus"))
        self.vdc_ref_bus = QtGui.QLabel(self.tab_bus)
        self.vdc_ref_bus.setGeometry(QtCore.QRect(330, 70, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vdc_ref_bus.setFont(font)
        self.vdc_ref_bus.setObjectName(_fromUtf8("vdc_ref_bus"))
        self.label_36 = QtGui.QLabel(self.tab_bus)
        self.label_36.setGeometry(QtCore.QRect(220, 140, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.pushButton_low_vdc_bus = QtGui.QPushButton(self.tab_bus)
        self.pushButton_low_vdc_bus.setGeometry(QtCore.QRect(10, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_low_vdc_bus.setFont(font)
        self.pushButton_low_vdc_bus.setObjectName(_fromUtf8("pushButton_low_vdc_bus"))
        self.pushButton_raise_vdc_bus = QtGui.QPushButton(self.tab_bus)
        self.pushButton_raise_vdc_bus.setGeometry(QtCore.QRect(600, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_raise_vdc_bus.setFont(font)
        self.pushButton_raise_vdc_bus.setObjectName(_fromUtf8("pushButton_raise_vdc_bus"))
        self.pushButton_low_iq_bus = QtGui.QPushButton(self.tab_bus)
        self.pushButton_low_iq_bus.setGeometry(QtCore.QRect(10, 90, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_low_iq_bus.setFont(font)
        self.pushButton_low_iq_bus.setObjectName(_fromUtf8("pushButton_low_iq_bus"))
        self.pushButton_raise_iq_bus = QtGui.QPushButton(self.tab_bus)
        self.pushButton_raise_iq_bus.setGeometry(QtCore.QRect(600, 90, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_raise_iq_bus.setFont(font)
        self.pushButton_raise_iq_bus.setObjectName(_fromUtf8("pushButton_raise_iq_bus"))
        self.label_35 = QtGui.QLabel(self.tab_bus)
        self.label_35.setGeometry(QtCore.QRect(380, 140, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_41 = QtGui.QLabel(self.tab_bus)
        self.label_41.setGeometry(QtCore.QRect(390, 70, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.tabWidget.addTab(self.tab_bus, _fromUtf8(""))
        self.tab_pow = QtGui.QWidget()
        self.tab_pow.setObjectName(_fromUtf8("tab_pow"))
        self.horizontalSlider_iq_ref_pow = QtGui.QSlider(self.tab_pow)
        self.horizontalSlider_iq_ref_pow.setGeometry(QtCore.QRect(70, 100, 521, 29))
        self.horizontalSlider_iq_ref_pow.setMinimum(0)
        self.horizontalSlider_iq_ref_pow.setMaximum(2000)
        self.horizontalSlider_iq_ref_pow.setProperty("value", 1000)
        self.horizontalSlider_iq_ref_pow.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_iq_ref_pow.setObjectName(_fromUtf8("horizontalSlider_iq_ref_pow"))
        self.horizontalSlider_id_ref_pow = QtGui.QSlider(self.tab_pow)
        self.horizontalSlider_id_ref_pow.setGeometry(QtCore.QRect(70, 30, 521, 29))
        self.horizontalSlider_id_ref_pow.setMaximum(2000)
        self.horizontalSlider_id_ref_pow.setProperty("value", 1000)
        self.horizontalSlider_id_ref_pow.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_id_ref_pow.setObjectName(_fromUtf8("horizontalSlider_id_ref_pow"))
        self.label_29 = QtGui.QLabel(self.tab_pow)
        self.label_29.setGeometry(QtCore.QRect(580, 140, 62, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.tab_pow)
        self.label_30.setGeometry(QtCore.QRect(40, 140, 62, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.tab_pow)
        self.label_31.setGeometry(QtCore.QRect(40, 70, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.tab_pow)
        self.label_32.setGeometry(QtCore.QRect(580, 70, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.id_ref_pow = QtGui.QLabel(self.tab_pow)
        self.id_ref_pow.setGeometry(QtCore.QRect(360, 70, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.id_ref_pow.setFont(font)
        self.id_ref_pow.setObjectName(_fromUtf8("id_ref_pow"))
        self.iq_ref_pow = QtGui.QLabel(self.tab_pow)
        self.iq_ref_pow.setGeometry(QtCore.QRect(360, 140, 50, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.iq_ref_pow.setFont(font)
        self.iq_ref_pow.setObjectName(_fromUtf8("iq_ref_pow"))
        self.label_39 = QtGui.QLabel(self.tab_pow)
        self.label_39.setGeometry(QtCore.QRect(240, 70, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.label_40 = QtGui.QLabel(self.tab_pow)
        self.label_40.setGeometry(QtCore.QRect(240, 140, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.pushButton_raise_id_pow = QtGui.QPushButton(self.tab_pow)
        self.pushButton_raise_id_pow.setGeometry(QtCore.QRect(600, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_raise_id_pow.setFont(font)
        self.pushButton_raise_id_pow.setObjectName(_fromUtf8("pushButton_raise_id_pow"))
        self.pushButton_low_id_pow = QtGui.QPushButton(self.tab_pow)
        self.pushButton_low_id_pow.setGeometry(QtCore.QRect(10, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_low_id_pow.setFont(font)
        self.pushButton_low_id_pow.setObjectName(_fromUtf8("pushButton_low_id_pow"))
        self.pushButton_low_iq_pow = QtGui.QPushButton(self.tab_pow)
        self.pushButton_low_iq_pow.setGeometry(QtCore.QRect(10, 90, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_low_iq_pow.setFont(font)
        self.pushButton_low_iq_pow.setObjectName(_fromUtf8("pushButton_low_iq_pow"))
        self.pushButton_raise_iq_pow = QtGui.QPushButton(self.tab_pow)
        self.pushButton_raise_iq_pow.setGeometry(QtCore.QRect(600, 90, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_raise_iq_pow.setFont(font)
        self.pushButton_raise_iq_pow.setObjectName(_fromUtf8("pushButton_raise_iq_pow"))
        self.label_42 = QtGui.QLabel(self.tab_pow)
        self.label_42.setGeometry(QtCore.QRect(410, 140, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_43 = QtGui.QLabel(self.tab_pow)
        self.label_43.setGeometry(QtCore.QRect(410, 70, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.tabWidget.addTab(self.tab_pow, _fromUtf8(""))
        self.apply_but = QtGui.QPushButton(Form)
        self.apply_but.setGeometry(QtCore.QRect(690, 50, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.apply_but.setFont(font)
        self.apply_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.apply_but.setObjectName(_fromUtf8("apply_but"))
        self.start_but = QtGui.QPushButton(Form)
        self.start_but.setEnabled(False)
        self.start_but.setGeometry(QtCore.QRect(690, 140, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.start_but.setFont(font)
        self.start_but.setObjectName(_fromUtf8("start_but"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(13, 243, 781, 181))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(158, 255, 165);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.status = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.status.setFont(font)
        self.status.setStyleSheet(_fromUtf8("background-color: rgb(158, 255, 165);"))
        self.status.setObjectName(_fromUtf8("status"))
        self.gridLayout.addWidget(self.status, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.fault_type = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fault_type.setFont(font)
        self.fault_type.setObjectName(_fromUtf8("fault_type"))
        self.gridLayout.addWidget(self.fault_type, 0, 4, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 0, 5, 1, 1)
        self.vdc_v = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vdc_v.setFont(font)
        self.vdc_v.setObjectName(_fromUtf8("vdc_v"))
        self.gridLayout.addWidget(self.vdc_v, 0, 6, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.frequency = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.frequency.setFont(font)
        self.frequency.setObjectName(_fromUtf8("frequency"))
        self.gridLayout.addWidget(self.frequency, 1, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("background-color: rgb(251, 255, 201);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)
        self.current_a_a = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.current_a_a.setFont(font)
        self.current_a_a.setStyleSheet(_fromUtf8("background-color: rgb(251, 255, 201);"))
        self.current_a_a.setObjectName(_fromUtf8("current_a_a"))
        self.gridLayout.addWidget(self.current_a_a, 1, 4, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("background-color: rgb(184, 255, 250);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 1, 5, 1, 1)
        self.voltage_a_v = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.voltage_a_v.setFont(font)
        self.voltage_a_v.setStyleSheet(_fromUtf8("background-color: rgb(184, 255, 250);"))
        self.voltage_a_v.setObjectName(_fromUtf8("voltage_a_v"))
        self.gridLayout.addWidget(self.voltage_a_v, 1, 6, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.real_power_w = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.real_power_w.setFont(font)
        self.real_power_w.setObjectName(_fromUtf8("real_power_w"))
        self.gridLayout.addWidget(self.real_power_w, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("background-color: rgb(251, 255, 201);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)
        self.current_b_a = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.current_b_a.setFont(font)
        self.current_b_a.setStyleSheet(_fromUtf8("background-color: rgb(251, 255, 201);"))
        self.current_b_a.setObjectName(_fromUtf8("current_b_a"))
        self.gridLayout.addWidget(self.current_b_a, 2, 4, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("background-color: rgb(184, 255, 250);"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 2, 5, 1, 1)
        self.voltage_b_v = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.voltage_b_v.setFont(font)
        self.voltage_b_v.setStyleSheet(_fromUtf8("background-color: rgb(184, 255, 250);"))
        self.voltage_b_v.setObjectName(_fromUtf8("voltage_b_v"))
        self.gridLayout.addWidget(self.voltage_b_v, 2, 6, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 2)
        self.reactive_power_var = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reactive_power_var.setFont(font)
        self.reactive_power_var.setObjectName(_fromUtf8("reactive_power_var"))
        self.gridLayout.addWidget(self.reactive_power_var, 3, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("background-color: rgb(251, 255, 201);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 3, 1, 1)
        self.current_c_a = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.current_c_a.setFont(font)
        self.current_c_a.setStyleSheet(_fromUtf8("background-color: rgb(251, 255, 201);"))
        self.current_c_a.setObjectName(_fromUtf8("current_c_a"))
        self.gridLayout.addWidget(self.current_c_a, 3, 4, 1, 1)
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(_fromUtf8("background-color: rgb(184, 255, 250);"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 3, 5, 1, 1)
        self.voltage_c_v = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.voltage_c_v.setFont(font)
        self.voltage_c_v.setStyleSheet(_fromUtf8("background-color: rgb(184, 255, 250);"))
        self.voltage_c_v.setObjectName(_fromUtf8("voltage_c_v"))
        self.gridLayout.addWidget(self.voltage_c_v, 3, 6, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.horizontalSlider_vdc_ref_bus, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               Form.vdc_ref_bus_changed)
        QtCore.QObject.connect(self.horizontalSlider_iq_ref_bus, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               Form.iq_ref_bus_changed)
        QtCore.QObject.connect(self.apply_but, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.apply)
        QtCore.QObject.connect(self.start_but, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.start_or_stop)
        QtCore.QObject.connect(self.horizontalSlider_id_ref_pow, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               Form.id_ref_pow_changed)
        QtCore.QObject.connect(self.horizontalSlider_iq_ref_pow, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               Form.iq_ref_pow_changed)
        QtCore.QObject.connect(self.pushButton_low_vdc_bus, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.low_vdc_bus)
        QtCore.QObject.connect(self.pushButton_low_iq_bus, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.low_iq_bus)
        QtCore.QObject.connect(self.pushButton_raise_iq_bus, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.raise_iq_bus)
        QtCore.QObject.connect(self.pushButton_raise_vdc_bus, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.raise_vdc_bus)
        QtCore.QObject.connect(self.pushButton_low_id_pow, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.low_id_pow)
        QtCore.QObject.connect(self.pushButton_low_iq_pow, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.low_iq_pow)
        QtCore.QObject.connect(self.pushButton_raise_id_pow, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.raise_id_pow)
        QtCore.QObject.connect(self.pushButton_raise_iq_pow, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.raise_iq_pow)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), Form.select_mode)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.tabWidget, self.apply_but)
        Form.setTabOrder(self.apply_but, self.start_but)
        Form.setTabOrder(self.start_but, self.horizontalSlider_vdc_ref_bus)
        Form.setTabOrder(self.horizontalSlider_vdc_ref_bus, self.horizontalSlider_iq_ref_bus)
        Form.setTabOrder(self.horizontalSlider_iq_ref_bus, self.pushButton_low_vdc_bus)
        Form.setTabOrder(self.pushButton_low_vdc_bus, self.pushButton_raise_vdc_bus)
        Form.setTabOrder(self.pushButton_raise_vdc_bus, self.pushButton_low_iq_bus)
        Form.setTabOrder(self.pushButton_low_iq_bus, self.pushButton_raise_iq_bus)
        Form.setTabOrder(self.pushButton_raise_iq_bus, self.pushButton_raise_id_pow)
        Form.setTabOrder(self.pushButton_raise_id_pow, self.pushButton_low_id_pow)
        Form.setTabOrder(self.pushButton_low_id_pow, self.pushButton_low_iq_pow)
        Form.setTabOrder(self.pushButton_low_iq_pow, self.pushButton_raise_iq_pow)
        Form.setTabOrder(self.pushButton_raise_iq_pow, self.horizontalSlider_id_ref_pow)
        Form.setTabOrder(self.horizontalSlider_id_ref_pow, self.horizontalSlider_iq_ref_pow)

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QtGui.QApplication.translate("Form", "Bi-directional Converter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("Form", "300 V", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("Form", "-10 A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("Form", "10 A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("Form", "400 V", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(
            QtGui.QApplication.translate("Form", "Vdc Reference:", None, QtGui.QApplication.UnicodeUTF8))
        self.iq_ref_bus.setText(QtGui.QApplication.translate("Form", "0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.vdc_ref_bus.setText(QtGui.QApplication.translate("Form", "380.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(
            QtGui.QApplication.translate("Form", "Iq Reference:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_low_vdc_bus.setText(
            QtGui.QApplication.translate("Form", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_raise_vdc_bus.setText(
            QtGui.QApplication.translate("Form", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_low_iq_bus.setText(
            QtGui.QApplication.translate("Form", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_raise_iq_bus.setText(
            QtGui.QApplication.translate("Form", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("Form", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate("Form", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bus),
                                  QtGui.QApplication.translate("Form", "Bus Monitoring Mode", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("Form", "10 A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("Form", "-10 A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("Form", "-10 A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("Form", "10 A", None, QtGui.QApplication.UnicodeUTF8))
        self.id_ref_pow.setText(QtGui.QApplication.translate("Form", "0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.iq_ref_pow.setText(QtGui.QApplication.translate("Form", "0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(
            QtGui.QApplication.translate("Form", "Id Reference:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(
            QtGui.QApplication.translate("Form", "Iq Reference:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_raise_id_pow.setText(
            QtGui.QApplication.translate("Form", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_low_id_pow.setText(
            QtGui.QApplication.translate("Form", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_low_iq_pow.setText(
            QtGui.QApplication.translate("Form", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_raise_iq_pow.setText(
            QtGui.QApplication.translate("Form", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("Form", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("Form", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pow),
                                  QtGui.QApplication.translate("Form", "Power Dispatching Mode", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        self.apply_but.setText(QtGui.QApplication.translate("Form", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.start_but.setText(QtGui.QApplication.translate("Form", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.status.setText(QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Fault Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.fault_type.setText(QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "Vdc(V):", None, QtGui.QApplication.UnicodeUTF8))
        self.vdc_v.setText(QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Frequency:", None, QtGui.QApplication.UnicodeUTF8))
        self.frequency.setText(QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(
            QtGui.QApplication.translate("Form", "Current A(A):", None, QtGui.QApplication.UnicodeUTF8))
        self.current_a_a.setText(QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(
            QtGui.QApplication.translate("Form", "Voltage A(V):", None, QtGui.QApplication.UnicodeUTF8))
        self.voltage_a_v.setText(QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(
            QtGui.QApplication.translate("Form", "Real Power(W):", None, QtGui.QApplication.UnicodeUTF8))
        self.real_power_w.setText(
            QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(
            QtGui.QApplication.translate("Form", "Current B(A):", None, QtGui.QApplication.UnicodeUTF8))
        self.current_b_a.setText(QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(
            QtGui.QApplication.translate("Form", "Voltage B(V):", None, QtGui.QApplication.UnicodeUTF8))
        self.voltage_b_v.setText(QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(
            QtGui.QApplication.translate("Form", "Reactive Power(var):", None, QtGui.QApplication.UnicodeUTF8))
        self.reactive_power_var.setText(
            QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(
            QtGui.QApplication.translate("Form", "Current C(A):", None, QtGui.QApplication.UnicodeUTF8))
        self.current_c_a.setText(QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(
            QtGui.QApplication.translate("Form", "Voltage C(V):", None, QtGui.QApplication.UnicodeUTF8))
        self.voltage_c_v.setText(QtGui.QApplication.translate("Form", "No Value", None, QtGui.QApplication.UnicodeUTF8))
