#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
from common import (__VERSION__, __AUTHOR__, __AUTHOR_EMAIL__)

setup(
    name="common-tags",
    packages=find_packages(exclude=["*.demo"]),
    version=__VERSION__,
    url="https://github.com/agusmakmun/common-tags/",
    download_url="https://github.com/agusmakmun/common-tags/tarball/v{}".format(__VERSION__),
    description="Common templatetags provides for Django",
    long_description=open("README.rst").read(),
    license="MIT",
    author=__AUTHOR__,
    author_email=__AUTHOR_EMAIL__,
    keywords=["django common templatetags", "django templatetags"],
    zip_safe=False,
    include_package_data=True,
    install_requires=["Django>=1.10.1"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Framework :: Django",
    ]
)
