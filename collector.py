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

import os

import cream
import cream.ipc
import cream.extensions


class Collector(cream.Module):

    __ipc_domain__ = 'org.cream.collector'

    def __init__(self):

        cream.Module.__init__(self)

        api = cream.extensions.ExtensionInterface({
            })

        self.extensions = cream.extensions.ExtensionManager([os.path.join(self._base_path, 'extensions')], api)
        self.extensions.load('261cc99d518c24669fff883722967fdec993c01af05dd2eedd61919f875a71d7')


if __name__ == '__main__':
    collector = Collector()
    collector.main()
