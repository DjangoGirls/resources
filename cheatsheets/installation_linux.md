# Installation - Linux

## Installing Python

It is very likely that you already have Python installed out of the box. To check if you have it installed (and which version it is), open a console and type the following command:

    $ python3 --version
    Python 3.4.2

If you don't have Python installed or if you want a different version, you can install it as follows:

#### Ubuntu

Type this command into your console:

    sudo apt-get install python3.4

#### Fedora

Use this command in your console:

    sudo yum install python3.4

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

> __NOTE:__ Initiating the virtual environment on Ubuntu 14.04 like this currently gives the following error:

>     Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1

> To get around this, use the `virtualenv` command instead.

>     ~/djangogirls$ sudo apt-get install python-virtualenv
>     ~/djangogirls$ virtualenv --python=python3.4 myvenv

### Working with virtualenv

The command above will create a directory called `myvenv` (or whatever name you chose) that contains our virtual environment (basically a bunch of directory and files). All we want to do now is start it by running:

    ~/djangogirls$ source myvenv/bin/activate

Remember to replace `myvenv` with your chosen `virtualenv` name!

> __NOTE:__ sometimes `source` might not be available. In those cases try doing this instead:

>     ~/djangogirls$ . myvenv/bin/activate


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

on Linux
> If you get an error when calling pip on Ubuntu 12.04 please run `python -m pip install -U --force-reinstall pip` to fix the pip installation in the virtualenv.

## Heroku account

Heroku (http://heroku.com/) is a service which we will use to host your website. 

You need to install your Heroku toolbelt which you can find here: https://toolbelt.heroku.com

Please also create a free Heroku account here: https://id.heroku.com/signup/www-home-top

Then authenticate your Heroku account on your computer by running this command:

    $ heroku login

In case you don't have an SSH key this command will automatically create one. SSH keys are required to push code to the Heroku.

## Code editor

There are a lot of different editors and it largely boils down to personal preference. Some suggestions are below, but feel free to ask your coach what their preferences are.

* Gedit: [download here](https://wiki.gnome.org/Apps/Gedit#Download) (https://wiki.gnome.org/Apps/Gedit#Download)

* Sublime Text 2: [download here](http://www.sublimetext.com/2) (http://www.sublimetext.com/2)

* Atom: [download here](https://atom.io/) (https://atom.io/)