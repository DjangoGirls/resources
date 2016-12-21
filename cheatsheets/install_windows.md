# Installation - Windows

## Installing Python

You can download Python for Windows from the website https://www.python.org/downloads/release/python-342/. After downloading the ***.msi** file, you should run it (double-click on it) and follow the instructions there. It is important to remember the path (the directory) where you installed Python. It will be needed later!

## Virtual environment

Before we install Django, we'll create a **virtual environment** (also called a *virtualenv*). It will isolate your Python/Django setup on a per-project basis, meaning that any changes you make to one website won't affect any others you're also developing.

All you need to do is find a directory in which you want to create the `virtualenv`; for this tutorial we will be using a new directory `djangogirls` from your home directory:

    mkdir djangogirls
    cd djangogirls

We will make a virtualenv called `myvenv`. 

To create a new `virtualenv`, you need to open the console and run `C:\Python34\python -m venv myvenv`. It will look like this:

    C:\Users\Name\djangogirls> C:\Python34\python -m venv myvenv

where `C:\Python34\python` is the directory in which you previously installed Python and `myvenv` is the name of your `virtualenv`. You can use any other name, but stick to lowercase and use no spaces. It is also good idea to keep the name short - you'll be referencing it a lot!

### Working with virtualenv

The command above will create a directory called `myvenv` (or whatever name you chose) that contains our virtual environment (basically a bunch of directory and files). All we want to do now is start it by running:

    C:\Users\Name\djangogirls> myvenv\Scripts\activate

Remember to replace `myvenv` with your chosen `virtualenv` name!

You will know that you have `virtualenv` started when you see that the prompt in your console looks like:

    (myvenv) C:\Users\Name\djangogirls>

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

> If you get an error when calling pip on Windows platform please check if your project pathname contains spaces (i.e. `C:\Users\User Name\djangogirls`). If it does please consider moving it to another place without spaces (suggestion is: `C:\djangogirls`). After the move please try the above command again.

## Heroku account

Heroku (http://heroku.com/) is a service which we will use to host your website. 

You need to install your Heroku toolbelt which you can find here: https://toolbelt.heroku.com/

> When running the Heroku toolbelt installation program on Windows make sure to choose "Custom Installation" when being asked which components to install. In the list of components that shows up after that please additionally check the checkbox in front of "Git and SSH".

> On Windows you also must run the following command to add Git and SSH to your command prompt's `PATH`: `setx PATH "%PATH%;C:\Program Files\Git\bin"`. Restart the command prompt program afterwards to enable the change.

Please also create a free Heroku account here: https://id.heroku.com/signup/www-home-top

Then authenticate your Heroku account on your computer by running this command:

    $ heroku login

In case you don't have an SSH key this command will automatically create one. SSH keys are required to push code to the Heroku.

## Code editor

* Gedit: [download here](https://wiki.gnome.org/Apps/Gedit#Download) (https://wiki.gnome.org/Apps/Gedit#Download)

* Sublime Text 2: [download here](http://www.sublimetext.com/2) (http://www.sublimetext.com/2)

* Atom: [download here](https://atom.io/) (https://atom.io/)