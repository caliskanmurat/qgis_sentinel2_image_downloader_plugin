# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DownloadSentinelDialog
                                 A QGIS plugin
 This plugin allows users to be able to download Sentinel 2 images.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-05
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Murat Çalışkan
        email                : caliskan.murat.20@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'sentinel_downloader_dialog_base.ui'))

FORM_CLASS2, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'index_config.ui'))

class DownloadSentinelDialog(QtWidgets.QDialog, QtWidgets.QApplication, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(DownloadSentinelDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)


class IndexWindow(QtWidgets.QDialog, QtWidgets.QApplication, FORM_CLASS2):
    def __init__(self, parent=None):
        """Constructor."""
        super(IndexWindow, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS2.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
