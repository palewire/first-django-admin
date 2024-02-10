# Act 2: Hello models

Now we create our app. In Django terms, an app is a collection of files that does something, like publish a blog or store public records. A project, like we made above, collects those apps and organizes them into a working website.

You can create a new app with Django's `startapp` command. Since we are aiming to make a list of people invited to join the academy, naming this one isn't too hard.

Return to your terminal and hit the combination of `CTRL-C`, which will terminal your test server and return you to the command line. Then use our friend `manage.py` to create our app.

```bash
python manage.py startapp academy
```

There should now be a new `academy` folder in your project. If you look inside you will see that Django created a series of files common to every app.

```txt
academy/
    __init__.py
    admin.py
    apps.py
    migrations/
    models.py
    tests.py
    views.py
```

We will only be using two of them in this tutorial. The file called `models.py` is where we will design our database tables. Another called `admin.py` is where we will configure the panels where reporters will be able to enrich the source data.

But before we do any of that, we need to configure our project to include our new app. Use your text editor to open the file `settings.py` in the `project` directory. Add our app, `academy`, to the `INSTALLED_APPS` list you find there.

```{code-block} python
:emphasize-lines: 8

  INSTALLED_APPS = (
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'academy',
  )
```

:::{note}
Python, like most programming languages, is very strict. When you add a new word to a list, as we did above, it always needs to be followed by a comma and surrounded by quotes. The indentations are also very stict and need to be consistent from line to line. Also, lines starting with `#` or surrounding by `"""` quotes are comments that will not be run as code and are instead there only as documentation.
:::

Next open up the `models.py` file in the `academy` app's directory. Here we will use Django's built-in [models](https://docs.djangoproject.com/en/4.0/topics/db/models/) system to design a database table to hold the source data.

Each table is defined using a Python [class](http://www.learnpython.org/en/Classes_and_Objects) that inherits special powers [from Django](https://docs.djangoproject.com/en/dev/topics/db/models/). Those special powers allow it to synchronize with an underlying database. Our work begins by creating our class and naming it after the data we'll put inside.

```{code-block} python
:emphasize-lines: 4

from django.db import models

# Create your models here.
class Invite(models.Model):
```

:::{note}
Don't know what a class is? Don't stress out about it. It's a little tricky to explain, but a class is basically a blueprint for designing how information in your code is structured. In our case, we're creating a blueprint that will link up our data with a traditional database table (this is often called a schema).
:::

Next, like any good database table, it needs some fields.

If you open [the source CSV](https://github.com/palewire/first-django-admin/blob/master/project/academy_invites_2014.csv), you will see that is has only two columns: name and branch.

Django has some [fancy tricks](https://docs.djangoproject.com/en/4.0/ref/models/fields/) for defining fields depending on what kind of data they hold. Now we'll use the `CharField` to expand our models to hold the name and branch data from our source. It just so happens, that CharFields have a maximum length that must always be set. We're going to pick a couple big numbers for that.

```{code-block} python
:emphasize-lines: 5-6

  from django.db import models

  # Create your models here.
  class Invite(models.Model):
      name = models.CharField(max_length=500)
      branch = models.CharField(max_length=500)
```

:::{note}
Watch out. You'll need to carefully indent your code according to Python's very [strict rules](https://www.geeksforgeeks.org/indentation-in-python/) for this to work.
:::

Now let's add a few more fields that we will ask the reporters to figure out and fill in. We'll use another Django trick, the `choices` option, to make some of them multiple-choice fields rather than free text.

First gender.

```{code-block} python
:emphasize-lines: 7-18

from django.db import models

# Create your models here.
class Invite(models.Model):
    name = models.CharField(max_length=500)
    branch = models.CharField(max_length=500)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
        ("?", "Unknown")
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="?"
    )
```

:::{note}
When you create a choices list each option needs to have two values. The first one is what is written into the database, and is often more compact. The second one is what is displayed for the user, and is often more verbose.
:::

Then the invitee's date of birth. Since this type of field will start off empty we need to instruct the database to: 1) allow null values with `null=True` and 2) allow entrants to leave it empty when they update records later with `blank=True`.

```{code-block} python
:emphasize-lines: 18

from django.db import models

# Create your models here.
class Invite(models.Model):
    name = models.CharField(max_length=500)
    branch = models.CharField(max_length=500)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
        ("?", "Unknown")
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="?"
    )
    date_of_birth = models.DateField(null=True, blank=True)
```

Race.

```{code-block} python
:emphasize-lines: 19-32

from django.db import models

# Create your models here.
class Invite(models.Model):
    name = models.CharField(max_length=500)
    branch = models.CharField(max_length=500)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
        ("?", "Unknown")
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="?"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    RACE_CHOICES = (
        ("ASIAN", "Asian"),
        ("BLACK", "Black"),
        ("LATINO", "Latino"),
        ("WHITE", "White"),
        ("OTHER", "Other"),
        ("?", "Unknown"),
    )
    race = models.CharField(
        max_length=10,
        choices=RACE_CHOICES,
        default="?"
    )
```

Finally, an open-ended text field for reporters to leave notes about their decisions.

```{code-block} python
:emphasize-lines: 32

from django.db import models

# Create your models here.
class Invite(models.Model):
    name = models.CharField(max_length=500)
    branch = models.CharField(max_length=500)
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
        ("?", "Unknown")
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="?"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    RACE_CHOICES = (
        ("ASIAN", "Asian"),
        ("BLACK", "Black"),
        ("LATINO", "Latino"),
        ("WHITE", "White"),
        ("OTHER", "Other"),
        ("?", "Unknown"),
    )
    race = models.CharField(
        max_length=10,
        choices=RACE_CHOICES,
        default="?"
    )
    notes = models.TextField(blank=True)
```

Congratulations, you've written your first model. But it won't be created as a real table in your database until you run what Django calls a "migration." That's just a fancy word for syncing our models with our database.

Make sure to save your `models.py` file. Then we'll `manage.py` to prepare the changes necessary to create your new model.

```bash
python manage.py makemigrations academy
```

Now run the `migrate` command to execute it.

```bash
python manage.py migrate academy
```

That's it. You've made your database table.