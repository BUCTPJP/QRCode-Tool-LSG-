# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\学习\理科类\编程设计\python\二维码小工具\UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 525)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 500))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame.setStyleSheet("QFrame{\n"
"border: 2px solid black;\n"
"border-radius: 2px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.text4 = QtWidgets.QTextBrowser(self.frame)
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(12)
        self.text4.setFont(font)
        self.text4.setObjectName("text4")
        self.gridLayout.addWidget(self.text4, 10, 1, 1, 5)
        self.button4 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(14)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.gridLayout.addWidget(self.button4, 5, 5, 1, 1)
        self.text1 = QtWidgets.QTextEdit(self.frame)
        self.text1.setMinimumSize(QtCore.QSize(0, 170))
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        self.text1.setFont(font)
        self.text1.setObjectName("text1")
        self.gridLayout.addWidget(self.text1, 0, 2, 3, 4)
        self.tip1 = QtWidgets.QLabel(self.frame)
        self.tip1.setMinimumSize(QtCore.QSize(0, 40))
        self.tip1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(20)
        self.tip1.setFont(font)
        self.tip1.setAlignment(QtCore.Qt.AlignCenter)
        self.tip1.setObjectName("tip1")
        self.gridLayout.addWidget(self.tip1, 0, 1, 1, 1)
        self.text7 = QtWidgets.QTextEdit(self.frame)
        self.text7.setMinimumSize(QtCore.QSize(0, 40))
        self.text7.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text7.setFont(font)
        self.text7.setObjectName("text7")
        self.gridLayout.addWidget(self.text7, 2, 1, 1, 1)
        self.tip3 = QtWidgets.QLabel(self.frame)
        self.tip3.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(20)
        self.tip3.setFont(font)
        self.tip3.setAlignment(QtCore.Qt.AlignCenter)
        self.tip3.setObjectName("tip3")
        self.gridLayout.addWidget(self.tip3, 5, 2, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(14)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 9, 2, 1, 2)
        self.button3 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(14)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 9, 5, 1, 1)
        self.button1 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(14)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 9, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mod1 = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.mod1.setFont(font)
        self.mod1.setObjectName("mod1")
        self.verticalLayout.addWidget(self.mod1)
        self.mod2 = QtWidgets.QRadioButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.mod2.setFont(font)
        self.mod2.setObjectName("mod2")
        self.verticalLayout.addWidget(self.mod2)
        self.mod = QtWidgets.QButtonGroup(self)
        self.mod.addButton(self.mod1, 1)
        self.mod.addButton(self.mod2, 2)
        self.gridLayout.addWidget(self.frame_3, 5, 1, 1, 1)
        self.text3 = QtWidgets.QTextEdit(self.frame)
        self.text3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.text3.setFont(font)
        self.text3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text3.setLineWidth(7)
        self.text3.setObjectName("text3")
        self.gridLayout.addWidget(self.text3, 5, 3, 1, 1)
        self.tip6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(10)
        self.tip6.setFont(font)
        self.tip6.setAlignment(QtCore.Qt.AlignCenter)
        self.tip6.setObjectName("tip6")
        self.gridLayout.addWidget(self.tip6, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_2.setStyleSheet("QFrame{\n"
"border: 2px solid black;\n"
"border-radius: 2px\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tip4 = QtWidgets.QLabel(self.frame_2)
        self.tip4.setMaximumSize(QtCore.QSize(110, 40))
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(12)
        self.tip4.setFont(font)
        self.tip4.setObjectName("tip4")
        self.gridLayout_2.addWidget(self.tip4, 0, 0, 1, 1)
        self.text6 = QtWidgets.QTextBrowser(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Adobe Heiti Std")
        font.setPointSize(14)
        self.text6.setFont(font)
        self.text6.setObjectName("text6")
        self.gridLayout_2.addWidget(self.text6, 7, 0, 1, 2)
        self.button6 = QtWidgets.QPushButton(self.frame_2)
        self.button6.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(20)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.gridLayout_2.addWidget(self.button6, 3, 0, 1, 1)
        self.button5 = QtWidgets.QPushButton(self.frame_2)
        self.button5.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(20)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.gridLayout_2.addWidget(self.button5, 3, 1, 1, 1)
        self.tip5 = QtWidgets.QLabel(self.frame_2)
        self.tip5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(12)
        self.tip5.setFont(font)
        self.tip5.setObjectName("tip5")
        self.gridLayout_2.addWidget(self.tip5, 6, 0, 1, 1)
        self.text5 = QtWidgets.QTextBrowser(self.frame_2)
        self.text5.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("喻兵行楷")
        font.setPointSize(12)
        self.text5.setFont(font)
        self.text5.setObjectName("text5")
        self.gridLayout_2.addWidget(self.text5, 1, 0, 1, 2)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("border: 1px solid black")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "二维码小工具"))
        self.frame.setToolTip(_translate("MainWindow", "生成"))
        self.button4.setText(_translate("MainWindow", "查找\n"
"颜色代码"))
        self.tip1.setText(_translate("MainWindow", "内容"))
        self.tip3.setText(_translate("MainWindow", "颜色"))
        self.button2.setText(_translate("MainWindow", "选择logo\n"
"并生成"))
        self.button3.setText(_translate("MainWindow", "选择背景\n"
"并生成"))
        self.button1.setText(_translate("MainWindow", "普通\n"
"生成"))
        self.mod1.setText(_translate("MainWindow", "模式一"))
        self.mod2.setText(_translate("MainWindow", "模式二"))
        self.tip6.setText(_translate("MainWindow", "X(下方功能慎用，\n"
"请提前阅读使用说明了解)"))
        self.frame_2.setToolTip(_translate("MainWindow", "解析"))
        self.tip4.setText(_translate("MainWindow", "运行时间："))
        self.button6.setText(_translate("MainWindow", "清空\n"
"显示"))
        self.button5.setText(_translate("MainWindow", "选择\n"
"二维码"))
        self.tip5.setText(_translate("MainWindow", "内容："))
import UI_rc
