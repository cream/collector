#! /usr/bin/env python
# -*- coding: utf-8 -*-

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
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import urllib
from xml.dom.minidom import parseString as parse_xml

import cream.ipc
import cream.extensions

@cream.extensions.register
class Weather(cream.extensions.Extension, cream.ipc.Object):

    def __init__(self, *args):

        cream.extensions.Extension.__init__(self, *args)
        cream.ipc.Object.__init__(self,
            'org.cream.collector',
            '/org/cream/collector/weather'
        )


    @cream.ipc.method('s', 'a{ss}')
    def get_weather(self, location):

        handle = urllib.urlopen('http://api.wunderground.com/auto/wui/geo/WXCurrentObXML/index.xml?query={0}'.format(location))
        data = handle.read()
        handle.close()
        
        dom = parse_xml(data)

        return {
            'weather': dom.getElementsByTagName('weather')[0].childNodes[0].data,
            'temperature': dom.getElementsByTagName('temp_c')[0].childNodes[0].data,
            'humidity': dom.getElementsByTagName('relative_humidity')[0].childNodes[0].data.replace("%", ""),
            'wind_direction': dom.getElementsByTagName('wind_dir')[0].childNodes[0].data,
            'wind_speed': str(round(float(dom.getElementsByTagName('wind_mph')[0].childNodes[0].data) * 1.609, 1)),
            'pressure': dom.getElementsByTagName('pressure_mb')[0].childNodes[0].data,
            'visibility': dom.getElementsByTagName('visibility_km')[0].childNodes[0].data,
            'icon': dom.getElementsByTagName('icon')[0].childNodes[0].data
            }
