from collections import namedtuple

from .cli import cli

__version__ = "1.0.3"
VersionInfo = namedtuple("VersionInfo", "major minor macro release")

version_info = VersionInfo(1, 0, 3, "stable")
