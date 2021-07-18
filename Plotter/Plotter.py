import sys
import numpy as np
from PySide2 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from TextToFunc import *
from MainMenu import *
import resources
class MyMplCanvas(FigureCanvas):
    def __init__(self, parent):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        # self.axes.spines['left'].set_position('center')
        # self.axes.spines['bottom'].set_position('zero')

        self.axes.spines['top'].set_color('none')
        self.axes.spines['right'].set_color('none')
        self.axes.xaxis.set_ticks_position('bottom')
        self.axes.yaxis.set_ticks_position('left')
        self.axes.set_aspect('equal')

        FigureCanvas.__init__(self, fig)
        self.resize(parent.size().width() - 10, parent.size().height() - 10)
        self.setParent(parent)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        icon = QIcon("Icons/Icon.png")
        self.setWindowIcon(icon)
        self.setFixedSize(self.size().width(),self.size().height())
        self.canvas = MyMplCanvas(self.plotArea)
        self.toolbar = NavigationToolbar(self.canvas, self.plotArea, True)
        self.newLay = QVBoxLayout()
        self.newLay.addWidget(self.toolbar)
        self.newLay.addWidget(self.canvas)
        self.plotArea.setLayout(self.newLay)
        self.plotButton.clicked.connect(self.drawPlot)
    
    def displayMessage(self, Message : str):
        msg = QMessageBox()
        icon = QIcon("Icons/Icon.png")
        msg.setWindowIcon(icon)
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
                self.canvas.axes.clear()
                # self.canvas.axes.spines['left'].set_position('center')
                self.canvas.axes.spines['top'].set_color('none')
                self.canvas.axes.spines['right'].set_color('none')
                self.canvas.axes.set_aspect('equal')
                self.canvas.axes.xaxis.set_ticks_position('bottom')
                self.canvas.axes.yaxis.set_ticks_position('left')
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