"""
This is setup.py
"""

from setuptools import setup

APP = ["ping_status.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": False,  # Changed to False
    "plist": {
        "LSUIElement": True,
        "CFBundleName": "PingStatus",
        "CFBundleDisplayName": "Ping Status",
        "CFBundleGetInfoString": "Ping Status Monitor",
        "CFBundleIdentifier": "com.pingstatus.app",
        "CFBundleVersion": "0.1.0",
        "CFBundleShortVersionString": "0.1.0",
    },
    "packages": ["rumps"],
    "includes": ["subprocess", "threading", "time"],  # Added explicit includes
}

setup(
    app=APP,
    name="PingStatus",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
