#
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


import time
import sys
import argparse

import keyring
from keyring.backends.OS_X import Keyring

from UIUCEnterpriseBot import UIUCEnterpriseBot

RETURN_STATUS_SUCCESS = 0
RETURN_STATUS_FAILURE = 1


def setup_arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('major', metavar='major',
                        type=str, help='Course major')
    parser.add_argument('course', metavar='course',
                        type=str, help='Course number')
    parser.add_argument('crn', metavar='crn',
                        type=str, help='Course registration number')
    parser.add_argument('term', type=str,
                        help='Term number (ex. 120158 for FA15)')
    parser.add_argument('username', help='UIUC Enterprise username')
    parser.add_argument('--password', dest='password', type=str,
                        help='UIUC Enterprise password', default='')
    parser.add_argument('--add-on-release', dest='add_on_release',
                        const=True, default=False, action='store_const',
                        help='Attempt to add course when it becomes available')
    # the service name is used by the Mac OSX keychain services api
    # for more info, read:
    # https://developer.apple.com/library/mac/documentation/Security/Conceptual/keychainServConcepts/03tasks/tasks.html#//apple_ref/doc/uid/TP30000897-CH205-TP9
    parser.add_argument('--service-name', type=str, dest='service_name',
                        default='', help='For internal use.')
    return parser


def get_password(username, service_name):
    keyring.set_keyring(Keyring())
    password = keyring.get_password(service_name, username)
    return password


def poll(username, password, term, major, course, crn, add_on_release=False):
    ss = UIUCEnterpriseBot()
    ss.term = term
    ss.login(username=username, password=password)

    while True:
        try:
            classes = ss.get_classes(major=major, course=course)

            print(crn + ": " + str(classes[crn]))

            if classes[crn]:
                if add_on_release:
                    ss.add_course(crn)
                sys.exit(RETURN_STATUS_SUCCESS)

        except KeyError:
            print(sys.stderr,
                  "Error: poll failed due to an unexpected error. Exiting...")
            sys.exit(RETURN_STATUS_FAILURE)

        time.sleep(5)


def main():
    parser = setup_arguments_parser()
    args = parser.parse_args()

    username = args.username

    if args.service_name != '':
        password = get_password(username, args.service_name)
    elif args.password == '':
        password = ''
    else:
        password = args.password

    if password == '':
        print(sys.stderr, 'Error: unable to resolve passoword. Exiting...')
        sys.exit(RETURN_STATUS_FAILURE)

    poll(username, password, args.term, args.major, args.course,
         args.crn, args.add_on_release)

