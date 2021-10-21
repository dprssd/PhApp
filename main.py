import invertor_d
import invertor_add
import design_1
import panel_d
import sys

from config import  host, user, password, db_name
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget


class panelWin(QtWidgets.QMainWindow, panel_d.Ui_MainWindow_p, invertor_d.Ui_MainWindow_i):
    def __init__(self, invertor_d_ui):
        nRowInv = 0
        super(panelWin, self).__init__()
        self.ui = panel_d.Ui_MainWindow_p()
        self.ui.setupUi(self)
        self.ui.tableWidget.setRowCount(nRowInv)
        self.ui.addButton.clicked.connect(self.addPan)
        self.ui.deleteButton.clicked.connect(self.deleteRow)
        self.ui.tableWidget.clicked.connect(self.tClick)
        self.ui.changeButton.clicked.connect(self.changeRow)
        self.ui.choseButton.clicked.connect(self.cClick)

        self.invertor_d_ui = invertor_d_ui

    def tClick(self):
        index = self.ui.tableWidget.selectionModel().currentIndex()
        self.ui.lineEdit.setText(self.ui.tableWidget.item(index.row(), 0).text())
        self.ui.squarePanSpinBox.setValue(float(self.ui.tableWidget.item(index.row(), 1).text()))
        self.ui.kpdSpinBox.setValue(float(self.ui.tableWidget.item(index.row(), 2).text()))
        self.ui.iscSpinBox.setValue(float(self.ui.tableWidget.item(index.row(), 3).text()))
        self.ui.temp_BSpinBox.setValue(float(self.ui.tableWidget.item(index.row(), 4).text()))
        self.ui.temp_k1SpinBox.setValue(float(self.ui.tableWidget.item(index.row(), 5).text()))

    def addPan(self):
        nRowInv = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(nRowInv + 1)
        a1 = QTableWidgetItem(self.ui.lineEdit.text())
        a2 = QTableWidgetItem(str(self.ui.squarePanSpinBox.value()))
        a3 = QTableWidgetItem(str(self.ui.kpdSpinBox.value()))
        a4 = QTableWidgetItem(str(self.ui.iscSpinBox.value()))
        a5 = QTableWidgetItem(str(self.ui.temp_BSpinBox.value()))
        a6 = QTableWidgetItem(str(self.ui.temp_k1SpinBox.value()))
        self.ui.tableWidget.setItem(int(nRowInv), 0, a1)
        self.ui.tableWidget.setItem(int(nRowInv), 1, a2)
        self.ui.tableWidget.setItem(int(nRowInv), 2, a3)
        self.ui.tableWidget.setItem(int(nRowInv), 3, a4)
        self.ui.tableWidget.setItem(int(nRowInv), 4, a5)
        self.ui.tableWidget.setItem(int(nRowInv), 5, a6)
        nRowInv += 1

    def deleteRow(self):
        index = self.ui.tableWidget.selectionModel().currentIndex()
        self.ui.tableWidget.removeRow(index.row())

    def changeRow(self):
        index = self.ui.tableWidget.selectionModel().currentIndex()
        a1 = QTableWidgetItem(self.ui.lineEdit.text())
        a2 = QTableWidgetItem(str(self.ui.squarePanSpinBox.value()))
        a3 = QTableWidgetItem(str(self.ui.kpdSpinBox.value()))
        a4 = QTableWidgetItem(str(self.ui.iscSpinBox.value()))
        a5 = QTableWidgetItem(str(self.ui.temp_BSpinBox.value()))
        a6 = QTableWidgetItem(str(self.ui.temp_k1SpinBox.value()))
        self.ui.tableWidget.setItem(int(index.row()), 0, a1)
        self.ui.tableWidget.setItem(int(index.row()), 1, a2)
        self.ui.tableWidget.setItem(int(index.row()), 2, a3)
        self.ui.tableWidget.setItem(int(index.row()), 3, a4)
        self.ui.tableWidget.setItem(int(index.row()), 4, a5)
        self.ui.tableWidget.setItem(int(index.row()), 5, a6)

    def cClick(self):
        x = 0
        self.invertor_d_ui.comboBox_2.clear()
        while x < int(self.ui.tableWidget.rowCount()):
            self.invertor_d_ui.comboBox_2.addItem(self.ui.tableWidget.item(x, 0).text())
            x += 1

    def closeEvent(self, event):
        x = 0
        self.invertor_d_ui.comboBox_2.clear()
        while x < int(self.ui.tableWidget.rowCount()):
            self.invertor_d_ui.comboBox_2.addItem(self.ui.tableWidget.item(x, 0).text())
            x += 1


#Выбор инвертора
class invAdd(QtWidgets.QMainWindow, invertor_add.Ui_MainWindow_inv_add, panel_d.Ui_MainWindow_p, invertor_d.Ui_MainWindow_i):
    def __init__(self, invertor_d_ui):
        super(invAdd, self).__init__()
        self.invertor_d_ui = invertor_d_ui
        self.ui = invertor_add.Ui_MainWindow_inv_add()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.addPan)
        self.ui.deleteButton.clicked.connect(self.deleteRow)
        self.ui.tableWidget.clicked.connect(self.tClick)
        self.ui.changeButton.clicked.connect(self.changeRow)
        self.ui.choseButton.clicked.connect(self.cClick)

    def addPan(self):
        nRowInv = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(nRowInv + 1)
        a1 = QTableWidgetItem(str(self.ui.numSpinBox.value()))
        a2 = QTableWidgetItem(str(self.ui.lineEdit.text()))
        a3 = QTableWidgetItem(str(self.ui.numSpinBox_2.value()))
        self.ui.tableWidget.setItem(int(nRowInv), 0, a1)
        self.ui.tableWidget.setItem(int(nRowInv), 1, a2)
        self.ui.tableWidget.setItem(int(nRowInv), 2, a3)
        nRowInv += 1

    def deleteRow(self):
        index = self.ui.tableWidget.selectionModel().currentIndex()
        self.ui.tableWidget.removeRow(index.row())

    def tClick(self):
        index = self.ui.tableWidget.selectionModel().currentIndex()
        self.ui.numSpinBox.setValue(float(self.ui.tableWidget.item(index.row(), 0).text()))
        self.ui.lineEdit.setText(self.ui.tableWidget.item(index.row(), 1).text())
        self.ui.numSpinBox_2.setValue(float(self.ui.tableWidget.item(index.row(), 2).text()))

    def changeRow(self):
        index = self.ui.tableWidget.selectionModel().currentIndex()
        a1 = QTableWidgetItem(str(self.ui.numSpinBox.value()))
        a2 = QTableWidgetItem(str(self.ui.lineEdit.text()))
        a3 = QTableWidgetItem(str(self.ui.numSpinBox_2.value()))
        self.ui.tableWidget.setItem(int(index.row()), 0, a1)
        self.ui.tableWidget.setItem(int(index.row()), 1, a2)
        self.ui.tableWidget.setItem(int(index.row()), 2, a3)

    def cClick(self):
        x = 0
        self.invertor_d_ui.comboBox.clear()
        while x < int(self.ui.tableWidget.rowCount()):
            self.invertor_d_ui.comboBox.addItem(self.ui.tableWidget.item(x, 1).text())
            x += 1

    def closeEvent(self, event):
        x = 0
        self.invertor_d_ui.comboBox.clear()
        while x < int(self.ui.tableWidget.rowCount()):
            self.invertor_d_ui.comboBox.addItem(self.ui.tableWidget.item(x, 1).text())
            x += 1

class invertorWin(QtWidgets.QMainWindow, invertor_d.Ui_MainWindow_i, invertor_add.Ui_MainWindow_inv_add):
    def __init__(self):
        super(invertorWin, self).__init__()
        self.ui = invertor_d.Ui_MainWindow_i()
        self.panel = panelWin(self.ui)
        self.inv = invAdd(self.ui)
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.openPanel)
        self.ui.addButton.clicked.connect(self.addInv)
        self.ui.deleteButton.clicked.connect(self.deleteRow)
        self.ui.tableWidget.clicked.connect(self.tClick)
        self.ui.pushButton_2.clicked.connect(self.openInv)
        self.ui.changeButton.clicked.connect(self.changeRow)

    def tClick(self):
        index = self.ui.tableWidget.selectionModel().currentIndex()
        self.ui.numSpinBox.setValue(float(self.ui.tableWidget.item(index.row(), 3).text()))
        if (self.ui.tableWidget.item(index.row(), 1).text()) == 'Последовательное':
            self.ui.conRadioButton.setChecked(True)
        else:
            self.ui.parRadioButton.setChecked(True)

    def addInv(self):
        if self.ui.conRadioButton.isChecked():
            s = 'Последовательное'
        else:
            s = 'Параллельное'
        nRowInv = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(nRowInv + 1)
        a1 = QTableWidgetItem(str(self.ui.comboBox.currentText()))
        a2 = QTableWidgetItem(str(s))
        a3 = QTableWidgetItem(str(self.ui.comboBox_2.currentText()))
        a4 = QTableWidgetItem(str(self.ui.numSpinBox.value()))
        self.ui.tableWidget.setItem(int(nRowInv), 0, a1)
        self.ui.tableWidget.setItem(int(nRowInv), 1, a2)
        self.ui.tableWidget.setItem(int(nRowInv), 2, a3)
        self.ui.tableWidget.setItem(int(nRowInv), 3, a4)
        nRowInv += 1

    def deleteRow(self):
        index = self.ui.tableWidget.selectionModel().currentIndex()
        self.ui.tableWidget.removeRow(index.row())

    def changeRow(self):
        if self.ui.conRadioButton.isChecked():
            s = 'Последовательное'
        else:
            s = 'Параллельное'

        index = self.ui.tableWidget.selectionModel().currentIndex()
        a1 = QTableWidgetItem(str(self.ui.comboBox.currentText()))
        a2 = QTableWidgetItem(str(s))
        a3 = QTableWidgetItem(str(self.ui.comboBox_2.currentText()))
        a4 = QTableWidgetItem(str(self.ui.numSpinBox.value()))
        self.ui.tableWidget.setItem(int(index.row()), 0, a1)
        self.ui.tableWidget.setItem(int(index.row()), 1, a2)
        self.ui.tableWidget.setItem(int(index.row()), 2, a3)
        self.ui.tableWidget.setItem(int(index.row()), 3, a4)



    def changeInv(self):
        if self.ui.conRadioButton.isChecked():
            s = 'Последовательное'
        else:
            s = 'Параллельное'

        index = self.ui.tableWidget.selectionModel().currentIndex()
        a1 = QTableWidgetItem(str(self.ui.comboBox.currentText()))
        a2 = QTableWidgetItem(str(s))
        a3 = QTableWidgetItem(str(self.ui.comboBox_2.currentText()))
        a4 = QTableWidgetItem(str(self.ui.numSpinBox.value()))
        self.ui.tableWidget.setItem(int(index.row()), 0, a1)
        self.ui.tableWidget.setItem(int(index.row()), 1, a2)
        self.ui.tableWidget.setItem(int(index.row()), 2, a3)
        self.ui.tableWidget.setItem(int(index.row()), 4, a4)

    def openInv(self):
        self.inv.show()

    def openPanel(self):
        self.panel.show()



class mywindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.invertor = invertorWin()
        self.ui = design_1.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.openDialog)

    #        self.ui.pushButton.clicked.connect(self.calcAll)

    #    def calcAll(self):

    def openDialog(self):
        self.invertor.show()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
