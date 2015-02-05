:tocdepth: 2

First Django admin
==================

A step-by-step guide to creating a simple web application that empowers you to enlist reporters in data entry and refinement.

You will learn just enough about the [Django](https://www.djangoproject.com/) framework to design database tables, load in data and create an administration panel for others to improve it. You will not bother with all the other web developer crap.

This guide in currently being developed by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_ and Ken Schwencke for a workshop `scheduled for March 8 <http://ire.org/conferences/nicar2015/hands-on-training/>`_ at
the 2015 conference of the National Institute for Computer-Assisted Reporting in Atlanta.

-  Code:
   `github.com/ireapps/first-django-admin/ <https://github.com/ireapps/first-django-admin>`__
-  Issues:
   `github.com/ireapps/first-django-admin/issues/ <https://github.com/ireapps/first-django-admin/issues>`__

What you will make
------------------

This tutorial will guide you through creating a custom Django administration panel where reporters can inspect, edit and augment a list of invitees to the `Academy of Motion Picture Arts and Sciences <http://www.oscars.org/>`_, the elite organization that decides the Oscars.

In 2012, `a study by the Los Angeles Times <http://www.latimes.com/entertainment/movies/academy/la-et-unmasking-oscar-academy-project-html-htmlstory.html>`_ found the group is overwhelmingly white and male, which led to renewed calls to diversify the Oscar voting pool. A new list was used to write `a follow-up story <http://www.latimes.com/entertainment/envelope/moviesnow/la-et-mn-diversity-oscar-academy-members-20131221-story.html>`_ in 2013. The analysis appeared on the front page `again in early 2015 <http://www.latimes.com/entertainment/movies/la-et-mn-oscar-nominations-diversity-20150116-story.html#page=1>`_ when the academy was criticized after announcing a `virtually all-white slate <http://graphics.latimes.com/oscar-nominees-2015/>`_ of nominees.

By following the steps below, you will repeat The Times' work using the academy's 2014 list of new invitees, creating a system to share the load of producing a follow-up story in `this vein <http://www.latimes.com/entertainment/envelope/moviesnow/la-et-mn-diversity-oscar-academy-members-20131221-story.html>`_.

Prelude: Prerequisites
----------------------

Before you can begin, your computer needs the following tools installed
and working to participate.

1. A `command-line
   interface <https://en.wikipedia.org/wiki/Command-line_interface>`__
   to interact with your computer
2. A `text editor <https://en.wikipedia.org/wiki/Text_editor>`__ to work
   with plain text files
3. Version 2.7 of the
   `Python <http://python.org/download/releases/2.7.6/>`__ programming
   language
4. The `pip <https://pip.pypa.io/en/latest/installing.html>`_ package manager and `virtualenv <http://www.virtualenv.org/en/latest/>`_ environment manager for Python


.. note::

  Depending on your experience and operating system, you might
  already be ready to go with everything above. If so, move on to the next
  chapter. If not, don't worry. And don't give up! It will be a bit of a
  slog but the instructions below will point you in the right direction.

.. _command-line-prereq:

Command-line interface
~~~~~~~~~~~~~~~~~~~~~~

Unless something is wrong with your computer, there should be a way to
open a window that lets you type in commands. Different operating
systems give this tool slightly different names, but they all have some
form of it, and there are alternative programs you can install as well.

On Windows you can find the command-line interface by opening the
"command prompt." Here are instructions for `Windows
8 <http://windows.microsoft.com/en-us/windows/command-prompt-faq#1TC=windows-8>`__
and `earlier
versions <http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window>`__. On Apple computers, you open the `"Terminal"
application <http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line>`__. Ubuntu Linux comes with a program of the `same
name <http://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it>`__.

Text editor
~~~~~~~~~~~

A program like Microsoft Word, which can do all sorts of text formatting
like change the size and color of words, is not what you need. Do not
try to use it below.

You need a program that works with simple `"plain text"
files <https://en.wikipedia.org/wiki/Text_file>`__, and is therefore
capable of editing documents containing Python code, HTML markup and
other languages without dressing them up by adding anything extra. Such
programs are easy to find and some of the best ones are free, including
those below.

For Windows, I recommend installing
`Notepad++ <http://notepad-plus-plus.org/>`__. For Apple computers, try
`TextWrangler <http://www.barebones.com/products/textwrangler/download.html>`__.
In Ubuntu Linux you can stick with the pre-installed
`gedit <https://help.ubuntu.com/community/gedit>`__ text editor.

Python
~~~~~~

If you are using Mac OSX or a common flavor of Linux, Python is probably
already installed and you can test to see what version, if any, is there
waiting for you by typing the following into your terminal.

.. code:: bash

    $ python -V

.. note::

    You don't have to type the "$" It's just a generic symbol
    geeks use to show they're working on the command line.

If you don't have Python installed (a more likely fate for Windows
users) try downloading and installing it from
`here <http://www.python.org/download/releases/2.7.6/>`__.

In Windows, it's also crucial to make sure that the Python program is
available on your system's ``PATH`` so it can be called from anywhere on
the command line. `This
screencast <http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96>`__
can guide you through that process.

Python 2.7 is preferred but you can probably find a way to make most of
this tutorial work with other versions if you futz a little.

.. _command-line-pip:

pip and virtualenv
------------------

The `pip package manager <https://pip.pypa.io/en/latest/>`_
makes it easy to install open-source libraries that
expand what you're able to do with Python. Later, we will use it to install everything
needed to create a working web application.

If you don't have it already, you can get pip by following
`these instructions <https://pip.pypa.io/en/latest/installing.html>`_. In Windows, it's necessary to make sure that the
Python ``Scripts`` directory is available on your system's ``PATH`` so it can be called from anywhere on the command line. `This screencast <http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96>`_ can help.

Verify pip is installed with the following.

.. code-block:: bash

    $ pip -V

The `virtualenv environment manager <http://www.virtualenv.org/en/latest/>`_
makes it possible to create an isolated corner of your computer where all the different
tools you use to build an application are sealed off.

It might not be obvious why you need this, but it quickly becomes important when you need to juggle different tools
for different projects on one computer. By developing your applications inside separate
virtualenv environments, you can use different versions of the same third-party Python libraries without a conflict.
You can also more easily recreate your project on another machine, handy when
you want to copy your code to a server that publishes pages on the Internet.

You can check if virtualenv is installed with the following.

.. code-block:: bash

    $ virtualenv --version

If you don't have it, install it with pip.

.. code-block:: bash

    $ pip install virtualenv
    # If you're on a Mac or Linux and get an error saying you lack the right permissions, try it again as a superuser.
    $ sudo pip install virtualenv

If that doesn't work, `try following this advice <http://www.virtualenv.org/en/latest/virtualenv.html#installation>`_.

.. _activate:


Act 1: Hello Django
-------------------

Start by creating a new development environment with virtualenv. Name it after our application.

.. code-block:: bash

    # You don't have to type the "$" It's just a generic symbol
    # geeks use to show they're working on the command line.
    $ virtualenv first-django-admin

Jump into the directory it created.

.. code-block:: bash

    $ cd first-django-admin

Turn on the new virtualenv, which will instruct your terminal to only use those libraries installed
inside its sealed space. You only need to create the virtualenv once, but you'll need to repeat these
"activation" steps each time you return to working on this project.

.. code-block:: bash

    # In Linux or Mac OSX try this...
    $ . bin/activate
    # In Windows it might take something more like...
    $ cd Scripts
    $ activate
    $ cd ..

Make a new directory and move into it.

Use ``pip`` on the command line to install `Djang <https://www.djangoproject.com/>`_, a Python "framework"
we'll use to put together our website.

.. code-block:: bash

    $ pip install Django

Now use Django's ``django-admin`` command to create a new "project" that will be organized according to the framework's rules.

.. code-block:: bash

    $ django-admin startproject project

Now jump into the project and we'll start setting it up.

.. code-block:: bash

    $ cd project

.. note::

    Run the ``ls`` command, which lists the files in your current location. Wonder what all those weird files are in your new directory? We'll only need a couple for this tutorial, but you can read about all of them in the `official Django documentation <https://docs.djangoproject.com/en/1.7/intro/tutorial01/#creating-a-project>`_.

- Configure the settings (How much do we explain?)

Go back one directory before you create your app, which should exist alongside the project folder.

.. code-block:: bash

    $ cd ..

Now let's create the app. In Django terms, an "app" is a group of code files that describe the information in your database and how it functions in the Django admin. Optionally, it describes how you output the information into web pages or APIs.

Your app will have simple models to encapsulate the data in the Academy CSV, as well as fields we are interested in filling later for data collection

.. code-block:: bash

   $ django-admin startapp academy

The startapp command just created a barebones Django app for you. Jump in and let's see what files are there.

.. code-block:: bash

    $ cd academy

- Fire up the runserver for the first time to look at default admin

Act 2: Hello models
-------------------

- Draft a model to match our source CSV
- Write a management command that will load the CSV into the model

Act 3: Hello admin
------------------

- Create an admin to access and edit the new model
- Gradually refine it so it's better

Afterparty: Hello internet
--------------------------

Instructions for after you get home about how to host it on Amazon or something like that.

