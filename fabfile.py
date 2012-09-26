"""
Starter fabfile for deploying the DjangoApp project.

Change all the things marked CHANGEME. Other things can be left at their
defaults if you are happy with the default layout.
"""

import posixpath

from fabric.api import run, local, env, settings, cd, task
from fabric.contrib.files import exists
from fabric.operations import _prefix_commands, _prefix_env_vars
#from fabric.decorators import runs_once
#from fabric.context_managers import cd, lcd, settings, hide

# CHANGEME
env.home = '/opt/www'
env.dev_server = '192.168.125.94:8000'
env.sup_lang = 'ru'
env.hosts = ['jbo@app03.089.com.ua']
env.code_dir = "{0}/DjangoApp".format(env.home)
env.project_dir = "{0}/DjangoApp/DjangoApp".format(env.home)
env.static_root = "{0}/DjangoApp/static/".format(env.home)
env.virtualenv = "{0}/DjangoApp/.virtualenv".format(env.home)
env.code_repo = 'git@github.com:user/DjangoApp.git'
env.django_settings_module = 'DjangoApp.settings'

# Python version
PYTHON_BIN = "python2.7"
PYTHON_PREFIX = ""  # e.g. /usr/local  Use "" for automatic
PYTHON_FULL_PATH = "%s/bin/%s" % (PYTHON_PREFIX, PYTHON_BIN) if PYTHON_PREFIX else PYTHON_BIN

# Set to true if you can restart your webserver (via wsgi.py), false to stop/start your webserver
# CHANGEME
DJANGO_SERVER_RESTART = False


def virtualenv(venv_dir):
    """
    Context manager that establishes a virtualenv to use.
    """
    return settings(venv=venv_dir)


def run_venv(command, **kwargs):
    """
    Runs a command in a virtualenv (which has been specified using
    the virtualenv context manager
    """
    run("source %s/bin/activate" % env.virtualenv + " && " + command, **kwargs)


def install_dependencies():
  if not exists("{0}/media/uploads".format(env.code_dir)):
    run("mkdir -p {0}/media/uploads".format(env.code_dir))
  ensure_virtualenv()
  if not exists("{0}/lib/libz.so".format(env.virtualenv)):
    with cd("{0}/lib".format(env.virtualenv)):
      run("ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so")
      run("ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so")
      run("ln -s /usr/lib/x86_64-linux-gnu/libz.so")
  with virtualenv(env.virtualenv):
    with cd(env.code_dir):
      #run_venv("pip install -r requirements/prod.txt")
      run_venv("pip install -r requirements/dev.txt")

def ensure_virtualenv():
    if exists(env.virtualenv):
        return

    with cd(env.code_dir):
        run("virtualenv --no-site-packages --python=%s %s" %
            (PYTHON_BIN, env.virtualenv))
        run("echo %s > %s/lib/%s/site-packages/projectsource.pth" %
            (env.project_dir, env.virtualenv, PYTHON_BIN))


def ensure_src_dir():
    if not exists(env.code_dir):
        run("mkdir -p %s" % env.code_dir)
    with cd(env.code_dir):
        if not exists(posixpath.join(env.code_dir, '.git')):
            run('git clone %s .' % (env.code_repo))


def push_sources():
    """
    Push source code to server
    """
    ensure_src_dir()
    local('git push origin master')
    with cd(env.code_dir):
        run('git pull origin master')


@task
def run_tests():
    """ Runs the Django test suite as is.  """
    local("./manage.py test")


@task
def version():
    """ Show last commit to the deployed repo. """
    with cd(env.code_dir):
        run('git log -1')


@task
def uname():
    """ Prints information about the host. """
    run("uname -a")


@task
def webserver_stop():
    """
    Stop the webserver that is running the Django instance
    """
    run("service apache2 stop")


@task
def webserver_start():
    """
    Starts the webserver that is running the Django instance
    """
    run("service apache2 start")


@task
def webserver_restart():
    """
    Restarts the webserver that is running the Django instance
    """
    if DJANGO_SERVER_RESTART:
        with cd(env.code_dir):
            run("touch %s/wsgi.py" % env.project_dir)
    else:
        with settings(warn_only=True):
            webserver_stop()
        webserver_start()


def restart():
    """ Restart the wsgi process """
    with cd(env.code_dir):
        run("touch %s/DjangoApp/wsgi.py" % env.code_dir)


def build_static():
    assert env.static_root.strip() != '' and env.static_root.strip() != '/'
    with virtualenv(env.virtualenv):
        with cd(env.code_dir):
            run_venv("./manage.py collectstatic -v 0 --clear --noinput")

    run("chmod -R ugo+r %s" % env.static_root)

def build_bootstrap():
    run("cp /opt/www/DjangoApp/lib/bootstrap/img/* /opt/www/DjangoApp/DjangoApp/base/static/img/")
    run("cp /opt/www/DjangoApp/extras/fontawesome/font/* /opt/www/DjangoApp/DjangoApp/base/static/font/")
    run("recess --compile /opt/www/DjangoApp/DjangoApp/base/static/less/bootstrap.less > /opt/www/DjangoApp/DjangoApp/base/static/css/bootstrap.css")
    run("recess --compress /opt/www/DjangoApp/DjangoApp/base/static/less/bootstrap.less > /opt/www/DjangoApp/DjangoApp/base/static/css/bootstrap.min.css")
    run("recess --compile /opt/www/DjangoApp/DjangoApp/base/static/less/responsive.less > /opt/www/DjangoApp/DjangoApp/base/static/css/bootstrap-responsive.css")
    run("recess --compress /opt/www/DjangoApp/DjangoApp/base/static/less/responsive.less > /opt/www/DjangoApp/DjangoApp/base/static/css/bootstrap-responsive.min.css")
    run("cd /opt/www/DjangoApp/lib/bootstrap/ && cat js/bootstrap-transition.js js/bootstrap-alert.js js/bootstrap-button.js js/bootstrap-carousel.js js/bootstrap-collapse.js js/bootstrap-dropdown.js js/bootstrap-modal.js js/bootstrap-tooltip.js js/bootstrap-popover.js js/bootstrap-scrollspy.js js/bootstrap-tab.js js/bootstrap-typeahead.js js/bootstrap-affix.js > /opt/www/DjangoApp/DjangoApp/base/static/js/libs/bootstrap.js")
    run("uglifyjs -nc /opt/www/DjangoApp/DjangoApp/base/static/js/libs/bootstrap.js > /opt/www/DjangoApp/DjangoApp/base/static/js/libs/bootstrap.min.js")
    run("recess --compress /opt/www/DjangoApp/DjangoApp/base/static/less/aplication.less > /opt/www/DjangoApp/DjangoApp/base/static/css/aplication.min.css")
    run("recess --compile /opt/www/DjangoApp/DjangoApp/base/static/less/aplication.less > /opt/www/DjangoApp/DjangoApp/base/static/css/aplication.css")
    run("cp -u /opt/www/DjangoApp/extras/tinymce_setup.js /opt/www/DjangoApp/static/js/")
    run("cp -ur /opt/www/DjangoApp/extras/tinymce_language_pack/* /opt/www/DjangoApp/static/grappelli/tinymce/jscripts/tiny_mce/")
    #run("cp -u /opt/www/DjangoApp/extras/jquery-equal-heights/jQuery.equalHeights.js /opt/www/DjangoApp/DjangoApp/base/static/js/libs/")
    #run("cp -u /opt/www/DjangoApp/extras/jquery-pixel-em-converter/pxem.jQuery.js /opt/www/DjangoApp/DjangoApp/base/static/js/libs/")

def build_trans():
  with virtualenv(env.virtualenv):
    with cd(env.code_dir):
      run_venv("./manage.py compilemessages")

@task
def first_deployment_mode():
    """
    Use before first deployment to switch on fake south migrations.
    """
    env.initial_deploy = True


@task
def update_database(app=None):
    """
    Update the database (run the migrations)
    Usage: fab update_database:app_name
    """
    with virtualenv(env.virtualenv):
        with cd(env.code_dir):
            if getattr(env, 'initial_deploy', False):
                run_venv("./manage.py syncdb --all")
                run_venv("./manage.py migrate --fake --noinput")
            else:
                run_venv("./manage.py syncdb --noinput")
                if app:
                    run_venv("./manage.py migrate %s --noinput" % app)
                else:
                    run_venv("./manage.py migrate --noinput")


@task
def sshagent_run(cmd):
    """
    Helper function.
    Runs a command with SSH agent forwarding enabled.

    Note:: Fabric (and paramiko) can't forward your SSH agent.
    This helper uses your system's ssh to do so.
    """
    # Handle context manager modifications
    wrapped_cmd = _prefix_commands(_prefix_env_vars(cmd), 'remote')
    try:
        host, port = env.host_string.split(':')
        return local(
            "ssh -p %s -A %s@%s '%s'" % (port, env.user, host, wrapped_cmd)
        )
    except ValueError:
        return local(
            "ssh -A %s@%s '%s'" % (env.user, env.host_string, wrapped_cmd)
        )


@task
def deploy():
    """
    Deploy the project.
    """
    #with settings(warn_only=True):
    #    webserver_stop()
    #push_sources()
    install_dependencies()
    update_database()
    #build_trans()
    build_static()
    build_bootstrap()
    build_trans()
   # webserver_start()

@task
def bootstrap():
    build_bootstrap()
    build_static()

@task
def runs():
  with virtualenv(env.virtualenv):
    with cd(env.code_dir):
      #run_venv("./manage.py customdashboard")
      run_venv("./manage.py runserver {0}".format(env.dev_server))

@task
def trans():
  with virtualenv(env.virtualenv):
    with cd(env.code_dir):
      run_venv("./manage.py makemessages -l {0}".format(env.sup_lang))
      run_venv("./manage.py makemessages -d djangojs -l {0}".format(env.sup_lang))
  build_trans()

@task
def m(a1='help'):
  """
  Run manager command Exemple fab m:help
  """
  with virtualenv(env.virtualenv):
    with cd(env.code_dir):
      run_venv("./manage.py {0}".format(a1))

