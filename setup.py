"""
    UIUC Enterprise Webbot: a webbot to monitor the availability of a class
    through the UIUC Enterprise system.

    This file is part of UIUC Enterprise Webbot.

    UIUC Enterprise Webbot is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    UIUC Enterprise Webbot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with UIUC Enterprise Webbot. If not, see
    <http://www.gnu.org/licenses/>.

    author: Rajiv Nair (rsnair.com)
"""

from setuptools import setup, find_packages


setup(
    name='UIUCEnterpriseBot',
    version='0.2',

    description='A webbot for interacting with the Univ. of Illinois '
                'course registration website.',
    long_description='Long Desc',

    # The project's main homepage.
    url='https://github.com/rsnair2/UIUCEnterpriseBot',

    # Author details
    author='Rajiv Nair',
    author_email='rsnair2@me.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Education',
        'Topic :: Internet :: WWW/HTTP',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='uiuc webbot automation',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['requests',
                      'keyring'],

    entry_points={
        'console_scripts': [
            'webby=src.main:main',
        ],
    },
)
