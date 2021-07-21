# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 760)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color qlineargradient(spread:pad, x1:0.0852273, y1:0.063, x2:0.988, y2:0.982955, stop:0 rgba(62, 111, 170, 255), stop:1 rgba(255, 255, 255, 255))")
        self.bgWidget = QWidget(self.centralwidget)
        self.bgWidget.setObjectName(u"bgWidget")
        self.bgWidget.setGeometry(QRect(0, 0, 600, 760))
        self.bgWidget.setStyleSheet(u"QWidget#bgWidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.994, stop:0 rgba(79, 25, 173, 255), stop:0.988636 rgba(70, 104, 239, 255))}")
        self.functionLabel = QLabel(self.bgWidget)
        self.functionLabel.setObjectName(u"functionLabel")
        self.functionLabel.setGeometry(QRect(40, 50, 75, 25))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.functionLabel.setFont(font)
        self.functionLabel.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.functionInput = QLineEdit(self.bgWidget)
        self.functionInput.setObjectName(u"functionInput")
        self.functionInput.setGeometry(QRect(150, 50, 120, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.functionInput.sizePolicy().hasHeightForWidth())
        self.functionInput.setSizePolicy(sizePolicy)
        self.functionInput.setStyleSheet(u"border-radius:10px;")
        self.lowerLimitSpin = QSpinBox(self.bgWidget)
        self.lowerLimitSpin.setObjectName(u"lowerLimitSpin")
        self.lowerLimitSpin.setGeometry(QRect(220, 90, 50, 23))
        self.lowerLimitSpin.setStyleSheet(u"opacity:0.5;")
        self.lowerLimitSpin.setMinimum(-999)
        self.lowerLimitSpin.setMaximum(999)
        self.lowerLimitSpin.setSingleStep(1)
        self.lowerLimitSpin.setValue(0)
        self.lowerLimitSpin.setDisplayIntegerBase(10)
        self.titleLabel = QLabel(self.bgWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 10, 600, 25))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.titleLabel.setFont(font1)
        self.titleLabel.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.lowerLimitLabel = QLabel(self.bgWidget)
        self.lowerLimitLabel.setObjectName(u"lowerLimitLabel")
        self.lowerLimitLabel.setGeometry(QRect(40, 90, 160, 25))
        self.lowerLimitLabel.setFont(font)
        self.lowerLimitLabel.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.plotArea = QWidget(self.bgWidget)
        self.plotArea.setObjectName(u"plotArea")
        self.plotArea.setGeometry(QRect(0, 170, 590, 590))
        self.upperLimitLabel = QLabel(self.bgWidget)
        self.upperLimitLabel.setObjectName(u"upperLimitLabel")
        self.upperLimitLabel.setGeometry(QRect(330, 90, 157, 23))
        self.upperLimitLabel.setFont(font)
        self.upperLimitLabel.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"")
        self.plotButton = QPushButton(self.bgWidget)
        self.plotButton.setObjectName(u"plotButton")
        self.plotButton.setGeometry(QRect(200, 140, 75, 30))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(14)
        self.plotButton.setFont(font2)
        self.plotButton.setStyleSheet(u"border-radius:10px;\n"
"background-color:#4f19ad;\n"
"border:2px solid black; color:white;")
        self.clearButton = QPushButton(self.bgWidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(330, 140, 75, 30))
        self.clearButton.setFont(font2)
        self.clearButton.setStyleSheet(u"border-radius:10px;\n"
"background-color:#4f19ad;\n"
"border:2px solid black; font: 14pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"")
        self.upperLimitSpin = QSpinBox(self.bgWidget)
        self.upperLimitSpin.setObjectName(u"upperLimitSpin")
        self.upperLimitSpin.setGeometry(QRect(510, 90, 50, 23))
        self.upperLimitSpin.setMinimum(-999)
        self.upperLimitSpin.setMaximum(999)
        self.upperLimitSpin.setSingleStep(1)
        self.upperLimitSpin.setValue(0)
        self.upperLimitSpin.setDisplayIntegerBase(10)
        self.sampleNumberLable = QLabel(self.bgWidget)
        self.sampleNumberLable.setObjectName(u"sampleNumberLable")
        self.sampleNumberLable.setGeometry(QRect(330, 50, 134, 23))
        self.sampleNumberLable.setFont(font)
        self.sampleNumberLable.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: white;")
        self.sampleNumberSpin = QSpinBox(self.bgWidget)
        self.sampleNumberSpin.setObjectName(u"sampleNumberSpin")
        self.sampleNumberSpin.setGeometry(QRect(510, 50, 50, 23))
        self.sampleNumberSpin.setStyleSheet(u"")
        self.sampleNumberSpin.setMinimum(10)
        self.sampleNumberSpin.setMaximum(9999)
        self.sampleNumberSpin.setSingleStep(10)
        self.sampleNumberSpin.setValue(10)
        self.sampleNumberSpin.setDisplayIntegerBase(10)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.functionInput, self.sampleNumberSpin)
        QWidget.setTabOrder(self.sampleNumberSpin, self.lowerLimitSpin)
        QWidget.setTabOrder(self.lowerLimitSpin, self.upperLimitSpin)
        QWidget.setTabOrder(self.upperLimitSpin, self.plotButton)
        QWidget.setTabOrder(self.plotButton, self.clearButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Function Plotter", None))
        self.functionLabel.setText(QCoreApplication.translate("MainWindow", u"Function", None))
        self.functionInput.setToolTip(QCoreApplication.translate("MainWindow", u"Supported special operations are 'sin()', 'cos()' exponant as 'exp()' and power as '^'", None))
#if QT_CONFIG(tooltip)
        self.lowerLimitSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Supports integers between -999 and 999", None))
#endif // QT_CONFIG(tooltip)
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Function plotter", None))
        self.lowerLimitLabel.setText(QCoreApplication.translate("MainWindow", u"Lower bound for X", None))
        self.upperLimitLabel.setText(QCoreApplication.translate("MainWindow", u"Upper bound for X", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.upperLimitSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Supports integers between -999 and 999", None))
#endif // QT_CONFIG(tooltip)
        self.sampleNumberLable.setText(QCoreApplication.translate("MainWindow", u"Sample number", None))
#if QT_CONFIG(tooltip)
        self.sampleNumberSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Needs to be =>100 to be smooth", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

