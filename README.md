
# DjangoApp Project #

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

mkdir -p /opt/www/DjangoApp/DjangoApp-app/releases/
mkdir -p /opt/www/DjangoApp/DjangoApp-app/shared/
cd /opt/www/DjangoApp/DjangoApp-app/releases/
git clone git@git.089.com.ua:DjangoApp-app.git dev
git branch --track -b DjangoApp origin/DjangoApp
ln -s /opt/www/DjangoApp/DjangoApp-app/releases/dev /opt/www/DjangoApp/DjangoApp-app/current
cd /opt/www/DjangoApp/DjangoApp-app/current
git submodule update --init



License
-------
This software is licensed under the [New BSD License][BSD]. For more
information, read the file ``LICENSE``.

[BSD]: http://opensource.org/licenses/BSD-3-Clause
