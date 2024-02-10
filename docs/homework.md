# Act 6: Hello homework

There are two constants in this kind of work: 1) Your models will change. 2) Reporters need to be told what to do.

With that in mind, let's alter our model so we have a place for a reporter's name. Then we will assign each invitee to a reporter to finish.

First, let's add a character field and some choices for the reporter's name. Open your `models.py` file and add them.

```{code-block} python
:emphasize-lines: 33-43

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
    REPORTER_CHOICES = (
        ("lois-lane", "Lois Lane"),
        ("clark-kent", "Clark Kent"),
        ("jimmy-olson", "Jimmy Olson")
    )
    reporter = models.CharField(
        max_length=255,
        choices=REPORTER_CHOICES,
        blank=True
    )
```

Great. Save it and let's run:

```bash
python manage.py runserver
```

Now go to [http://localhost:8000/admin/](http://localhost:8000/admin/) and click on 'Invites.' You should see this:

```{image} /_static/hello-newsroom-nomigrationerror.png
```

Uh oh. What happened? Well, in Django parlance, we are missing a migration. While your `models.py` file describes your database tables, simply changing the file won't change your database. Django needs some instructions on how to create, delete or migrate fields in an explicit way. This is where migrations come in. Migrations explain how to modify your database, including the ability to "roll back" your database tables to a previous state.

Thankfully, in newer versions of Django, this feature is built in. Kill your `runserver` by hitting `ctrl-c`, and run a command:

```bash
# Create a migration
python manage.py makemigrations academy
```

This creates a file that says we want to add a reporter field to our database.  Let's check to see what we did. List the contents of `academy/migrations/`

```bash
# In OSX or Linux
ls academy/migrations/
# In Windows
dir academy/migrations
```

You should see that there are two migration files there: `0001_initial.py` and `0002_invite_reporter.py`. When you created your table before, you ran the `makemigrations` command as well, which created the initial file. Every time you make a migration, Django will add another file to this folder.

:::{note}
If you're using `git` to track your project, it's important to add these migrations to your git repository. Otherwise people collaborating with you won't know what changes you have made to the database.
:::

Now we have to apply the migration. Your changes won't be applied to the database until you run `migrate`, so let's do that now

```bash
# Actually apply the migrations
python manage.py migrate academy
```

Excellent. Run your server and check out an invite now. You should see a dropdown like this:

```{image} /_static/hello-newsroom-reporter.png
```

Wouldn't it be great if you could see this information at a glance, though? Pop open your `admin.py` file and let's do just that. We will add "reporter" to the end of our `list_display` list.

```{code-block} python
:emphasize-lines: 5

from django.contrib import admin
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "gender", "date_of_birth", "race", "reporter",)
    list_filter = ("branch", "gender", "race",)
    search_fields = ("name",)

admin.site.register(Invite, InviteAdmin)
```

Now fire up your runserver again and check out the invite list:

```{image} /_static/hello-newsroom-nones.png
```

That's a whole lot of blanks though, and do you really want to go into each page and select the name from a dropdown to assign it? No, you do not. Let's make one quick change to the `admin.py` file to speed this up. We are going to use a feature called `list_editable` to make changes directly from the invite list:

```{code-block} python
:emphasize-lines: 7

from django.contrib import admin
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "gender", "date_of_birth", "race", "reporter",)
    list_filter = ("branch", "gender", "race",)
    list_editable = ("reporter",)
    search_fields = ("name",)

admin.site.register(Invite, InviteAdmin)
```

Ready? Save the file and open up the invite list again.

```{image} /_static/hello-newsroom-list-editable.png
```

Now you can edit the reporter field directly from the admin list! Select a few reporters from a few dropdowns and then scroll to the bottom of the page and hit Save. Congratulations, you've just doled out some work.

The admin's `list_editable` is a powerful little option that lets you do a lot of work in a little time. When you've assigned enough people, you can turn the feature back off by removing or commenting out the `list_editable` line in the admin.

If you want to go further and filter by reporter so, for example, you could see all of Jimmy Olson's assignments at a glance, simply add "reporter" to the `list_filter` list.

```{code-block} python
:emphasize-lines: 6

from django.contrib import admin
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "gender", "date_of_birth", "race", "reporter",)
    list_filter = ("branch", "gender", "race", "reporter",)
    list_editable = ("reporter",)
    search_fields = ("name",)

admin.site.register(Invite, InviteAdmin)
```