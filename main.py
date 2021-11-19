#!python3

import os, hashlib
from includes import *

if __name__ == '__main__':

    manifest = ''
    files = os.listdir(basedir)
    for file in files:
        with open(f'{basedir}/{file}', 'rb') as filedata:
            hash = hashlib.sha1(filedata.read()).hexdigest()
            manifest += f'SHA1({file})= {hash}\n'
    print (manifest)