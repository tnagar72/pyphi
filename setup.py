#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# setup.py

# Use a consistent encoding
from codecs import open

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

about = {}
with open("./pyphi/__about__.py", encoding="utf-8") as f:
    exec(f.read(), about)

install_requires = [
    "decorator >=4.0.0",
    "joblib >=0.8.0",
    "numpy >=1.11.0",
    "ordered-set >= 4.0.2",
    "psutil >=2.1.1",
    "pyemd >=0.3.0",
    "pymongo >=2.7.1",
    "pyyaml >=3.13",
    "ray[default] >=1.9.2",
    "redis >=2.10.5",
    "scipy >=0.13.3",
    "tblib >=1.3.2",
    "toolz >=0.9.0",
    "tqdm >=4.20.0",
]

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    license=about["__license__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    keywords=(
        "neuroscience causality causal-modeling causation "
        "integrated-information-theory iit integrated-information "
        "modeling"
    ),
    packages=find_packages(exclude=["docs", "test"]),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
    project_urls={
        "Bug Reports": "https://github.com/wmayner/pyphi/issues",
        "Documentation": "https://pyphi.readthedocs.io",
        "IIT Website": "http://integratedinformationtheory.org/",
        "Online Interface": "http://integratedinformationtheory.org/calculate.html",
        "User Group": "https://groups.google.com/forum/#!forum/pyphi-users",
    },
)
