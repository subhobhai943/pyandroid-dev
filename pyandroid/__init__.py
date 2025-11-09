"""PyAndroid - A Python library for Android application development.

This library provides a Pythonic interface for building Android applications
using cross-platform development techniques.
"""

__version__ = "1.0.0"
__author__ = "Subhobhai"
__email__ = "sarkarsubhadip604@gmail.com"
__license__ = "MIT"

from .core import AndroidApp, Activity, Intent
from .ui import View, Layout, Widget
from .utils import Logger, FileManager, NetworkManager

__all__ = [
    'AndroidApp',
    'Activity', 
    'Intent',
    'View',
    'Layout',
    'Widget',
    'Logger',
    'FileManager',
    'NetworkManager'
]
