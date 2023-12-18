#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
web_static folder of my AirBnB Clone repo, using the function do_pack. """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generates a .tgz archive from the contents of the
    web_static directory. """
    # Create the folder versions if not exists
    local("mkdir -p versions")
    # Create the file with date format
    date = datetime.now()
    date_format = date.strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date_format)
    # Compress file
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None
