## Translate PO or PROPeRTIES files in PyBossa

This project shows how you can translate a *po* or *properties* file in a PyBossa server.

Lots of projects and applications use gettext technology to localize their
strings. The same happens for Firefox extensions with the PROPERTIES files for
their extensions and addons.

This project shows how you can crowd-translate those projects using PyBossa
technology.

## Translating PO files

For translating PO files all you have to do is to pass the *pot* file generated
by gettext to [pbs](https://github.com/PyBossa/pbs):

```bash
pbs create_project
pbs update_project
pbs add_tasks --task-file=messages.pot --tasks-type=po --redundancy=3
```

Those three commands will create the *translations* project for you, add the
templates, and upload the strings to translate.

**NOTE**: we strongly recommend to change the name of the project to something
like: project-to-language. For example: pybossa-to-spanish

Now you can invite your users and volunteers to translate the strings. When all
the strings are translated, you will create a new project to vote for the best
translated string:


```bash
pbs --project project_voting.json create_project
pbs --project project_voting.json update_project
```

Now, we've to get the translated strings and pass them to the new project:

```bash
python vote.py
pbs --project project_voting.json add_tasks --task-file=/tmp/translations_voting_tasks.json --redundancy=5
```

The first command will download all the translated strings, and transform them
for the second project. It creates a file in the */tmp/* folder named
*translations_voting_tasks.json*, and that file is the one that we used to
populate the second project.

Once all the tasks of this second project have been completed, now you can
generate your new *mo* file with this command:

```bash
python create_mo.py
```

It will create an *mo* file for you in the */tmp* folder. Copy and paste that
file in your translations folder and you will be done.

## Translating Firefox extensions and/or addons

Firefox extensions and addons use PROPERTIES files to localize them. The
PyBossa pbs command supports that file too, so all you have to do is follow the
same steps as before, but with slightly changes.

For creating the tasks you will pass the properties file:

```bash
pbs add_tasks --task-file=en-US.properties --tasks-type=properties --redundancy=3
```

Then, run the voting command as before, and once the voting has been completed,
run the following command to create the translated PROPERTIES file:

```bash
python create_properties.py
```

This will create a new file in the */tmp/* folder named *file.properties*.

## License

Please, see COPYING file.
