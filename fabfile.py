"""
Starter fabfile for deploying the kvazar project.

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
env.home = '/opt/www/kvazar/kvazar-app'
env.app_name = 'kvazar'
env.dev_server = '192.168.125.94:8000'
env.deploy_revision = 'kvazar'
env.requirements_dev = 'requirements/dev.txt'
env.requirements_prod = 'requirements/prod.txt'
env.local_settings_file = 'local.py'
# Strategy developer or production
env.strategy = 'developer'
env.sup_lang = 'ru'
env.hosts = ['jbo@app03.089.com.ua']
env.code_dir = "{0}/current".format(env.home)
env.shared_dir = "{0}/shared".format(env.home)
env.project_dir = "{0}/current".format(env.home)
env.app_dir = "{0}/current/{1}".format(env.home, env.app_name)
env.public_root = "{0}/current/public".format(env.home)
env.static_root = "{0}/current/public/static/".format(env.home)
env.media_root = "{0}/current/public/media".format(env.home)
env.virtualenv = "{0}/shared/env".format(env.home)
env.code_repo = 'git@git.089.com.ua:kvazar-app.git'
env.django_settings_module = 'kvazar.settings'

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
  if not exists(env.public_root):
    run("mkdir -p {0}".format(env.public_root))
  if not exists("{0}/media/uploads".format(env.shared_dir)):
    run("mkdir -p {0}/media/uploads".format(env.shared_dir))
  if not exists(env.media_root):
    run("ln -s {0}/media {1}".format(env.shared_dir, env.media_root))
  if not exists(env.static_root):
    run("mkdir -p {0}".format(env.static_root))
  if not exists("{0}/config".format(env.shared_dir)):
    run("mkdir -p {0}/config".format(env.shared_dir))
  if not exists("{0}/log".format(env.shared_dir)):
    run("mkdir -p {0}/log".format(env.shared_dir))
  if not exists("{0}/log".format(env.project_dir)):
    run("ln -s {0}/log {1}/log".format(env.shared_dir, env.project_dir))
  if not exists("{0}/pids".format(env.shared_dir)):
    run("mkdir -p {0}/pids".format(env.shared_dir))
  if not exists("{0}/system".format(env.shared_dir)):
    run("mkdir -p {0}/system".format(env.shared_dir))
  if not exists("{0}/system".format(env.public_root)):
    run("ln -s {0}/system {1}/system".format(env.shared_dir, env.public_root))
  ensure_virtualenv()
  if not exists("{0}/lib/libz.so".format(env.virtualenv)):
    with cd("{0}/lib".format(env.virtualenv)):
      run("ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so")
      run("ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so")
      run("ln -s /usr/lib/x86_64-linux-gnu/libz.so")
  with virtualenv(env.virtualenv):
    with cd(env.code_dir):
      #run_venv("pip install -r requirements/prod.txt")
      if env.strategy == 'developer':
        run_venv("pip install -r {0}".format(env.requirements_dev))
      else:
        run_venv("pip install -r {0}".format(env.requirements_prod))

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
    run("touch %s/kvazar/wsgi.py" % env.code_dir)


def build_static():
  assert env.static_root.strip() != '' and env.static_root.strip() != '/'
  with virtualenv(env.virtualenv):
    with cd(env.code_dir):
      run_venv("./manage.py collectstatic -v 0 --clear --noinput")
      run("chmod -R ugo+r {0}".format(env.static_root))

def build_bootstrap():
  run("cp {0}/lib/bootstrap/img/* {1}/base/static/img/".format(env.code_dir, env.app_dir))
  run("cp {0}/extras/fontawesome/font/* {1}/base/static/font/".format(env.code_dir, env.app_dir))
  run("recess --compile {0}/base/static/less/bootstrap.less > {0}/base/static/css/bootstrap.css".format(env.app_dir))
  run("recess --compress {0}/base/static/less/bootstrap.less > {0}/base/static/css/bootstrap.min.css".format(env.app_dir))
  run("recess --compile {0}/base/static/less/responsive.less > {0}/base/static/css/bootstrap-responsive.css".format(env.app_dir))
  run("recess --compress {0}/base/static/less/responsive.less > {0}/base/static/css/bootstrap-responsive.min.css".format(env.app_dir))
  run("cd {0}/lib/bootstrap/ && cat js/bootstrap-transition.js js/bootstrap-alert.js js/bootstrap-button.js js/bootstrap-carousel.js js/bootstrap-collapse.js js/bootstrap-dropdown.js js/bootstrap-modal.js js/bootstrap-tooltip.js js/bootstrap-popover.js js/bootstrap-scrollspy.js js/bootstrap-tab.js js/bootstrap-typeahead.js js/bootstrap-affix.js > {0}/base/static/js/libs/bootstrap.js".format(env.app_dir))
  run("uglifyjs -nc {0}/base/static/js/libs/bootstrap.js > {0}/base/static/js/libs/bootstrap.min.js".format(env.app_dir))
  run("recess --compress {0}/base/static/less/aplication.less > {0}/base/static/css/aplication.min.css".format(env.app_dir))
  run("recess --compile {0}/base/static/less/aplication.less > {0}/base/static/css/aplication.css".format(env.app_dir))
  run("cp -u {0}/extras/tinymce_setup.js {1}static/js/".format(env.code_dir, env.static_root))
  run("cp -ur {0}/extras/tinymce_language_pack/* {1}static/grappelli/tinymce/jscripts/tiny_mce/".format(env.code_dir, env.app_dir))
  #run("cp -u {0}/extras/jquery-equal-heights/jQuery.equalHeights.js {0}/base/static/js/libs/".format(env.code_dir, env.app_dir))
  #run("cp -u {0}/extras/jquery-pixel-em-converter/pxem.jQuery.js {0}/base/static/js/libs/".format(env.code_dir, env.app_dir))

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
    return local("ssh -p %s -A %s@%s '%s'" % (port, env.user, host, wrapped_cmd))
  except ValueError:
    return local("ssh -A %s@%s '%s'" % (env.user, env.host_string, wrapped_cmd))


@task
def deploy():
  """
  Deploy the project.
  """
  #with settings(warn_only=True):
  #    webserver_stop()
  #push_sources()
  install_dependencies()
  if exists("{0}/{1}".format(env.shared_dir, env.local_settings_file)):
    if not exists("{0}/{1}".format(env.app_dir, env.local_settings_file)):
      run("ln -s {0}/{1}".format(env.app_dir, env.local_settings_file))
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

