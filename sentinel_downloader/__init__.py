# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DownloadSentinel
                                 A QGIS plugin
 This plugin allows users to be able to download Sentinel 2 images.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-05
        copyright            : (C) 2024 by Murat Çalışkan
        email                : caliskan.murat.20@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DownloadSentinel class from file DownloadSentinel.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sentinel_downloader import DownloadSentinel
    return DownloadSentinel(iface)
