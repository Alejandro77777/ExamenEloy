# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Jan 10 19:44:22 2017
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(294, 550)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.lineEdit_00 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_00.setGeometry(QtCore.QRect(20, 10, 61, 61))
        self.lineEdit_00.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit_00.setFont(font)
        self.lineEdit_00.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_00.setText(_fromUtf8(""))
        self.lineEdit_00.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_00.setObjectName(_fromUtf8("lineEdit_00"))
        self.lineEdit_01 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_01.setGeometry(QtCore.QRect(80, 10, 61, 61))
        self.lineEdit_01.setStyleSheet(_fromUtf8("background-color:rgb(220, 220, 220);\n"
"border-radius:10px;"))
        self.lineEdit_01.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_01.setObjectName(_fromUtf8("lineEdit_01"))
        self.lineEdit_10 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(20, 70, 61, 61))
        self.lineEdit_10.setStyleSheet(_fromUtf8("background-color:rgb(220, 220, 220);\n"
"border-radius:10px;"))
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(80, 70, 61, 61))
        self.lineEdit_11.setText(_fromUtf8(""))
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_20 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(20, 140, 61, 61))
        self.lineEdit_20.setText(_fromUtf8(""))
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.lineEdit_21 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_21.setGeometry(QtCore.QRect(80, 140, 61, 61))
        self.lineEdit_21.setText(_fromUtf8(""))
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.lineEdit_30 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_30.setGeometry(QtCore.QRect(20, 200, 61, 61))
        self.lineEdit_30.setText(_fromUtf8(""))
        self.lineEdit_30.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.lineEdit_31 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_31.setGeometry(QtCore.QRect(80, 200, 61, 61))
        self.lineEdit_31.setStyleSheet(_fromUtf8("background-color:rgb(220, 220, 220);\n"
"border-radius:10px;"))
        self.lineEdit_31.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_31.setObjectName(_fromUtf8("lineEdit_31"))
        self.lineEdit_02 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_02.setGeometry(QtCore.QRect(150, 10, 61, 61))
        self.lineEdit_02.setStyleSheet(_fromUtf8("background-color:rgb(220, 220, 220);\n"
"border-radius:10px;"))
        self.lineEdit_02.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_02.setObjectName(_fromUtf8("lineEdit_02"))
        self.lineEdit_03 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_03.setGeometry(QtCore.QRect(210, 10, 61, 61))
        self.lineEdit_03.setText(_fromUtf8(""))
        self.lineEdit_03.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_03.setObjectName(_fromUtf8("lineEdit_03"))
        self.lineEdit_12 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(150, 70, 61, 61))
        self.lineEdit_12.setText(_fromUtf8(""))
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(210, 70, 61, 61))
        self.lineEdit_13.setText(_fromUtf8(""))
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_22 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_22.setGeometry(QtCore.QRect(150, 140, 61, 61))
        self.lineEdit_22.setText(_fromUtf8(""))
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.lineEdit_23 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_23.setGeometry(QtCore.QRect(210, 140, 61, 61))
        self.lineEdit_23.setStyleSheet(_fromUtf8("background-color:rgb(220, 220, 220);\n"
"border-radius:10px;"))
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.lineEdit_32 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_32.setGeometry(QtCore.QRect(150, 200, 61, 61))
        self.lineEdit_32.setStyleSheet(_fromUtf8("background-color:rgb(220, 220, 220);\n"
"border-radius:10px;"))
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_32.setObjectName(_fromUtf8("lineEdit_32"))
        self.lineEdit_33 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_33.setGeometry(QtCore.QRect(210, 200, 61, 61))
        self.lineEdit_33.setText(_fromUtf8(""))
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_33.setObjectName(_fromUtf8("lineEdit_33"))
        self.lineEdit_44 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_44.setGeometry(QtCore.QRect(40, 270, 221, 30))
        self.lineEdit_44.setObjectName(_fromUtf8("lineEdit_44"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 300, 71, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 300, 141, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lineEdit_01.setText(_translate("MainWindow", "1", None))
        self.lineEdit_10.setText(_translate("MainWindow", "2", None))
        self.lineEdit_31.setText(_translate("MainWindow", "2", None))
        self.lineEdit_02.setText(_translate("MainWindow", "3", None))
        self.lineEdit_23.setText(_translate("MainWindow", "3", None))
        self.lineEdit_32.setText(_translate("MainWindow", "1", None))
        self.pushButton.setText(_translate("MainWindow", "Reset", None))
        self.pushButton_2.setText(_translate("MainWindow", "Comprova sudoku", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

