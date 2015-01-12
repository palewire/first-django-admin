:tocdepth: 2

First django admin
==================

A step-by-step guide to creating a simple web application that empowers you to enlist reporters in data entry and refinement.

This guide in currently being developed by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_ and Ken Schwencke for a workshop scheduled for
the 2015 conference of the National Institute for Computer-Assisted Reporting. 

-  Code repository:
   `github.com/ireapps/first-django-admin/ <https://github.com/ireapps/first-django-admin>`__
-  Issues:
   `github.com/ireapps/first-django-admin/issues/ <https://github.com/ireapps/first-django-admin/issues>`__

What you will make
------------------

This tutorial will guide you through the creating a custom Django administration panel where reporters can inspect, edit and augment a list of inductees to the Academy of Motion Picture Arts and Sciences, the elite organization that decides the Oscars.

In 2012, `a study by the Los Angeles Times <http://www.latimes.com/entertainment/movies/academy/la-et-unmasking-oscar-academy-project-html-htmlstory.html>`_ found the group is overwhelmingly white and male, which led to renewed calls to diversify the Oscar voting pool. By following the steps below, you will repeat The Times' work using the Academy's 2014 list of new members, creating a system to share the load of producing a follow-up story in `this vein <http://www.latimes.com/entertainment/envelope/moviesnow/la-et-mn-diversity-oscar-academy-members-20131221-story.html>`_.

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
4. The `pip <https://pip.pypa.io/en/latest/installing.html>`__
   package manager for Python

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

pip
~~~

The `pip package
manager <https://pip.pypa.io/en/latest/>`__ makes it
easy to install open-source libraries that expand what you're able to do
with Python. Later, we will use it to install everything needed to
create a working web application.

If you don't have it already, you can get pip by following `these
instructions <https://pip.pypa.io/en/latest/installing.html>`__.
In Windows, it's necessary to make sure that the Python ``Scripts``
directory is available on your system's ``PATH`` so it can be called
from anywhere on the command line. `This
screencast <http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96>`__
can help.

Verify pip is installed with the following.

.. code:: bash

    $ pip -V


Act 1: Hello Django
-------------------

- Create a new Django project
- Configure the settings
- Create an app
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

