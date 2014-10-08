import enki
import polib

e = enki.Enki('a', 'http://localhost:5001', 'translationsvoting')

e.get_all()


po = polib.POFile()
po.metadata = {
    'Project-Id-Version': '1.0',
    'Report-Msgid-Bugs-To': 'you@example.com',
    'POT-Creation-Date': '2007-10-18 14:00+0100',
    'PO-Revision-Date': '2007-10-18 14:00+0100',
    'Last-Translator': 'you <you@example.com>',
    'Language-Team': 'English <yourteam@example.com>',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Transfer-Encoding': '8bit',
}

for t in e.tasks:
    entry = polib.POEntry(
        msgid=t.info['msgid'],
        msgstr=e.task_runs_df[t.id]['msgid'].describe()['top'],
        occurrences=t.info['occurrences']
    )
    po.append(entry)

po.save('/tmp/mio.mo')
