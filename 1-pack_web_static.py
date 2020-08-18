#!/usr/bin/python3
""" Script that compress files and put to the server"""

from fabric.api import local
import datetime


def do_pack():
    """ Compress files """

    date = datetime.datetime.now()
    path = 'versions/web_static_{}{}{}{}{}{}.tgz web_static\
'.format(date.year, date.month, date.day, date.hour,
         date.minute, date.second)
    local("mkdir -p versions")
    sucess = local('tar -cvzf {} web_static'.format(path), capture=True)
    if sucess.succeeded:
        print(path)
    else:
        print('None')
