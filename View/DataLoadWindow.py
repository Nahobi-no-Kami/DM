# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataLoad.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadDataWindow(object):
    def setupUi(self, LoadDataWindow):
        LoadDataWindow.setObjectName("LoadDataWindow")
        LoadDataWindow.resize(500, 140)
        LoadDataWindow.setMinimumSize(QtCore.QSize(500, 140))
        LoadDataWindow.setMaximumSize(QtCore.QSize(500, 140))
        self.verticalLayoutWidget = QtWidgets.QWidget(LoadDataWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.timeDiapazonLOAD = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.timeDiapazonLOAD.setMaximumSize(QtCore.QSize(489, 80))
        self.timeDiapazonLOAD.setObjectName("timeDiapazonLOAD")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.timeDiapazonLOAD)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 471, 61))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.EndDateLabelLOAD = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.EndDateLabelLOAD.setObjectName("EndDateLabelLOAD")
        self.gridLayout_3.addWidget(self.EndDateLabelLOAD, 0, 1, 1, 1)
        self.ToDateTimeLOAD = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_3)
        self.ToDateTimeLOAD.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ToDateTimeLOAD.setObjectName("ToDateTimeLOAD")
        self.gridLayout_3.addWidget(self.ToDateTimeLOAD, 1, 1, 1, 1)
        self.FromDateTimeLOAD = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_3)
        self.FromDateTimeLOAD.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.FromDateTimeLOAD.setObjectName("FromDateTimeLOAD")
        self.gridLayout_3.addWidget(self.FromDateTimeLOAD, 1, 0, 1, 1)
        self.StartDateLabelLOAD = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.StartDateLabelLOAD.setObjectName("StartDateLabelLOAD")
        self.gridLayout_3.addWidget(self.StartDateLabelLOAD, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.timeDiapazonLOAD)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.loadButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loadButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loadButton.setObjectName("loadButton")
        self.verticalLayout.addWidget(self.loadButton)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(LoadDataWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadDataWindow)

    def retranslateUi(self, LoadDataWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadDataWindow.setWindowTitle(_translate("LoadDataWindow", "LoadDataWindow"))
        self.timeDiapazonLOAD.setTitle(_translate("LoadDataWindow", "Выбор временного диапазона"))
        self.EndDateLabelLOAD.setText(_translate("LoadDataWindow", "Конечная дата"))
        self.StartDateLabelLOAD.setText(_translate("LoadDataWindow", "Начальная дата"))
        self.loadButton.setText(_translate("LoadDataWindow", "Загрузить данные"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadDataWindow = QtWidgets.QWidget()
    ui = Ui_LoadDataWindow()
    ui.setupUi(LoadDataWindow)
    LoadDataWindow.show()
    sys.exit(app.exec_())
