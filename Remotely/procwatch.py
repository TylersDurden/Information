import os


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def procedure_dump(args):
    cmd = 'lsof'
    if len(args)>=1:
        for arg in args:
            cmd += ' ' + arg
        os.system(cmd + '>> procs.txt')
        os.system('clear')
        procedures = swap('procs.txt', True)
    else:
        os.system('lsof >> procs.txt')
        os.system('clear')
        procedures = swap('procs.txt', True)
    return procedures


def procedure_parser(procedures):
    PROCS = {}
    II = 0
    for proc in procedures:
        stats = proc.split(' ')
        DATA = []
        for info in stats:
            if info != '':
                DATA.append(info)
        try:
            info = {'COMMAND': DATA.pop(0),
                    'PID': DATA.pop(0),
                    'TID': DATA.pop(0),
                    'USER': DATA.pop(0),
                    'FD': DATA.pop(0),
                    'TYPE': DATA.pop(0),
                    'DEVICE': DATA.pop(0),
                    'SIZE/OFFSET': DATA.pop(0),
                    'NODE': DATA.pop(0)}
            II += 1
            PROCS[II] = info
        except IndexError:
            pass
    print str(II) + " Procedures Mapped [Fully] to System Info"
    return PROCS


def main():
    procedures = procedure_dump([])
    print str(len(procedures)) + " Running Procedures Identified "
    # Parse the raw procedure data
    PROCS = procedure_parser(procedures)


if __name__ == '__main__':
    main()