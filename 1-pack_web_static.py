#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates .tgz archive
    """
    try:
        local("mkdir -p versions")

        now = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "web_static_{}.tgz".format(now)

        local(f"tar -cvzf versions/{name} web_static/")

        return f"versions/{name}"
    except Exception:
        return None
