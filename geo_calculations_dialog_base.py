# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geo_calculations_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_geo_calculationsDialogBase(object):
    def setupUi(self, geo_calculationsDialogBase):
        geo_calculationsDialogBase.setObjectName("geo_calculationsDialogBase")
        geo_calculationsDialogBase.resize(756, 421)
        self.button_box = QtWidgets.QDialogButtonBox(geo_calculationsDialogBase)
        self.button_box.setGeometry(QtCore.QRect(160, 360, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.wysokoscButton = QtWidgets.QPushButton(geo_calculationsDialogBase)
        self.wysokoscButton.setGeometry(QtCore.QRect(60, 150, 291, 71))
        self.wysokoscButton.setObjectName("wysokoscButton")
        self.PushButton_pole = QtWidgets.QPushButton(geo_calculationsDialogBase)
        self.PushButton_pole.setGeometry(QtCore.QRect(60, 240, 291, 71))
        self.PushButton_pole.setObjectName("PushButton_pole")
        self.label = QtWidgets.QLabel(geo_calculationsDialogBase)
        self.label.setGeometry(QtCore.QRect(60, 40, 251, 61))
        self.label.setObjectName("label")
        self.mMapLayerComboBox = QgsMapLayerComboBox(geo_calculationsDialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(370, 60, 160, 27))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")

        self.retranslateUi(geo_calculationsDialogBase)
        self.button_box.accepted.connect(geo_calculationsDialogBase.accept) # type: ignore
        self.button_box.rejected.connect(geo_calculationsDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(geo_calculationsDialogBase)

    def retranslateUi(self, geo_calculationsDialogBase):
        _translate = QtCore.QCoreApplication.translate
        geo_calculationsDialogBase.setWindowTitle(_translate("geo_calculationsDialogBase", "Geodetic Calculations"))
        self.wysokoscButton.setText(_translate("geo_calculationsDialogBase", "Oblicz różnice wysokości"))
        self.PushButton_pole.setText(_translate("geo_calculationsDialogBase", "Oblicz pole powierzchni"))
        self.label.setText(_translate("geo_calculationsDialogBase", "Wybierz warstwę z wybranymi punktami"))
from qgsmaplayercombobox import QgsMapLayerComboBox
