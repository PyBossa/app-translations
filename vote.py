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
