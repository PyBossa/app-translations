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
