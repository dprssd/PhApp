# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_p(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choseButton = QtWidgets.QPushButton(self.centralwidget)
        self.choseButton.setGeometry(QtCore.QRect(990, 350, 81, 21))
        self.choseButton.setObjectName("choseButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(880, 350, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 1061, 344))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 10, 0, 1, 1)
        self.temp_BSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.temp_BSpinBox.setMinimumSize(QtCore.QSize(218, 20))
        self.temp_BSpinBox.setDecimals(4)
        self.temp_BSpinBox.setSingleStep(3.0)
        self.temp_BSpinBox.setObjectName("temp_BSpinBox")
        self.gridLayout_2.addWidget(self.temp_BSpinBox, 11, 0, 1, 1)
        self.temp_k1SpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.temp_k1SpinBox.setDecimals(5)
        self.temp_k1SpinBox.setObjectName("temp_k1SpinBox")
        self.gridLayout_2.addWidget(self.temp_k1SpinBox, 14, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 12, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)
        self.iscSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.iscSpinBox.setObjectName("iscSpinBox")
        self.gridLayout_2.addWidget(self.iscSpinBox, 9, 0, 1, 1)
        self.squarePanSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.squarePanSpinBox.setObjectName("squarePanSpinBox")
        self.gridLayout_2.addWidget(self.squarePanSpinBox, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)
        self.kpdSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.kpdSpinBox.setObjectName("kpdSpinBox")
        self.gridLayout_2.addWidget(self.kpdSpinBox, 7, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Название панели")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.changeButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.changeButton.setObjectName("changeButton")
        self.horizontalLayout.addWidget(self.changeButton)
        self.deleteButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action_Excel = QtWidgets.QAction(MainWindow)
        self.action_Excel.setObjectName("action_Excel")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_Excel_2 = QtWidgets.QAction(MainWindow)
        self.action_Excel_2.setObjectName("action_Excel_2")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_Excel)
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Панели"))
        self.choseButton.setText(_translate("MainWindow", "Выбрать"))
        self.cancelButton.setText(_translate("MainWindow", "Отменить"))
        self.label.setText(_translate("MainWindow", "Температурный коэффициент для P (B)"))
        self.label_2.setText(_translate("MainWindow", "Температурный коэффициент для I (k1)"))
        self.label_3.setText(_translate("MainWindow", "Название панели"))
        self.label_4.setText(_translate("MainWindow", "Общая площадь солнечных панелей (м^2)"))
        self.label_6.setText(_translate("MainWindow", "Ток КЗ (А)"))
        self.label_5.setText(_translate("MainWindow", "Паспортное значение КПД (%)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Площадь с.н.(м^2)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "КПД (%)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ток КЗ (А)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Темп. коэф. для P"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Темп. коэф. для I"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.changeButton.setText(_translate("MainWindow", "Изменить"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action_Excel.setText(_translate("MainWindow", "Импорт Excel"))
        self.action.setText(_translate("MainWindow", "Импорт из БД"))
        self.action_Excel_2.setText(_translate("MainWindow", "Сохранить Excel"))
        self.action_2.setText(_translate("MainWindow", "Сохранить"))
        self.action_3.setText(_translate("MainWindow", "Сохранить"))
