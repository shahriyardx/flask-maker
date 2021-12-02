from collections import namedtuple

from .cli import cli

__version__ = "3.0.0"
VersionInfo = namedtuple("VersionInfo", "major minor macro release")

version_info = VersionInfo(3, 0, 0, "stable")
