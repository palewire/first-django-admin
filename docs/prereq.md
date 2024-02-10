# Prelude: Prerequisites

Before you can begin, your computer needs the following tools installed
and working.

1. A [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) to interact with your computer
2. A [text editor](https://en.wikipedia.org/wiki/Text_editor) to work with plain text files
3. Version 3.X of the [Python](https://www.python.org/downloads/) programming language
4. The [pipenv](https://pipenv.pypa.io/en/latest/) package and virtual environment manager for Python
5. [Git](http://git-scm.com/) version control software and an account at [GitHub.com](http://www.github.com)

:::{warning}
Stop and make sure you have all these tools installed and working properly. Otherwise, [you're gonna have a bad time](https://www.youtube.com/watch?v=ynxPshq8ERo).
:::

(command-line-prereq)=

## Command-line interface

Unless something is wrong with your computer, there should be a way to open a window that lets you type in commands. Different operating systems give this tool slightly different names, but they all have some form of it, and there are alternative programs you can install as well.

On Windows you can find the command-line interface by opening the "command prompt." Here are [instructions](https://www.bleepingcomputer.com/tutorials/windows-command-prompt-introduction/). On Apple computers, you open the ["Terminal" application](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line). Ubuntu Linux comes with a program of the [same name](http://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it).

## Text editor

A program like Microsoft Word, which can do all sorts of text formatting
such as change the size and color of words, is not what you need. Do not
try to use it below.

You need a program that works with simple ["plain text"
files](https://en.wikipedia.org/wiki/Text_file), and is therefore
capable of editing documents containing Python code, HTML markup and
other languages without dressing them up by adding anything extra. Such
programs are easy to find and some of the best ones are free, including
those below.

For Windows, I recommend installing
[Notepad++](https://notepad-plus-plus.org/). For Apple computers, try
[Atom](https://atom.io/).
In Ubuntu Linux you can stick with the pre-installed
[gedit](https://help.ubuntu.com/community/gedit) text editor.

## Python

Python is a computer programming language, like many others you may have heard of such as Ruby or PHP or Java. It is free and open source. We'll be installing Python 3 in a virtual environment, so it doesn't matter what version you have installed currently.

### For Mac

If you are using Mac OSX, Python version 2.7 is probably already installed, but we'll be using Python 3. To install that, we'll be using [Homebrew](https://docs.python-guide.org/starting/install3/osx/#install3-osx).

To install Python via Homebrew, you can run the following code:

```bash
brew install python
```

:::{note}
You'll note that the example above begins with a "\$". You do not need to type this. It is only a generic symbol
commonly used by geeks to indicate a piece of code should be run from the command line. On Windows, this prompt could even look quite different, likely starting with a phrase like `C:\`.
:::

You should see something like this after you hit enter:

```bash
python -V
Python 3.9.7
```

### For Windows

Windows people should follow the instructions [here](https://docs.python-guide.org/starting/install3/win/#install3-windows).

(command-line-pipenv)=

## pipenv

The [pipenv package manager](https://pipenv.pypa.io/) makes it easy to install open-source libraries that expand what you're able to do with Python. Later, we will use it to install everything needed to create a working web application.

Verify pipenv is installed with the following command:

```bash
pipenv -v
```

If you get and error, that means you don't have pipenv installed. You can get it by following [these instructions](https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv).