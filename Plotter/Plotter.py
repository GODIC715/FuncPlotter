import sys
from types import new_class
import numpy as np
from PySide2 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from TextToFunc import *
from MainMenu import *

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        
        self.resize(parent.size().width() - 10, parent.size().height() - 10)
        self.setParent(parent)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size().width(),self.size().height())
        self.canvas = MyMplCanvas(self.plotArea)
        self.toolbar = NavigationToolbar(self.canvas, self.plotArea, True)
        self.newLay = QVBoxLayout()
        self.newLay.addWidget(self.toolbar)
        self.newLay.addWidget(self.canvas)
        self.plotArea.setLayout(self.newLay)
        self.plotButton.clicked.connect(self.drawPlot)
        # self.layout().addWidget(self.toolbar)
    
    def displayMessage(self, Message : str):
        msg = QMessageBox()
        msg.setWindowTitle("Invalid input")
        msg.setText(Message)
        msg.exec()
    
    def drawPlot(self):
        self.FuncString = self.functionInput.text()
        self.lowerLimit = self.lowerLimitSpin.value()
        self.upperLimit = self.upperLimitSpin.value()
        self.sampleNum = self.sampleNumberSpin.value()
        self.Message = checkFuncInput(self.FuncString)

        if self.Message == True:
            if self.lowerLimit < self.upperLimit:

                mathFunction = mainFunc(self.FuncString)
                xValues = np.linspace(start = self.lowerLimit, stop = self.upperLimit, num = self.sampleNum)
                self.canvas.axes.plot(xValues, mathFunction(xValues))
                self.canvas.draw()
            else:
                self.displayMessage("Lower bound must be explicitly lower than the upper bound")
        else:
            self.displayMessage(self.Message)


app = QApplication (sys.argv) 
window = MainWindow() 
if __name__ == "__main__":
    window.show()
    app.exec_()