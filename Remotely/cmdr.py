import os, sys 

def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n',''))
    if destroy:
        os.remove(fname)
    return data
    
def commander(cmd, isVerbose):
    os.system(cmd+' >> output.txt')
    data = swap('output.txt',True)
    if isVerbose:
        for line in data:
            print line
    return data
   
   
def main():
    if '-c' in sys.argv:
        sys.argv.pop(0)
        sys.argv.pop(0)
        command = ''
        for arg in sys.argv:
            command += arg + ' '
        output = commander(command, True)

if __name__ == '__main__':
    main()

