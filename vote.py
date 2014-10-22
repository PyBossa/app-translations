import enki
import json


e = enki.Enki('key', 'http://localhost:5001', 'translations')

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
