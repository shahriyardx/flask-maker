from collections import namedtuple

from .cli import cli

__version__ = "2.0.1"
VersionInfo = namedtuple("VersionInfo", "major minor macro release")

version_info = VersionInfo(2, 0, 1, "stable")
