#!/usr/bin/env python
import os
import codecs
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

if os.path.exists("README.mdown"):
    long_description = codecs.open('README.mdown', "r", "utf-8").read()
else:
    long_description = "See http://github.com/nvie/vim_bridge/tree/master"

setup(
    name="vim_bridge",
    version=0.1,
    description="Vim-Python bridge for Vim scripts, to directly call into Python functions.",
    author="Vincent Driessen",
    author_email="vincent@datafox.nl",
    url="http://github.com/nvie/vim_bridge",
    platforms=["any"],
    license="BSD",
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    classifiers=[
        # Picked from
        #    http://pypi.python.org/pypi?:action=list_classifiers
        #"Development Status :: 1 - Planning",
        #"Development Status :: 2 - Pre-Alpha",
        #"Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        #"Development Status :: 6 - Mature",
        #"Development Status :: 7 - Inactive",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Topic :: Text Editors",
    ],
    long_description=long_description,
)
