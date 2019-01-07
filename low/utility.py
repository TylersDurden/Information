import os, sys


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def hexdump_reader(fname, show):
    os.system('hexdump -C '+fname+' >> hex.txt')
    hex = swap('hex.txt', True)
    data = {}
    ii = 1
    for line in hex:
        first = line.split(' ')[2:10]
        second = line.split(' ')[11:19]
        if len(first)>0:
            data[ii] = first
        if len(second) > 0:
            for element in second:
                data[ii].append(element)
        ii += 1
    # Also parse it into shell code style dump
    # using \xABC style printout
    shell = {}
    II = 0
    for ln in data.keys():
        lets = data[ln]
        line = ''
        for letter in lets:
            line += '\\x'+letter
        data[II] = line
        if show:
            print line
        II += 1
    return data, shell
