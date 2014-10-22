# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.

import enki
import sys
try:
    import settings
except:
    print "Please, create a settings.py file (see settings.py.tmpl)"
    sys.exit()

e = enki.Enki(settings.APIKEY, settings.SERVER, settings.PROJECT)

e.get_all()

lines = []
for t in e.tasks:
    msgstr = e.task_runs_df[t.id]['msgstr'].describe()['top']
    var_id = t.info['var_id']
    line = "%s= %s\n" % (var_id, msgstr)
    lines.append(line)

file = open('/tmp/file.properties', 'w')
for l in lines:
    file.write(l)
file.close()
