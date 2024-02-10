# Act 3: Hello loader

Our next challenge is to load the source CSV file into the model.

We are going to do this using Django's system for [management commands](https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/). It allows us to make our own `manage.py` commands like `migrate` and `startapp` that take advantage of Django's bag of tricks and interact with the database.

To do this, add a `management/commands` directory in our academy app, complete with empty `__init__.py` files required by Python. You can do this in your operating system's file explorer, or on the command line. From a Linux or OSX prompt that would look something like this.

```bash
# The -p flag here makes both new directories
mkdir -p academy/management/commands
# This creates the empty files on Macs or in Linux
touch academy/management/__init__.py
touch academy/management/commands/__init__.py
```

From Windows something more like this:

```bash
# If you're in Windows create them with your text editor
start notepad++ academy/management/__init__.py
start notepad++ academy/management/commands/__init__.py
```

When you're done the app's directory should look something like this.

```txt
academy/
    __init__.py
    admin.py
    apps.py
    models.py
    management/
        __init__.py
        commands/
            __init__.py
    migrations/
    tests.py
    views.py
```

Create a new file in the `management/commands` directory where the new command will go. Let's call it `loadacademycsv.py`.

```bash
# Mac or Linux
touch academy/management/commands/loadacademycsv.py
# Windows
start notepad++ academy/management/commands/loadacademycsv.py
```

Open it up and paste in the skeleton common to all management commands.

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
```

Running it is as simple as invoking its name with `manage.py`.

```bash
python manage.py loadacademycsv
```

Download [the source CSV file](https://raw.githubusercontent.com/palewire/first-django-admin/master/project/academy_invites_2014.csv) from GitHub and store it in your base directory next to `manage.py`.

Return to the management command and introduce Python's built-in [csv module](https://docs.python.org/3/library/csv.html), which can read and files CSV files.

```{code-block} python
:emphasize-lines: 1

import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Loading CSV"
```

Next add a variable beneath the print command that contains the path to where you've saved the CSV file. If you've saved it next to `manage.py`, that is as simple as starting off with "./".

```{code-block} python
:emphasize-lines: 8

import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Loading CSV"
        csv_path = "./academy_invites_2014.csv"
```

:::{note}
In case you don't already know, a “variable” is a fancy computer programming word for a named shortcut where we save our work as we go.
:::

Now access the file at that path with Python's built-in `open` function.

```{code-block} python
:emphasize-lines: 9

import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Loading CSV"
        csv_path = "./academy_invites_2014.csv"
        csv_file = open(csv_path, 'rb')
```

Feeding the file object it creates into the `csv` module's `DictReader` will return a list with each row read to work with.

```{code-block} python
:emphasize-lines: 10

import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Loading CSV"
        csv_path = "./academy_invites_2014.csv"
        csv_file = open(csv_path, 'rb')
        csv_reader = csv.DictReader(csv_file)
```

Create a loop that walks through the list, printing out each row as it goes by.

```{code-block} python
:emphasize-lines: 11-12

import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Loading CSV"
        csv_path = "./academy_invites_2014.csv"
        csv_file = open(csv_path, 'rb')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print row
```

Run it to see what we mean.

```bash
python manage.py loadacademycsv
```

Import our model into the command and use it to save the CSV records to the database.

```{code-block} python
:emphasize-lines: 2,13-17

import csv
from academy.models import Invite
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Loading CSV"
        csv_path = "./academy_invites_2014.csv"
        csv_file = open(csv_path, 'rb')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            obj = Invite.objects.create(
                name=row['Name'],
                branch=row['Branch']
            )
            print obj
```

Run it again and you've done it. The CSV is loaded into the database.

```bash
python manage.py loadacademycsv
```