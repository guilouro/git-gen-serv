#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import getpass

# Diretório principal do projeto
dir_project = os.sys.argv[1]

postreceive = "\
#!/bin/bash\n\
cd ../dev/ || exit\n\
unset GIT_DIR\n\
git reset --hard HEAD~1\n\
git pull origin master\n\
exec git-update-server-info"

print "\n\n"

git = '%s.git' % (dir_project[0].upper() + dir_project[1:])

# created paths
print "Created /dev/"
if not os.makedirs('dev'):
    print " --- success"

print "Created /%s/" % git
if not os.makedirs(git):
    print " --- success"

paths = {
    'home': os.path.abspath('.'),
    'dev': os.path.abspath('dev'),
    'git': os.path.abspath(git),
}

print "\n"

os.chdir(paths['git'])
paths['hooks'] = os.path.abspath('hooks')

os.system("git init --bare")
os.chdir(paths['hooks'])

with open('post-receive', 'w') as f:
    f.write(postreceive)

os.chdir(paths['dev'])
os.system('git init')

print '\nAdded remote origin in /%s/' % git
os.system('git remote add origin ../%s/' % git)
print " --- success"

print "\n\n"
