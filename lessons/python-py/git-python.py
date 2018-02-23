# from git import *


import git
import socket, os, sys

repo = git.Repo("/home/tokonbekov/src/mesa_jenkins")


commit = repo.commit()
# print(commit)

message = commit.message
print(message.splitlines()[0])

as = os.lis

# sha = repo.git.rev_parse(commit, short=True)
# print(sha)

# print( socket.gethostname() )



# import subprocess, os, sys
# sudoPassword = 'Z'
# command = 'ifconfig | grep inet'
# p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))