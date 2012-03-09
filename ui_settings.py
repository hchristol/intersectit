# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings.ui'
#
# Created: Fri Mar  9 14:20:27 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(449, 397)
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "IntersectIt :: settings", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(Settings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(Settings)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.observationTab = QtGui.QWidget()
        self.observationTab.setObjectName(_fromUtf8("observationTab"))
        self.formLayout_2 = QtGui.QFormLayout(self.observationTab)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.snapBox = QtGui.QCheckBox(self.observationTab)
        self.snapBox.setText(QtGui.QApplication.translate("Settings", "Snap to layers to place observations", None, QtGui.QApplication.UnicodeUTF8))
        self.snapBox.setChecked(True)
        self.snapBox.setObjectName(_fromUtf8("snapBox"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.snapBox)
        self.label_3 = QtGui.QLabel(self.observationTab)
        self.label_3.setText(QtGui.QApplication.translate("Settings", "Default precision for distances [mm]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.defaultPrecisionDistanceBox = QtGui.QDoubleSpinBox(self.observationTab)
        self.defaultPrecisionDistanceBox.setDecimals(1)
        self.defaultPrecisionDistanceBox.setMaximum(1000.0)
        self.defaultPrecisionDistanceBox.setProperty("value", 25.0)
        self.defaultPrecisionDistanceBox.setObjectName(_fromUtf8("defaultPrecisionDistanceBox"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.defaultPrecisionDistanceBox)
        self.label_4 = QtGui.QLabel(self.observationTab)
        self.label_4.setEnabled(False)
        self.label_4.setText(QtGui.QApplication.translate("Settings", "Default precision for orientations [°]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.defaultPrecisionOrientationBox = QtGui.QDoubleSpinBox(self.observationTab)
        self.defaultPrecisionOrientationBox.setEnabled(False)
        self.defaultPrecisionOrientationBox.setMaximum(2.0)
        self.defaultPrecisionOrientationBox.setSingleStep(0.1)
        self.defaultPrecisionOrientationBox.setProperty("value", 0.5)
        self.defaultPrecisionOrientationBox.setObjectName(_fromUtf8("defaultPrecisionOrientationBox"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.defaultPrecisionOrientationBox)
        self.tabWidget.addTab(self.observationTab, _fromUtf8(""))
        self.intersectionTab = QtGui.QWidget()
        self.intersectionTab.setObjectName(_fromUtf8("intersectionTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.intersectionTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.selectGroup = QtGui.QGroupBox(self.intersectionTab)
        self.selectGroup.setTitle(QtGui.QApplication.translate("Settings", "Selection of observations", None, QtGui.QApplication.UnicodeUTF8))
        self.selectGroup.setObjectName(_fromUtf8("selectGroup"))
        self.gridLayout_3 = QtGui.QGridLayout(self.selectGroup)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.rubberColor = QtGui.QPushButton(self.selectGroup)
        self.rubberColor.setToolTip(_fromUtf8(""))
        self.rubberColor.setText(_fromUtf8(""))
        self.rubberColor.setObjectName(_fromUtf8("rubberColor"))
        self.gridLayout_3.addWidget(self.rubberColor, 2, 2, 1, 1)
        self.rubberWidth = QtGui.QDoubleSpinBox(self.selectGroup)
        self.rubberWidth.setToolTip(_fromUtf8(""))
        self.rubberWidth.setDecimals(1)
        self.rubberWidth.setSingleStep(1.0)
        self.rubberWidth.setProperty("value", 2.0)
        self.rubberWidth.setObjectName(_fromUtf8("rubberWidth"))
        self.gridLayout_3.addWidget(self.rubberWidth, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.selectGroup)
        self.label_2.setText(QtGui.QApplication.translate("Settings", "highlighting", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.selectGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pixels = QtGui.QRadioButton(self.groupBox)
        self.pixels.setText(QtGui.QApplication.translate("Settings", "pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.pixels.setObjectName(_fromUtf8("pixels"))
        self.gridLayout_2.addWidget(self.pixels, 2, 0, 1, 1)
        self.mapUnits = QtGui.QRadioButton(self.groupBox)
        self.mapUnits.setText(QtGui.QApplication.translate("Settings", "map units", None, QtGui.QApplication.UnicodeUTF8))
        self.mapUnits.setChecked(True)
        self.mapUnits.setObjectName(_fromUtf8("mapUnits"))
        self.gridLayout_2.addWidget(self.mapUnits, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 2, 1, 1)
        self.tolerance = QtGui.QDoubleSpinBox(self.selectGroup)
        self.tolerance.setSingleStep(0.1)
        self.tolerance.setProperty("value", 0.3)
        self.tolerance.setObjectName(_fromUtf8("tolerance"))
        self.gridLayout_3.addWidget(self.tolerance, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.selectGroup)
        self.label.setText(QtGui.QApplication.translate("Settings", "select observations within", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.selectGroup, 0, 0, 1, 1)
        self.line_4 = QtGui.QFrame(self.intersectionTab)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_4.addWidget(self.line_4, 1, 0, 1, 1)
        self.resultGroup = QtGui.QGroupBox(self.intersectionTab)
        self.resultGroup.setTitle(QtGui.QApplication.translate("Settings", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.resultGroup.setObjectName(_fromUtf8("resultGroup"))
        self.gridLayout_6 = QtGui.QGridLayout(self.resultGroup)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.displayReport = QtGui.QCheckBox(self.resultGroup)
        self.displayReport.setText(QtGui.QApplication.translate("Settings", "display results report from least-squares", None, QtGui.QApplication.UnicodeUTF8))
        self.displayReport.setChecked(True)
        self.displayReport.setObjectName(_fromUtf8("displayReport"))
        self.gridLayout_6.addWidget(self.displayReport, 0, 0, 1, 2)
        self.saveReportBox = QtGui.QCheckBox(self.resultGroup)
        self.saveReportBox.setText(QtGui.QApplication.translate("Settings", "save LS report in field", None, QtGui.QApplication.UnicodeUTF8))
        self.saveReportBox.setObjectName(_fromUtf8("saveReportBox"))
        self.gridLayout_6.addWidget(self.saveReportBox, 2, 0, 1, 1)
        self.reportFieldCombo = QtGui.QComboBox(self.resultGroup)
        self.reportFieldCombo.setObjectName(_fromUtf8("reportFieldCombo"))
        self.gridLayout_6.addWidget(self.reportFieldCombo, 2, 1, 1, 1)
        self.placeIntersectionBox = QtGui.QCheckBox(self.resultGroup)
        self.placeIntersectionBox.setText(QtGui.QApplication.translate("Settings", "place point in layer", None, QtGui.QApplication.UnicodeUTF8))
        self.placeIntersectionBox.setObjectName(_fromUtf8("placeIntersectionBox"))
        self.gridLayout_6.addWidget(self.placeIntersectionBox, 1, 0, 1, 1)
        self.intersectionLayerCombo = QtGui.QComboBox(self.resultGroup)
        self.intersectionLayerCombo.setObjectName(_fromUtf8("intersectionLayerCombo"))
        self.gridLayout_6.addWidget(self.intersectionLayerCombo, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.resultGroup, 2, 0, 1, 1)
        self.tabWidget.addTab(self.intersectionTab, _fromUtf8(""))
        self.dimensionTab = QtGui.QWidget()
        self.dimensionTab.setObjectName(_fromUtf8("dimensionTab"))
        self.formLayout = QtGui.QFormLayout(self.dimensionTab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.placeDimensionBox = QtGui.QCheckBox(self.dimensionTab)
        self.placeDimensionBox.setText(QtGui.QApplication.translate("Settings", "place dimension arc in layer", None, QtGui.QApplication.UnicodeUTF8))
        self.placeDimensionBox.setChecked(True)
        self.placeDimensionBox.setObjectName(_fromUtf8("placeDimensionBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.placeDimensionBox)
        self.dimensionLayerCombo = QtGui.QComboBox(self.dimensionTab)
        self.dimensionLayerCombo.setObjectName(_fromUtf8("dimensionLayerCombo"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dimensionLayerCombo)
        self.placeMeasureBox = QtGui.QCheckBox(self.dimensionTab)
        self.placeMeasureBox.setText(QtGui.QApplication.translate("Settings", "place measure in field", None, QtGui.QApplication.UnicodeUTF8))
        self.placeMeasureBox.setChecked(True)
        self.placeMeasureBox.setObjectName(_fromUtf8("placeMeasureBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.placeMeasureBox)
        self.measureFieldCombo = QtGui.QComboBox(self.dimensionTab)
        self.measureFieldCombo.setObjectName(_fromUtf8("measureFieldCombo"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.measureFieldCombo)
        self.placePrecisionBox = QtGui.QCheckBox(self.dimensionTab)
        self.placePrecisionBox.setText(QtGui.QApplication.translate("Settings", "place precision in field", None, QtGui.QApplication.UnicodeUTF8))
        self.placePrecisionBox.setObjectName(_fromUtf8("placePrecisionBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.placePrecisionBox)
        self.precisionFieldCombo = QtGui.QComboBox(self.dimensionTab)
        self.precisionFieldCombo.setObjectName(_fromUtf8("precisionFieldCombo"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.precisionFieldCombo)
        self.tabWidget.addTab(self.dimensionTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)
        Settings.setTabOrder(self.pixels, self.buttonBox)

    def retranslateUi(self, Settings):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.observationTab), QtGui.QApplication.translate("Settings", "Observations", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.intersectionTab), QtGui.QApplication.translate("Settings", "Intersection", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dimensionTab), QtGui.QApplication.translate("Settings", "Dimensions", None, QtGui.QApplication.UnicodeUTF8))

