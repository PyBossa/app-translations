import enki
import json


e = enki.Enki('key', 'http://localhost:5001', 'translations')

e.get_all()

tasks = []

for t in e.tasks:
    options = dict()
    i = 0
    for k in e.task_runs_df[t.id]['msgid'].keys():
       options[k] = e.task_runs_df[t.id]['msgid'][k]
    t.info['msgid_options'] = options
    tasks.append(t.info)

file = open('/tmp/translations_voting_tasks.json', 'w')
file.write(json.dumps(tasks))
file.close()
