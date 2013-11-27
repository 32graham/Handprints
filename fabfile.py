from __future__ import with_statement
import posixpath

from fabric.api import run, env, task
from fabric.context_managers import cd, settings


# Host and login username:
env.hosts = ['jgraham32@jgraham32.webfactional.com']

# Directory where everything to do with this app will be stored on the server.
DJANGO_APP_ROOT = '/home/jgraham32/webapps/handprints_app/'

# Directory where static sources should be collected.  This must equal the value
# of STATIC_ROOT in the settings.py that is used on the server.
STATIC_ROOT = '/home/jgraham32/webapps/handprints_static/'

# Subdirectory of DJANGO_APP_ROOT in which project sources will be stored
SRC_SUBDIR = 'handprints'

# Python version
PYTHON_BIN = "python2.7"
PYTHON_PREFIX = "" # e.g. /usr/local  Use "" for automatic
PYTHON_FULL_PATH = "%s/bin/%s" % (PYTHON_PREFIX, PYTHON_BIN) if PYTHON_PREFIX else PYTHON_BIN


# Commands to stop and start the webserver that is serving the Django app.
DJANGO_SERVER_STOP = posixpath.join(DJANGO_APP_ROOT, 'apache2', 'bin', 'stop')
DJANGO_SERVER_START = posixpath.join(DJANGO_APP_ROOT, 'apache2', 'bin', 'start')
DJANGO_SERVER_RESTART = None

src_dir = posixpath.join(DJANGO_APP_ROOT, SRC_SUBDIR)


def push_sources():
    """
    Push source code to server
    """
    run("rm -rf /home/jgraham32/webapps/handprints_app/handprints")
    run("git clone https://josh_graham@bitbucket.org/josh_graham/handprints.git /home/jgraham32/webapps/handprints_app/handprints")


def update_database():
    """
    Update the database using syncdb and south
    """
    run("python2.7 /home/jgraham32/webapps/handprints_app/handprints/manage.py syncdb --all")
    run("python2.7 /home/jgraham32/webapps/handprints_app/handprints/manage.py migrate")


def install_dependencies():
    """
    Install required packages
    """
    run("pip install -r /home/jgraham32/webapps/handprints_app/handprints/requirements.txt")


@task
def webserver_stop():
    """
    Stop the webserver that is running the Django instance
    """
    run(DJANGO_SERVER_STOP)


@task
def webserver_start():
    """
    Starts the webserver that is running the Django instance
    """
    run(DJANGO_SERVER_START)


@task
def webserver_restart():
    """
    Restarts the webserver that is running the Django instance
    """
    if DJANGO_SERVER_RESTART:
        run(DJANGO_SERVER_RESTART)
    else:
        with settings(warn_only=True):
            webserver_stop()
        webserver_start()


def build_static():
    assert STATIC_ROOT.strip() != '' and STATIC_ROOT.strip() != '/'
    # Before Django 1.4 we don't have the --clear option to collectstatic
    run("rm -rf %s/*" % STATIC_ROOT)

    with cd(src_dir):
        run("python2.7 ./manage.py collectstatic -v 0 --noinput")

    run("chmod -R ugo+r %s" % STATIC_ROOT)

@task
def deploy():
    """
    Deploy project.
    """
    with settings(warn_only=True):
        webserver_stop()

    push_sources()
    #install_dependencies()
    update_database()
    build_static()

    webserver_start()
