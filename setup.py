#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

import cm_sdk 

PACKAGES = [
    'cm_sdk'
]

def is_requirement(line):
    """
    Return True if the requirement line is a package requirement;
    that is, it is not blank, a comment, or editable.
    """
    # Remove whitespace at the start/end of the line
    line = line.strip()

    # Skip blank lines, comments, and editable installs
    return not (
        line == '' or
        line.startswith('-r') or
        line.startswith('#') or
        line.startswith('-e') or
        line.startswith('git+')
    )

def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns a list of requirement strings.
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.strip() for line in open(path).readlines()
            if is_requirement(line)
        )
    return list(requirements)

setup_options = dict(
    name='edx-cloudmanager-sdk',
    version='0.1',
    description='Simple SDK for interactiong with the Mongo CloudManager REST API',
    url='https://github.com/edx-ops/edx-clhttps://github.com/edx-ops/edx-cloudmanager-sdk',
    packages=find_packages('.', exclude=['tests*']),
    package_dir={'cm_sdk': 'cm_sdk'},
    install_requires=load_requirements('requirements/base.txt'),
    license="Apache2",
    classifiers=(
        'Programming Language :: Python :: 2.7',
    ),
)

setup(**setup_options)
