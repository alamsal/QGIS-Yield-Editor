# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CropEditor
                                 A QGIS plugin
 CroptEditor
                             -------------------
        begin                : 2017-04-07
        copyright            : (C) 2017 by Aashis Lamsal
        email                : lamsalwork@gmail.com
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
    """Load CropEditor class from file CropEditor.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .crop_editor import CropEditor
    return CropEditor(iface)
