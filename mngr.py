# libraries
from hashlib import sha256
from getpass import getpass

# add flag to display input
import argparse
parser = argparse.ArgumentParser(description="This tool hashes a short password. The user is encouraged to use the hash as the target password externally. Utilises wl-clipboard.")
parser.add_argument('-s', '--show', action='store_true', help='show input for password')
parser.add_argument('-p', '--password', help='passthrough and process input immediately')

args = parser.parse_args()

if args.password:
    pwd = args.password
elif args.show:
    pwd = input('Enter password: ')
else:
    pwd = getpass('Input password: ')

output = sha256(pwd.encode('utf-8')).hexdigest()

# copy output to clipboard
import subprocess
subprocess.run('wl-copy', text=True, input=output)

# print output
print('Copied to clipboard: ' + output)
