
# kvazar Project #

## About ##

Describe your project here.

## Prerequisites ##

- Python >= 2.5
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)
-

    pip install -U django-fab-deploy
    pip install -U jinja2
    pip install -U "fabric >= 1.4"
    aptitude purge python-imaging
    aptitude install gettext libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
    ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
    ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
    ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
    pip install -U PIL
-

## Installation ##

scp ~/.ssh/id_dsa.pub jbo@git.089.com.ua:/home/jbo/gitolite-admin/keydir/${USERNAME}.pub
ssh-copy-id -i ~/.ssh/id_dsa.pub kvazar@app03.089.com.ua

на сервере с GIT
git add .
git ci -am "Added new user kvazar"
git pull
git push

mkdir -p /opt/www/kvazar/kvazar-app/releases/
mkdir -p /opt/www/kvazar/kvazar-app/shared/
cd /opt/www/kvazar/kvazar-app/releases/
git clone git@git.089.com.ua:kvazar-app.git dev
git branch --track -b kvazar origin/kvazar
ln -s /opt/www/kvazar/kvazar-app/releases/dev /opt/www/kvazar/kvazar-app/current
cd /opt/www/kvazar/kvazar-app/current
git submodule update --init

запускаем
cp /opt/www/kvazar/kvazar-app/current/kvazar/settings/local-dist.py /opt/www/kvazar/kvazar-app/shared/local.py
cd ~/kvazar-app/current
fab deploy


License
-------
This software is licensed under the [New BSD License][BSD]. For more
information, read the file ``LICENSE``.

[BSD]: http://opensource.org/licenses/BSD-3-Clause
