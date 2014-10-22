import enki
import polib
import sys
try:
    import settings
except:
    print "Please, create a settings.py file (see settings.py.tmpl)"
    sys.exit()

e = enki.Enki(settings.APIKEY, settings.SERVER, settings.PROJECT)

e.get_all()


po = polib.pofile('/tmp/messages.po')
for entry in po.untranslated_entries():
    for t in e.tasks:
        task_entry = polib.POEntry(
            msgid=t.info['msgid'],
            msgstr=t.info['msgstr'],
            occurrences=t.info['occurrences'])
        if entry.msgid == task_entry.msgid:
            entry.msgstr = e.task_runs_df[t.id]['msgstr'].describe()['top']

po.save('/tmp/new_messages.po')
po.save_as_mofile('/tmp/messages.mo')
