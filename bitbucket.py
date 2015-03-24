#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import os


class Bitbucket:

    def __init__(self):
        """
        Created repositories in bitbucket
        """
        self.slug = raw_input("Slug (Ex: project-name): ")
        self.group = raw_input("Bitbucket Group: ")
        self.user = raw_input("Bitbucket user: ")
        self.passwd = getpass.getpass("Bitbucket password: ")

        command = "curl -X POST -u %s:%s -v -H \
        \"Content-Type: application/json\" \
        https://api.bitbucket.org/2.0/repositories/%s/%s \
        -d '{\"scm\": \"git\", \"is_private\": \"true\",\
         \"fork_policy\": \"no_public_forks\" }'"

        os.system(command % (self.user, self.passwd, self.group, self.slug))

    def get_url(self):
        return "git@bitbucket.org:%s/%s.git" % (self.group, self.slug)


if __name__ == '__main__':
    bitbucket = Bitbucket()
    remote = raw_input("\nYour remote: ")
    os.system("git remote add %s %s" % (remote, bitbucket.get_url()))
    # print bitbucket.get_url()
