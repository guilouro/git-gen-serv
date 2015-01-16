#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import os

slug = raw_input("Slug (Ex: project-name): ")
group = raw_input("Bitbucket Group: ")
user = raw_input("Bitbucket user: ")
passwd = getpass.getpass("Bitbucket password: ")


command = "curl -X POST -u %s:%s -v -H \
\"Content-Type: application/json\" \
https://api.bitbucket.org/2.0/repositories/%s/%s \
-d '{\"scm\": \"git\", \"is_private\": \"true\",\
 \"fork_policy\": \"no_public_forks\" }'"


os.system(command % (user, passwd, group, slug))
