# Installation - OSX

## Installing Python

You need to go to the website https://www.python.org/downloads/release/python-342/ and download the Python installer:

* download the *Mac OS X 64-bit/32-bit installer* *DMG* file,
* double click to open it,
* double click *Python.mpkg* to run the installer.

Verify the installation was successful by opening the *Terminal* application and running the `python3` command:

    $ python3 --version
    Python 3.4.2

## Virtual environment

Before we install Django, we'll create a **virtual environment** (also called a *virtualenv*). It will isolate your Python/Django setup on a per-project basis, meaning that any changes you make to one website won't affect any others you're also developing.

All you need to do is find a directory in which you want to create the `virtualenv`; for this tutorial we will be using a new directory `djangogirls` from your home directory:

    mkdir djangogirls
    cd djangogirls

We will make a virtualenv called `myvenv`. 

Creating a `virtualenv` is as simple as running `python3 -m venv myvenv`.
It will look like this:

    ~/djangogirls$ python3 -m venv myvenv

`myvenv` is the name of your `virtualenv`. You can use any other name, but stick to lowercase and use no spaces. It is also good idea to keep the name short - you'll be referencing it a lot!

### Working with virtualenv

The command above will create a directory called `myvenv` (or whatever name you chose) that contains our virtual environment (basically a bunch of directory and files). All we want to do now is start it by running:

    ~/djangogirls$ source myvenv/bin/activate

Remember to replace `myvenv` with your chosen `virtualenv` name!

You will know that you have `virtualenv` started when you see that the prompt in your console looks like:

    (myvenv) ~/djangogirls$

Notice the prefix `(myvenv)` appears!

When working within a virtual environment, `python` will automatically refer to the correct version so you can use `python` instead of `python3`.

OK, we have all important dependencies in place. We can finally install Django!

## Installing Django

Now that you have your `virtualenv` started, you can install Django using `pip`. In the console, run `pip install django==1.7.1` (note that we use a double equal sign: `==`).

    (myvenv) ~$ pip install django==1.7.1
    Downloading/unpacking django==1.7.1
    Installing collected packages: django
    Successfully installed django
    Cleaning up...

## Heroku account

Heroku (http://heroku.com/) is a service which we will use to host your website. 

You need to install your Heroku toolbelt which you can find here: https://toolbelt.heroku.com/

Please also create a free Heroku account here: https://id.heroku.com/signup/www-home-top

Then authenticate your Heroku account on your computer by running this command:

    $ heroku login

In case you don't have an SSH key this command will automatically create one. SSH keys are required to push code to the Heroku.

## Code editor

There are a lot of different editors and it largely boils down to personal preference. Some suggestions are below, but feel free to ask your coach what their preferences are.

* Gedit: [download here](https://wiki.gnome.org/Apps/Gedit#Download) (https://wiki.gnome.org/Apps/Gedit#Download)

* Sublime Text 2: [download here](http://www.sublimetext.com/2) (http://www.sublimetext.com/2)

* Atom: [download here](https://atom.io/) (https://atom.io/)