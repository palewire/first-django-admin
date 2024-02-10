# Act 4: Hello admin

One of Django's unique features is that it comes with a custom administration that allows users to view, edit and create records. To see it in action, create a new superuser with permission to edit all records.

```bash
python manage.py createsuperuser
```

Then fire up the Django test server.

```bash
python manage.py runserver
```

And visit [localhost:8000/admin/](http://localhost:8000/admin/) and log in using the credentials you just created.

```{image} /_static/hello-admin-login.png
```

Without any additional configuration you will see administration panels for the apps installed with Django by default.

```{image} /_static/hello-admin-noconfig.png
```

Adding panels for your own models is done in the `admin.py` file included with each app. Open `academy/admin.py` to start in.

```python
from django.contrib import admin
from academy.models import Invite

admin.site.register(Invite)
```

Now reload [localhost:8000/admin/](http://localhost:8000/admin/) and you'll see it added to the index app list.

```{image} /_static/hello-admin-module.png
```

Click on "Invite" and you'll see all the records we loaded into the database as a list.

```{image} /_static/hello-admin-list.png
```

Configure the columns that appear in the list.

```{code-block} python
:emphasize-lines: 4-7

from django.contrib import admin
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "gender", "date_of_birth", "race")

admin.site.register(Invite, InviteAdmin)
```

Reload.

```{image} /_static/hello-admin-columns.png
```

Add a filter.

```{code-block} python
:emphasize-lines: 6

from django.contrib import admin
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "gender", "date_of_birth", "race")
    list_filter = ("branch", "gender", "race")

admin.site.register(Invite, InviteAdmin)
```

Reload.

```{image} /_static/hello-admin-filter.png
```

And now a search.

```{code-block} python
:emphasize-lines: 7

from django.contrib import admin
from academy.models import Invite

class InviteAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "gender", "date_of_birth", "race")
    list_filter = ("branch", "gender", "race")
    search_fields = ("name",)

admin.site.register(Invite, InviteAdmin)
```

Reload.

```{image} /_static/hello-admin-search.png
```

Take a moment to search, filter and sort the list to see how things work. You can even fill in a few records if you want to give that a spin.