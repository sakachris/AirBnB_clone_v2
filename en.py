#!/usr/bin/python3
from os import getenv
print("Host name is: {}".format(getenv('HBNB_MYSQL_HOST')))
print("Environment is: {}".format(getenv('HBNB_ENV')))
print("Password is: {}".format(getenv('HBNB_MYSQL_PWD')))
print("User is: {}".format(getenv('HBNB_MYSQL_USER')))
print("Database is: {}".format(getenv('HBNB_MYSQL_DB')))
