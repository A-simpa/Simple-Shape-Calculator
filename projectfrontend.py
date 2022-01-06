import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow,  QApplication, QWidget
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from Project import *
class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        loadUi("projectSSCALC.ui", self)
        valid = QRegExpValidator(QRegExp(r'[0-9]*[.][0-9]+'))
        self.r.setValidator(valid)
        self.l1.setValidator(valid)
        self.l2.setValidator(valid)
        self.b1.setValidator(valid)
        self.b2.setValidator(valid)
        self.h.setValidator(valid)
        self.ba.setValidator(valid)

        self.rc1.setValidator(valid)
        self.lc1.setValidator(valid)
        self.lc2.setValidator(valid)
        self.bc2.setValidator(valid)
        self.bc2.setValidator(valid)
        self.h2.setValidator(valid)
        self.ba2.setValidator(valid)

        self.area2.clicked.connect(self.Area2)
        self.clearall2.clicked.connect(self.Clear2)
        self.centroid2.clicked.connect(self.Centroid2)
        self.shapename.clicked.connect(self.Sn)

        self.area1.clicked.connect(self.Area1)
        self.clearall1.clicked.connect(self.Clear1)
        self.centroid1.clicked.connect(self.Centroid1)

    def Area1(self):
        if self.circlebutton.isChecked():
            circle =Circle(int(self.r.text()))
            self.answer1.setText(str(circle.Area()))
        elif self.rectbutton1.isChecked():
            rect = rectangle(int(self.l1.text()),  int(self.b1.text()))
            self.answer1.setText(str(rect.Area()))
        elif self.square1.isChecked():
            sq = square(int(self.l2.text()), int(self.b2.text()))
            self.answer1.setText(str(square.Area()))
        elif self.triangle1.isChecked():
            sq = triangle(int(self.h.text()), int(self.ba.text()))
            self.answer1.setText(str(square.Area()))

    def Clear1(self):
        self.r.clear()
        self.l1.clear()
        self.l2.clear()
        self.b1.clear()
        self.b2.clear()
        self.h.clear()
        self.ba.clear()
        self.answer2.clear()

    def Centroid1(self):
        if self.circlebutton.isChecked():
            circle =Circle(int(self.r.text()))
            self.answer1.setText(str(circle.Centroid()))
        elif self.rectbutton1.isChecked():
            rect = rectangle(int(self.l1.text()),  int(self.b1.text()))
            self.answer1.setText(str(rect.Centroid()))
        elif self.square1.isChecked():
            sq = square(int(self.l2.text()), int(self.b2.text()))
            self.answer1.setText(str(square.Centroid()))
        elif self.triangle1.isChecked():
            sq = triangle(int(self.h.text()), int(self.ba.text()))
            self.answer1.setText(str(square.Centroid()))

        
    def Area1(self):
        if self.circlebutton.isChecked():
            circle =Circle(int(self.r.text()))
            self.answer1.setText(str(circle.Area()))
        elif self.rectbutton1.isChecked():
            rect = rectangle(int(self.l1.text()),  int(self.b1.text()))
            self.answer1.setText(str(rect.Area()))
        elif self.square1.isChecked():
            sq = square(int(self.l2.text()), int(self.b2.text()))
            self.answer1.setText(str(square.Area()))
        elif self.triangle1.isChecked():
            sq = triangle(int(self.h.text()), int(self.ba.text()))
            self.answer1.setText(str(square.Area()))

    def Clear2(self):
        self.rc1.clear()
        self.lc1.clear()
        self.lc2.clear()
        self.bc1.clear()
        self.bc2.clear()
        self.h2.clear()
        self.ba2.clear()
        self.answer2.clear()

    def Centroid1(self):
        if self.circlebutton.isChecked():
            circle =Circle(int(self.r.text()))
            self.answer1.setText(str(circle.Centroid()))
        elif self.rectbutton1.isChecked():
            rect = rectangle(int(self.l1.text()),  int(self.b1.text()))
            self.answer1.setText(str(rect.Centroid()))
        elif self.square1.isChecked():
            sq = square(int(self.l2.text()), int(self.b2.text()))
            self.answer1.setText(str(square.Centroid()))
        elif self.triangle1.isChecked():
            sq = triangle(int(self.h.text()), int(self.ba.text()))
            self.answer1.setText(str(square.Centroid()))

    def Centroid2(self):
        cs = [0,0]
        n=0
        for i in [self.circlebox, self.rectanglebox1, self.squarebox, self.trianglebox]:
            if i.isChecked():
                n=n+1
                if i == self.circlebox:
                    c = [int(self.rc1.text()), int(self.rc1.text())]
                elif i == self.rectanglebox1:
                    c = [int(self.lc1.text())/2, int(self.bc1.text())/2]
                elif i == self.squarebox:
                    c = [int(self.lc2.text())/2, int(self.bc2.text())/2]
                elif i == self.trianglebox:
                    c = [int(self.ba.text())/2, int(self.h.text())/3]
                cs =[cs[0]+c[0], c[1]+c[1]]
        cs = [cs[0]/n, cs[0]/n]
        self.answer2.setText("Centroid at{}".format(cs))
    
    def Area2(self):
        area = 0
        for i in [self.circlebox, self.rectanglebox1, self.squarebox, self.trianglebox]:
            if i.isChecked():
                if i == self.circlebox:
                    c = Circle(int(self.rc1.text()))
                    area = area + c.Area()
                    print(area)
                elif i == self.rectanglebox1:
                    c = rectangle(int(self.lc1.text()), int(self.bc1.text()))
                    area = area + c.Area()
                elif i == self.squarebox:
                    c = square(int(self.lc2.text()), int(self.bc2.text()))
                    area = area + c.Area()
                elif i == self.trianglebox:
                    c =triangle(int(self.ba.text()), int(self.h2.text()))
                    area = area + c.Area()
        self.answer2.setText(str(area))

    def Sn(self):
        p= Plane(int(self.coner.text()), int(self.side.text()))
        self.answer3.setText(p.ShapeName())


                


        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome = GUI()
    welcome.show()
    try:
        sys.exit(app.exec_())
    except:
        print('exiting')



