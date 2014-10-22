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
import json

import sys
try:
    import settings
except:
    print "Please, create a settings.py file (see settings.py.tmpl)"
    sys.exit()

e = enki.Enki(settings.APIKEY, settings.SERVER, settings.PROJECT)

e.get_all()

tasks = []

for t in e.tasks:
    options = []
    i = 0
    for k in e.task_runs_df[t.id]['msgstr'].keys():
        option = dict(task_run_id=None, msgstr=None)
        option['task_run_id'] = k
        option['msgstr'] = e.task_runs_df[t.id]['msgstr'][k]
        options.append(option)
    t.info['msgstr_options'] = options
    tasks.append(t.info)

file = open('/tmp/translations_voting_tasks.json', 'w')
file.write(json.dumps(tasks))
file.close()
