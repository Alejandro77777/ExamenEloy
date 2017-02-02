import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

from exercici10 import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(Ventana, self).__init__(parent)
        self.setupUi(self)
        self.horizontalSlider_3.setValue(100)
        self.horizontalSlider_2.setValue(225)
        self.horizontalSlider.setValue(158)
        self.label_4.setText(str(self.horizontalSlider_3.value()))
        self.label_5.setText(str(self.horizontalSlider_2.value()))
        self.label_6.setText(str(self.horizontalSlider.value()))
        self.textEdit.setText("#64E19E")
        # Control button
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.paleta)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.sortir)
    
    def repinta(self):
        self.actualizar()
        self.label_7.setStyleSheet("background-color:"+self.textEdit.toPlainText()+";\nborder-radius: 10px;")

    def paleta(self):
        color = QColor(self.horizontalSlider_3.value(), self.horizontalSlider_2.value(), self.horizontalSlider.value())
        newcolor = QColorDialog.getColor(color)
        self.horizontalSlider_3.setValue(newcolor.red())
        self.horizontalSlider_2.setValue(newcolor.green())
        self.horizontalSlider.setValue(newcolor.blue())
        self.repinta()
    def actualizar(self):
        codigo  = "#"
        red = self.horizontalSlider_3.value()
        green = self.horizontalSlider_2.value()
        blue = self.horizontalSlider.value()
        valorRed=[]
        valorGreen=[]
        valorBlue=[]
        hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        if(red==0):
            codigo += "00"
        else:
            if(red < 16):
                codigo += "0"
                colorin=red%16
                valorRed.append(hex[colorin])
            else:
                while (red > 0):
                    colorin = red % 16
                    red = red/16
                    valorRed.append(hex[colorin])
                valorRed.reverse()
        for i in valorRed:
            codigo += str(i)
        if(green==0):
            codigo += "00"
        else:
            if(green < 16):
                codigo += "0"
                colorin=green%16
                valorGreen.append(hex[colorin])
            else:
                while (green > 0):
                    colorin = green % 16
                    green = green/16
                    valorGreen.append(hex[colorin])
                valorGreen.reverse()
        for i in valorGreen:
            codigo += str(i)
        if(blue==0):
            codigo += "00"
        else:
            if(blue < 16):
                codigo += "0"
                colorin=blue%16
                valorBlue.append(hex[colorin])
            else:
                while (blue > 0):
                    colorin = blue % 16
                    blue = blue/16
                    valorBlue.append(hex[colorin])
                valorBlue.reverse()
        for i in valorBlue:
            codigo += str(i)
        self.textEdit.setText(codigo)

    def sortir(self):
        app.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = Ventana()
    finestra.show()
    
    sys.exit(app.exec_())