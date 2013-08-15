#-----------------------------------------------------------
#
# Intersect It is a QGIS plugin to place observations (distance or orientation)
# with their corresponding precision, intersect them using a least-squares solution
# and save dimensions in a dedicated layer to produce maps.
#
# Copyright    : (C) 2013 Denis Rouzaud
# Email        : denis.rouzaud@gmail.com
#
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this progsram; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTextEdit
from qgis.core import QGis, QgsGeometry, QgsPoint, QgsMapLayer, QgsTolerance, QgsSnapper, QgsMapLayerRegistry
from qgis.gui import QgsRubberBand, QgsMapTool, QgsMapCanvasSnapper, QgsMessageBar

from ..core.mysettings import MySettings
from ..core.distance import Distance

from distancedialog import DistanceDialog


class DistanceMapTool(QgsMapTool):
    def __init__(self, iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.settings = MySettings()
        QgsMapTool.__init__(self, self.canvas)

    def activate(self):
        QgsMapTool.activate(self)
        self.rubber = QgsRubberBand(self.canvas, QGis.Point)
        self.rubber.setColor(self.settings.value("rubberColor"))
        self.rubber.setIcon(self.settings.value("rubberIcon"))
        self.rubber.setIconSize(self.settings.value("rubberSize"))
        self.updateSnapperList()
        QgsMapLayerRegistry.instance().layersAdded.connect(self.updateSnapperList)
        QgsMapLayerRegistry.instance().layersRemoved.connect(self.updateSnapperList)
        self.messageWidget = self.iface.messageBar().createMessage("Intersect It", "Not snapped.")
        self.messageWidgetExist = True
        self.messageWidget.destroyed.connect(self.messageWidgetRemoved)
        if self.settings.value("obsDistanceSnapping") != "no":
            self.iface.messageBar().pushWidget(self.messageWidget)

    def updateSnapperList(self, dummy=None):
        self.snapperList = []
        tolerance = self.settings.value("selectTolerance")
        units = self.settings.value("selectUnits")
        for layer in self.iface.mapCanvas().layers():
            if layer.type() == QgsMapLayer.VectorLayer and layer.hasGeometryType():
                snapLayer = QgsSnapper.SnapLayer()
                snapLayer.mLayer = layer
                snapLayer.mSnapTo = QgsSnapper.SnapToVertex
                snapLayer.mTolerance = tolerance
                if units == "map":
                    snapLayer.mUnitType = QgsTolerance.MapUnits
                else:
                    snapLayer.mUnitType = QgsTolerance.Pixels
                self.snapperList.append(snapLayer)

    def deactivate(self):
        self.iface.messageBar().popWidget(self.messageWidget)
        self.rubber.reset()
        QgsMapLayerRegistry.instance().layersAdded.disconnect(self.updateSnapperList)
        QgsMapLayerRegistry.instance().layersRemoved.disconnect(self.updateSnapperList)
        QgsMapTool.deactivate(self)

    def messageWidgetRemoved(self):
        self.messageWidgetExist = False

    def displaySnapInfo(self, snappingResults):
        if not self.messageWidgetExist:
            return
        nSnappingResults = len(snappingResults)
        if nSnappingResults == 0:
            message = "No snap"
        else:
            message = "Snapped to: <b>%s" % snappingResults[0].layer.name() + "</b>"
            if nSnappingResults > 1:
                layers = []
                message += " Nearby: "
                for res in snappingResults[1:]:
                    layerName = res.layer.name()
                    if layerName not in layers:
                        message += res.layer.name() + ", "
                        layers.append(layerName)
                message = message[:-2]
        messageTextEdit = self.messageWidget.findChild(QTextEdit, "mMsgText")
        if messageTextEdit is not None:
            messageTextEdit.setText(message)

    def canvasMoveEvent(self, mouseEvent):
        snappedPoint = self.snapToLayers(mouseEvent.pos())
        if snappedPoint is None:
            self.rubber.reset()
        else:
            self.rubber.setToGeometry(QgsGeometry().fromPoint(snappedPoint), None)

    def canvasPressEvent(self, mouseEvent):
        if mouseEvent.button() != Qt.LeftButton:
            return
        pixPoint = mouseEvent.pos()
        mapPoint = self.toMapCoordinates(pixPoint)
        #snap to layers
        mapPoint = self.snapToLayers(pixPoint, mapPoint)
        self.rubber.setToGeometry(QgsGeometry().fromPoint(mapPoint), None)
        distance = Distance(self.iface, mapPoint, 1)
        dlg = DistanceDialog(distance, self.canvas)
        if dlg.exec_():
            distance.save()
        self.rubber.reset()

    def snapToLayers(self, pixPoint, initPoint=None):
        self.snapping = self.settings.value("obsDistanceSnapping")

        if self.snapping == "no":
            return initPoint

        if self.snapping == "project":
            ok, snappingResults = QgsMapCanvasSnapper(self.canvas).snapToBackgroundLayers(pixPoint, [])
            self.displaySnapInfo(snappingResults)
            if ok == 0 and len(snappingResults) > 0:
                return QgsPoint(snappingResults[0].snappedVertex)
            else:
                return initPoint

        if self.snapping == "all":
            if len(self.snapperList) == 0:
                return initPoint
            snapper = QgsSnapper(self.canvas.mapRenderer())
            snapper.setSnapLayers(self.snapperList)
            snapper.setSnapMode(QgsSnapper.SnapWithResultsWithinTolerances)
            ok, snappingResults = snapper.snapPoint(pixPoint, [])
            self.displaySnapInfo(snappingResults)
            if ok == 0 and len(snappingResults) > 0:
                return QgsPoint(snappingResults[0].snappedVertex)
            else:
                return initPoint
