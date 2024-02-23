#!/usr/bin/env python
# coding: utf-8

# Copyright 2017 TWO SIGMA OPEN SOURCE, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from setuptools import setup, find_packages

from setupbase import (
    get_version,
)

setup_args = dict(
    name='beakerx_base',
    description='BeakerX: Beaker Base Extensions for Jupyter Notebook',
    long_description='BeakerX: Beaker Base Extensions for Jupyter Notebook',
    version=get_version(os.path.join('beakerx_base', '_version.py')),
    author='Two Sigma Open Source, LLC',
    author_email='beakerx-feedback@twosigma.com',
    url='http://beakerx.com',
    keywords=[
        'ipython',
        'jupyter',
        'widgets'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3',
    install_requires=[
        'ipywidgets>=7.5.1,<9',
        'pandas',
        'pytz'
    ],
    extras_require={
        'test': [
            'pytest'
        ]
    },
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
)

if __name__ == '__main__':
    setup(**setup_args)
