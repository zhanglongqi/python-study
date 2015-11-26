__author__ = 'longqi'
import subprocess

subprocess.Popen('echo "hello world!"', shell=True, executable='/bin/zsh', )


def print_string(string):
    print(subprocess.Popen('echo "%s"' % string, shell=True, ))


subprocess.call(['ls', '-sh', '/boot'])

print('_______________________________')
import sys

process1 = subprocess.Popen('ls -sh /home2', shell=True, stderr=subprocess.PIPE)
process1.communicate()
sys.stderr.write('Message to stderr, hi zhang\n')

print('2_______________________________')
process2 = subprocess.Popen('who', shell=True, stdout=subprocess.PIPE)

out, err = process2.communicate()
print(out, err)

print('3_______________________________')

if any(s.startswith(b'longqi ') for s in out.split(b'\n')):
    print('LongQi is here')
else:
    print('He is not here, Find him somewhrere else')
