#!/usr/bin/python3
""" Script that compress files and put to the server"""

from fabric.api import *
import datetime
import os


env.hosts = ['35.231.155.83', '54.161.4.135']


def do_deploy(archive_path):
    """
    distributes an archive to your web servers,
    using the function do_deploy:

    Args:
        archive_path ([string]): path to a file
    """
    if os.path.exists(archive_path) is False:
        return(False)
    else:
        try:
            # Upload files 📄
            upload = put('{}'.format(archive_path), '/tmp/')
            file = archive_path.split('/')[-1]
            folder = file.split('.')[0]
            # Descompressing files ✅
            run('mkdir -p /data/web_static/releases/{}/'.format(folder))
            # -C Move the content to the folder
            run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/\
'.format(file, folder))
            # delete the file from web server
            run('rm -rf /tmp/{}'.format(file))
            # organize the files
            run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/\
'.format(folder, folder))
            # delete the symbolic link
            run('rm -rf /data/web_static/current')
            # Create new symbolic link
            run('ln -s /data/web_static/releases/{}/ /data/web_static/current\
'.format(folder))
        except Exception as error:
            pass
            return(False)
