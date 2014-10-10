import enki
import polib

e = enki.Enki('a', 'http://localhost:5001', 'translationsvoting')

e.get_all()


po = polib.pofile('/tmp/messages.po')
for entry in po.untranslated_entries():
    for t in e.tasks:
        task_entry = polib.POEntry(
            msgid=t.info['msgid'],
            msgstr=t.info['msgstr'],
            occurrences=t.info['occurrences'])
        if entry.msgid == task_entry.msgid:
            entry.msgstr = e.task_runs_df[t.id]['msgid'].describe()['top']

po.save('/tmp/new_messages.po')
po.save_as_mofile('/tmp/messages.mo')
