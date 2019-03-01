# Copyright 2018 The crowdcompute:crowdengine Authors
# This file is part of the crowdcompute:crowdengine library.
#
# The crowdcompute:crowdengine library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# The crowdcompute:crowdengine library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with the crowdcompute:crowdengine library. If not, see <http://www.gnu.org/licenses/>.

import os
from setuptools import setup, find_packages

THISDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(THISDIR)

VERSION = open("version.txt").readline().strip()
HOMEPAGE = "https://github.com/crowdcompute/python-jsonrpc"
DOWNLOAD_BASEURL = "https://github.com/crowdcompute/python-jsonrpc/raw/master/dist/"
DOWNLOAD_URL = DOWNLOAD_BASEURL + "python-jsonrpc-%s.tar.gz" % VERSION

setup(
    name="py-crowdcompute",
    version=VERSION,
    author="Andreas Lymbouras",
    author_email="ant.lymp@gmail.com",
    description="Python SDK for crowdcompute",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url=HOMEPAGE,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [""],
)