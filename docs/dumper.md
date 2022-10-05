```{include} _templates/nav.html
```

# Epilogue: Hello dumper

Alright, so let's assume you work with some industrious reporters. They roll through all the records and you've got the gender, race and age entered for everybody in the database.

Here's how you can get the data back out as a CSV. We'll start by creating a new management command much like the one we made for the loader.

```bash
# Mac or Linux
touch academy/management/commands/dumpacademycsv.py
# Windows
start notepad++ academy/management/commands/dumpacademycsv.py
```

Open it up and paste in the barebones of a management command.

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Dumping CSV")
```

Import our Invite model and create a loop that runs through all the records
and prints out each field.

```{code-block} python
:emphasize-lines: 1,8-10

from academy.models import Invite
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Dumping CSV"
        for obj in Invite.objects.all():
            row = [obj.name, obj.branch, obj.gender, obj.date_of_birth, obj.race, obj.notes, obj.reporter]
            print(row)
```

Save the file and run the command. You should see all the data printed out in lists.

```python
python manage.py dumpacademycsv
```

Now introduce the csv module to output those rows to a new file.

```{code-block} python
:emphasize-lines: 1-3,11-14,17

import os
import csv
from django.conf import settings
from academy.models import Invite
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Dumping CSV"
        csv_path = os.path.join(settings.BASE_DIR, "dump.csv")
        csv_file = open(csv_path, 'w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['name', 'branch', 'gender', 'date_of_birth', 'race', 'notes', 'reporter'])
        for obj in Invite.objects.all():
            row = [obj.name, obj.branch, obj.gender, obj.date_of_birth, obj.race, obj.notes, obj.reporter]
            csv_writer.writerow(row)
```

Run our new command once more.

```python
python manage.py dumpacademycsv
```

Now open up `dump.csv` in your base directory and your export should be good to go.
