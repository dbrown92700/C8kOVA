#!python3

import os, hashlib, tarfile
from includes import *

# Build a OVA manifest file.  Calculates SHA1 hash for all files in directory 'ovadir'
# and writes a file name .mf that matches the ISO filename into ovadir
def writemanifest(ovadir):
    manifest = ''
    files = os.listdir(f'{ovadir}')
    for file in files:
        if file[0] != '.':
            with open(f'{ovadir}/{file}', 'rb') as filedata:
                hash = hashlib.sha1(filedata.read()).hexdigest()
                manifest += f'SHA1({file})= {hash}\n'
                if '.iso' in file:
                    filename = file[0:len(file)-4]
    manfile = open(f'{ovadir}/{filename}.mf', 'w')
    manfile.write(manifest)

# Create OVA file with filename using files in outdir
def tarova(ovadir, outdir, filename):

    outfile = tarfile.open(f'{outdir}/{filename}.ova', 'w')
    files = os.listdir(ovadir)
    for file in files:
        if file[0] != '.':
            outfile.add(f'{ovadir}/{file}', arcname=f'{file}')
    outfile.close()

def writeovf(ovadir, outdir, values):

    files = os.listdir(ovadir)
    for file in files:
        if '.iso' in file:
            ovffile = file[0:len(file)-4]
            break
    ovf = open(f'{ovadir}/{ovffile}.ovf','w')
    format = open(f'{outdir}/format.ovf')
    for line in format:
        outline = line
        if 'Property ovf:key=' in line:
            keybegin = line.find('"')+1
            keyend = line.find('"', keybegin)
            key = line[keybegin:keyend]
            try:
                keyvalue = values[key]
            except:
                keyvalue = ''
            print(line)
            if keyvalue != '':
                keybegin = line.find('ovf:value="')
                outline = line[0:keybegin] + 'ovf:value="' + keyvalue + '">\n'
        ovf.write(outline)
    ovf.close()
    format.close()

if __name__ == '__main__':

    parameters = open(f'{outdir}/parameters.csv', 'r', encoding='utf-8-sig')
    header = parameters.readline().strip('\n').split(',')
    for line in parameters:
        data = line.strip('\n').split(',')
        values = {}
        index = 0
        for parameter in header:
            values[parameter] = data[index]
            index += 1
        print(values)
        writeovf(ovadir, outdir, values)
        writemanifest(ovadir)
        tarova(ovadir, outdir, values['hostname'])
