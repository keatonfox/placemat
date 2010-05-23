#!/usr/bin/python2.4
#
# Copyright 2010 Google Inc. All Rights Reserved.

"""Placemat sample program.

API features used:
    SHOW TABLES
"""


import sys


from placemat import ftclient


def main():
    if (len(sys.argv) > 1):
      auth_token = ftclient.GetAuthToken(sys.argv)
    else:
      auth_token = ftclient.GetAuthToken()
  
    ft = ftclient.FTClient(auth_token)
  
    print ft.runGetQuery('SHOW TABLES')


if __name__ == '__main__':
    main()
