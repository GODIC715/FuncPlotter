import sys
import numpy as np
from PySide2 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from TextToFunc import *
from MainMenu import *
import icons

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent):
        fig = Figure()
        self.axes = fig.add_subplot(1,1,1)

        # Canvas and figure colors
        fig.patch.set_facecolor('#4668ef')
        self.axes.set_facecolor('#4668ef')
        self.setupCanvas()
        FigureCanvas.__init__(self, fig)
        self.resize(parent.size().width() - 10, parent.size().height() - 10)
        self.setParent(parent)
        self.setStyleSheet("background-color:black;")
    
    def setupCanvas(self):
        self.axes.spines['top'].set_color('none')
        self.axes.spines['right'].set_color('none')
        self.axes.spines['left'].set_linewidth(3)
        self.axes.spines['bottom'].set_linewidth(3)
        self.axes.set_xlabel('X', fontsize = 18)
        self.axes.set_ylabel('F(X)', fontsize = 18)
        self.axes.tick_params(axis='x', labelsize = 12)
        self.axes.tick_params(axis='y', labelsize = 12)
        self.axes.xaxis.set_ticks_position('bottom')
        self.axes.yaxis.set_ticks_position('left')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        icon = QIcon(QPixmap(":/Icons/Icon.png"))
        self.setWindowIcon(icon)
        self.setFixedSize(self.size().width(),self.size().height())
        self.canvas = MyMplCanvas(self.plotArea)
        self.toolbar = NavigationToolbar(self.canvas, self.plotArea, True)
        self.toolbar.setStyleSheet("NavigationToolbar#toolbar{background-color:rgba(62, 111, 170, 255);}")        
        self.newLayout = QVBoxLayout()
        self.newLayout.addWidget(self.toolbar)
        self.newLayout.addWidget(self.canvas)
        self.plotArea.setLayout(self.newLayout)
        self.plotButton.clicked.connect(self.drawPlot)
        self.clearButton.clicked.connect(self.clearCanvas)

    def displayMessage(self, Message : str):
        msg = QMessageBox()
        icon = QIcon(QPixmap(":/Icons/Icon.png"))
        msg.setWindowIcon(icon)
        msg.setWindowTitle("Invalid input")
        msg.setText(Message)
        msg.exec()
    
    def drawPlot(self):

        # Created this variable just to hold the text passed into the messagebox as I couldn't find a way to make pytest-qt
        # find and see the text on the messagebox 
        self.testingVar = ""

        self.funcString = self.functionInput.text()
        self.funcString = prepString(self.funcString)
        self.lowerLimit = self.lowerLimitSpin.value()
        self.upperLimit = self.upperLimitSpin.value()
        self.sampleNum = self.sampleNumberSpin.value()
        self.initFuncCheck = checkFuncInput(self.funcString)
        if self.initFuncCheck != True: 
            self.testingVar = self.initFuncCheck
            self.displayMessage(self.initFuncCheck)
        else:
            if self.lowerLimit >= self.upperLimit:
                self.testingVar = "Lower bound must be explicitly lower than the upper bound"
                self.displayMessage("Lower bound must be explicitly lower than the upper bound")
            else:
                mathFunction = evalFunction(self.funcString)
                xValues = np.linspace(start = self.lowerLimit, stop = self.upperLimit, num = self.sampleNum)
                yValues = mathFunction(xValues)
                if type(yValues) == str:
                    if yValues == "TypeError":
                        self.testingVar = "You probably forgot to provide an argument somewhere. Check for 'sin()' for example"
                        self.displayMessage("You probably forgot to provide an argument somewhere. Check for 'sin()' for example")
                    elif yValues == "SyntaxError":
                        self.testingVar = "You probably forgot to close a bracket or provide a second number somewhere. Check for 'sin(x' or '5^' for example"
                        self.displayMessage("You probably forgot to close a bracket or provide a second number somewhere. Check for 'sin(x' or '5^' for example")
                else:
                    self.clearCanvas()
                    if "x" not in self.funcString: # Function input string is a valid math expression that just doesn't have an x in it. In other words, a cconstant value.
                        self.canvas.axes.plot(xValues, np.array([yValues for x in range(self.sampleNum)]), color='k', linewidth=3, label = f'{self.funcString}')
                        self.testingVar = "Plotted successfully"
                    else:
                        self.canvas.axes.plot(xValues, mathFunction(xValues), color='k', linewidth=3, label = f'{self.funcString}')
                        self.testingVar = "Plotted successfully"
                    self.canvas.axes.legend()
                    self.canvas.draw()

    def clearCanvas(self):
        self.canvas.axes.clear()
        self.canvas.setupCanvas()
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()