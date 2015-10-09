__author__ = 'longqi'
import subprocess

subprocess.Popen('echo "hello world!"', shell=True, executable='/usr/bin/zsh', )


def print_string(string):
    print(subprocess.Popen('echo "%s"' % string, shell=True, ))


print_string("dd")
subprocess.call(['ls', '-sh', '/boot'])

print('_______________________________')
import sys

process1 = subprocess.Popen('ls -sh /home2', shell=True, stderr=subprocess.PIPE)
process1.communicate()
sys.stderr.write('Message to stderr, hi zhang\n')
