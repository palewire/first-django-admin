# Act 5: Hello newsroom

Now you're ready to get other people involved. The first thing to do is create additional users for your colleagues. Return to [localhost:8000/admin/](http://localhost:8000/admin/) and click the plus button to the right of the "Users" link.

```{image} /_static/hello-newsroom-userlink.png
```

Name a user.

```{image} /_static/hello-newsroom-nameuser.png
```

When filling in their profile, be **certain** to click on the "staff status" checkbox that gives users authorization to access the admin.

```{image} /_static/hello-newsroom-staffstatus.png
```

Lower down, choose which permissions to give this user. In this example, since the source data are already loaded the reporter will only have authorization to edit records, not create or delete them.

```{image} /_static/hello-newsroom-permissions.png
```

We're getting close. One problem, though. That `localhost` address we've been using isn't on the Internet. It only exists on your machine.

There are numerous ways to deploy your Django application so other people can access it. You could use the [Apache](https://docs.djangoproject.com/en/4.0/howto/deployment/) webserver. You could try a cloud service like [Heroku](https://devcenter.heroku.com/articles/getting-started-with-django).

But if all you need is for other people inside your office network (often referred to as an "Intranet") to log in, here's a simple trick that will work in most cases.

Return to your command line, hit `CTRL-C` and try this.

```bash
python manage.py runserver 0.0.0.0:8000
```

Now all you need to do is find your computer's IP address and others in your office will soon be able to access it. The method varies depending on your operating system. Good instructions are [available here](http://home.huck.psu.edu/it/how-to/how-to-ip-address). Though it mostly boils down to opening a new command line terminal and typing in one of the following.

```bash
# In OSX or Linux
ifconfig
# In Windows
ipconfig
```

Then within the code that comes out you'll see a series of numbers formatted something like 172.19.131.101 after a label like "inet" or "IPv4 Address".

Copy and paste that into your clipboard. Open up the `settings.py` file and add it, along with localhost, to the empty `ALLOWED_HOSTS` setting. This list controls what web addresses are able to access your database.

```python
ALLOWED_HOSTS = [
    'localhost',
    '192.168.1.79',
]
```

Save that file and then go to your browser and paste that same IP address into a pattern like [http://xxx.xx.xxx.xx:8000/admin/](http://XXX.YY.ZZZ.QQ:8000/admin/) and see what happens. If your Django site appears, you're off to a good start.

Now visit your colleagues' computers across the newsroom and if the same address works. If it does, you're ready to roll.

```{image} /_static/hello-newsroom-permissions.png
```

Now as long as the runserver command is up and running back at your computer, your data entry website is online. Congratulations!