#!/usr/bin/python3
# encoding: utf-8

from user import User, Admin, Privileges

usuario01 = Admin("kurt", "cobain", "kurt.cobain", "kurt@nirvana.com", "nevermind")
usuario01.privileges.show_privileges()

