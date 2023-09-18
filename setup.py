from distutils.core import setup
from re import search

_version = ""
with open("version.txt", "r") as verfile:
    contents = verfile.read()
    matchString = r"version=(\d*\.\d*\.\d*)"
    _version = search(matchString, contents).group(1)

setup(
    name="Duck Garden",
    version=_version,
    description="A simple app for ducks.",
    author="Collin Matz",
    author_email="collin.matz.a@gmail.com",
    packages=[
        "PyQt6"
    ]
)