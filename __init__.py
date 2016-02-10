# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Planeamiento
                                 A QGIS plugin
 Herramientas para el Dpto. de Planeamiento del Gobierno de Canarias
                             -------------------
        begin                : 2016-02-10
        copyright            : (C) 2016 by Félix José Hernández
        email                : fhernandeze@grafcan.es
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
    """Load Planeamiento class from file Planeamiento.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .planeamiento_tools import Planeamiento
    return Planeamiento(iface)
