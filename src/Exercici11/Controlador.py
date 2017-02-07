import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

from exercici66 import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    
    sudoku = []
    
    
    def __init__(self, parent = None):
        super(Ventana, self).__init__(parent)
        self.setupUi(self)
        # Control button
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.comprova)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.sortir)
        self.sudoku = [
        [str(""),1,3,str("")],
        [2,str(""),str(""),str("")],
        [str(""),str(""),str(""),3],
        [str(""),2,1,str("")]]
        for i in range(0,4):
            for j in range(0,4):
                nom = 'lineEdit_' + str(i) + str(j)
                VarText = self.findChild(QtGui.QLineEdit, nom)
                numero = self.sudoku[i][j]
                VarText.setText(str(numero))
        
    def comprova(self):
        bool = True
        for i in range(0,4):
            for j in range(0,4):
                nom = 'lineEdit_' + str(i) + str(j)
                VarText = self.findChild(QtGui.QLineEdit, nom)
                self.sudoku[i][j] = VarText.text()
                if self.sudoku[i][j] == "" :
                    self.lineEdit_44.setText("Hi han caselles en blanc")
                if int(self.sudoku[i][j]) > 4 or int(self.sudoku[i][j]) < 1 :
                    self.lineEdit_44.setText("Has introduit un numero no valid")
                try :
                    
                except ValueError:
                    
        i = 0            
        while i < 3 and bool == True :
            j=0
            while j < 3 and bool == True :
                nom = 'lineEdit_' + str(i) + str(j)
                VarText = self.findChild(QtGui.QLineEdit, nom)
                self.sudoku[i][j] = VarText.text()
                k = j
                l = i
                while j < 3 :
                    if self.sudoku[i][j] == self.sudoku[i][j+1] :
                        self.lineEdit_44.setText("Hi han valors repetits")
                        bool = False
                    j = j + 1
                while i < 3 :
                    if self.sudoku[i+1][j] == self.sudoku[i][j] :
                        self.lineEdit_44.setText("hi han valors repetits")
                        bool = False
                    i = i + 1
                j = k
                i = l
                j = j + 1
            i = i + 1    
        
        if bool == True :
            self.lineEdit_44.setText("Es correcte")          
        if bool == False :
            self.lineEdit_44.setText("INCORRECTE")
                
                
                
        ##Comprobar matriz        
        for i in range(0,4):
            for j in range(0,4):
                print self.sudoku[i][j],
            print
                
        
    def sortir(self):
        self.sudoku = [
        [str(""),1,3,str("")],
        [2,str(""),str(""),str("")],
        [str(""),str(""),str(""),3],
        [str(""),2,1,str("")]]
        for i in range(0,4):
            for j in range(0,4):
                nom = 'lineEdit_' + str(i) + str(j)
                VarText = self.findChild(QtGui.QLineEdit, nom)
                numero = self.sudoku[i][j]
                VarText.setText(str(numero))
        self.lineEdit_44.setText("Reseteo correcto.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = Ventana()
    finestra.show()
    
    sys.exit(app.exec_())