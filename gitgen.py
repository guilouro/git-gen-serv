#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, sys

# dir_atual = os.path.abspath('.')
# Diretório principal do projeto 
dir_project = os.sys.argv[1]
# Diretório do git bare
dir_git_bare = 'git'
# Diretório do repositorio do projeto
dir_repositorio = dir_project

#paths
path_proj = os.path.abspath('%s' %(dir_project))
path_gitbare = os.path.abspath('%s/%s' %(dir_project, dir_git_bare))
path_hooks = os.path.abspath('%s/hooks' %(path_gitbare))
path_repo = os.path.abspath('%s/%s' %(dir_project, dir_project))

d = "*"*40
print "\n\n\n"


# Tenta criar os diretorios
print "Diretórios do projeto:"
repook = os.makedirs("%s/%s" %(dir_project, dir_repositorio))
bareok = os.makedirs("%s/%s" %(dir_project, dir_git_bare))
if not repook and not bareok:
	print "\n/%s\n-> /%s \n-> /%s \n\nDiretórios criados com sucesso\n\n%s\n" %(dir_project, dir_git_bare, dir_repositorio, d)
else:
	print "Erro ao criar diretórios"

# Tenta criar o git --bare init dentro da pasta git do projeto
if os.system("cd %s || exit && git --bare init" %(path_gitbare)):
	print "Erro ao criar git bare"

# Inicia o git no repositorio e add remote origin
if not os.system("cd %s || exit && git init && git remote add origin %s" %(path_repo, path_gitbare) ):
	pass
else:
	print "Erro ao criar git e adicionar remote origin"

# criar post-receive
postreceive = "\
#!/bin/bash\n\
cd ../%s/ || exit\n\
unset GIT_DIR\n\
git pull origin master\n\
exec git-update-server-info" %dir_repositorio

os.chdir(path_hooks)
with open('post-receive', 'w') as f:
	f.write(postreceive)

if sys.platform == "linux2":
	os.chmod('post-receive', 0755)

print "Repositórios criados com sucesso"
print "\n\n\n"

