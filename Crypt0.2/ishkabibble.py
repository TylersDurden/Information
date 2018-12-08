import os, sys, numpy as np

fGRN = '\33[32m'
fRED = '\33[91m'
fBLU = '\33[34m'
fBLD = '\33[1m'
fEND = '\33[0m'


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def dump_to_console(vargin):
    for element in vargin:
        print element


def stamp_generator(dims, cliche):
    seed = np.random.randint(0,2,dims[0]*dims[1]).reshape(dims)
    for x in range(dims[0]):
        line = ''
        for y in range(dims[1]):
            line += str(seed[x,y])
        if cliche:  # If cliche, Enter The Matrix
            print fGRN + fBLD + line + fEND
        else:
            print line
    return seed


def main():
    if len(sys.argv) <= 1:
        stamp_generator([5, 5])
    if '-manual' in sys.argv:
        stamp_generator([int(sys.argv[2]), int(sys.argv[3])], False)
    if '-matrix' in sys.argv:
        stamp_generator([8440, 100],True)


if __name__ == '__main__':
    main()

