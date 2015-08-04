#!/usr/bin/env python

# UIUCEnterpriseBot : a webbot that interacts with the
# University of Illinois course registration system
# Copyright (C) 2015  Rajiv Nair
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r', 'utf-8') as f:
    long_description = f.read()

setup(
    name='UIUCEnterpriseBot',
    version='0.3.0',
    description='Webbot for interacting with Univ. of Illinois course '
                'registration system.',
    long_description=long_description,
    url='https://github.com/rsnair2/UIUCEnterpriseBot',
    author='Rajiv Nair',
    author_email='rsnair2@me.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='uiuc webbot automation',
    packages=['UIUCEnterpriseBot'],
    install_requires=['requests',
                      'keyring'],
    entry_points={
        'console_scripts': [
            'uiuc-enterprise-bot=UIUCEnterpriseBot.main:main',
        ],
    },
)
