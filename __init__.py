# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AirviroOfflineEdb
                                 A QGIS plugin
 Editing Airviro emission databases offline
                             -------------------
        begin                : 2015-11-10
        copyright            : (C) 2015 by David Segersson
        email                : david.segersson@smhi.se
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
    """Load AirviroOfflineEdb class from file AirviroOfflineEdb.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgis_edb import AirviroOfflineEdb
    return AirviroOfflineEdb(iface)
