#!/usr/bin/env python
print('Content-type: text/html\r\n\r')
import json, urlparse, sys, os, git, cgitb, cgi, subprocess
from git import Repo
from subprocess import Popen, PIPE
from git import Git
dir_path = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILEPATH = dir_path+'/gitPull.conf.json'
config = None
quiet = False
daemon = False

configString = open(CONFIG_FILEPATH).read()
config = json.loads(configString)

for repository in config['repositories']:
    repo = Repo.init(repository['path'])
    Git(repository['path']).pull(repository['url'])