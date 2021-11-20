#!python3

import os, hashlib, tarfile
from includes import *

# Build a OVA manifest file.  Calculates SHA1 hash for all files in directory 'basedir'
# and writes a file name .mf that matches the ISO filename into basedir
def writemanifest(basedir):
    manifest = ''
    files = os.listdir(basedir)
    for file in files:
        if file[0] != '.':
            with open(f'{basedir}/{file}', 'rb') as filedata:
                hash = hashlib.sha1(filedata.read()).hexdigest()
                manifest += f'SHA1({file})= {hash}\n'
                if '.iso' in file:
                    filename = file[0:len(file)-4]
    manfile = open(f'{basedir}/{filename}.mf','w')
    manfile.write(manifest)
    return(filename)

def tarova(basedir, filename):

    outfile = tarfile.open(f'{basedir}/{filename}.ova', 'w')
    files = os.listdir(basedir)
    for file in files:
        if file[0] != '.':
            outfile.add(f'{basedir}/{file}', arcname=f'{file}')
    outfile.close()

if __name__ == '__main__':

    filename = writemanifest(basedir)
    tarova(basedir, filename)