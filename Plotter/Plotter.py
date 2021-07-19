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

        # Makes the figure fit the canvas better  
        fig.set_tight_layout(True)
        
        # Canvas and figure colors
        fig.patch.set_facecolor('#4668ef')
        self.axes.set_facecolor('#4668ef')
        
        # Removes the top and right borders and increases
        # the line width for the other borders
        self.axes.spines['top'].set_color('none')
        self.axes.spines['right'].set_color('none')
        self.axes.spines['left'].set_linewidth(3)
        self.axes.spines['bottom'].set_linewidth(3)
        self.axes.set_xlabel('X', fontsize = 18)
        self.axes.set_ylabel('F(X)', fontsize = 18)
        
        # Increases font size for the ticks
        self.axes.tick_params(axis='x', labelsize = 12)
        self.axes.tick_params(axis='y', labelsize = 12)
        self.axes.xaxis.set_ticks_position('bottom')
        self.axes.yaxis.set_ticks_position('left')
        
        # Sets the graph to be in a 1:1 aspect ratio.
        self.axes.set_aspect('equal')
        FigureCanvas.__init__(self, fig)
        
        # Resizes the canvas to be the same size as the parent widget minus some padding pixels
        self.resize(parent.size().width() - 10, parent.size().height() - 10)
        self.setParent(parent)
        self.setStyleSheet("background-color:black;")
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        icon = QIcon(QPixmap(":/Icons/Icon.png"))
        self.setWindowIcon(icon)

        # Ensures the window size is fixed as I couldn't handle with layouts
        self.setFixedSize(self.size().width(),self.size().height())

        # Create a new canvas with the empty widget plotArea as the parent
        self.canvas = MyMplCanvas(self.plotArea)

        # Creates a new toolbar with the first argument being the canvas that it controls
        # and the second argument is the parent widget
        self.toolbar = NavigationToolbar(self.canvas, self.plotArea, True)
        self.toolbar.setStyleSheet("NavigationToolbar#toolbar{background-color:rgba(62, 111, 170, 255);}")
        self.newLayout = QVBoxLayout()
        self.newLayout.addWidget(self.toolbar)
        self.newLayout.addWidget(self.canvas)
        self.plotArea.setLayout(self.newLayout)
        self.plotButton.clicked.connect(self.drawPlot)
        self.clearButton.clicked.connect(self.clear5ara)

    # Created this function to show
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
                if type(mathFunction(self.FuncString)) != float or type(mathFunction(self.FuncString)) != int:
                    self.displayMessage('Invalid syntax in function.')
                else:
                    xValues = np.linspace(start = self.lowerLimit, stop = self.upperLimit, num = self.sampleNum)
                    self.canvas.axes.clear()
                    # self.canvas.axes.spines['left'].set_position('center')
                    self.canvas.axes.set_xlabel('X')
                    self.canvas.axes.set_ylabel('F(X)')
                    self.canvas.axes.spines['top'].set_color('none')
                    self.canvas.axes.spines['right'].set_color('none')
                    self.canvas.axes.spines['left'].set_linewidth(3)
                    self.canvas.axes.spines['bottom'].set_linewidth(3)
                    self.canvas.axes.tick_params(axis='x', labelsize = 12)
                    self.canvas.axes.tick_params(axis='y', labelsize = 12)
                    self.canvas.axes.set_aspect('equal')
                    self.canvas.axes.xaxis.set_ticks_position('bottom')
                    self.canvas.axes.yaxis.set_ticks_position('left')
                    self.canvas.axes.plot(xValues, mathFunction(xValues), color='k', linewidth=3, label = f'{self.FuncString}')
                    self.canvas.axes.legend()
                    self.canvas.draw()
            else:
                self.displayMessage("Lower bound must be explicitly lower than the upper bound")
        else:
            self.displayMessage(self.Message)

    def clear5ara(self):
        self.canvas.axes.clear()
        self.canvas.axes.spines['top'].set_color('none')
        self.canvas.axes.spines['right'].set_color('none')
        self.canvas.axes.set_aspect('equal')
        self.canvas.axes.xaxis.set_ticks_position('bottom')
        self.canvas.axes.yaxis.set_ticks_position('left')
        self.canvas.draw()



app = QApplication (sys.argv) 
window = MainWindow() 
if __name__ == "__main__":
    window.show()
    app.exec_()