import os, sys, matplotlib.pyplot as plt

alphas = ['a','b','c','d','e','f',
          'g','h','i','j','k','l',
          'm','n','o','p','q','r',
          's','t','u','v','w','x',
          'y','z']
specials = [' ','`','!','@','#',
            '$','^','&','*','(',
            ')','-','_','=','+',
            '[','{','}',']','\\',
            '|',':',';','"',',',
            '<','>',',','.','/',
            '?']


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def simple_alpha_map():
    mapping = {}
    ii = 0
    for letter in alphas:
        mapping[ii] = letter
        ii += 1
    for let in alphas:
        mapping[ii] = let.upper()
        ii += 1
    for i in range(9):
        mapping[ii] = i
        ii += 1
    for character in specials:
        mapping[ii] = character
        ii += 1
    # Also adding extra bin for unknown characters
    mapping[ii] = 'error'
    return mapping


def count_letters(example):
    data = []
    alph = simple_alpha_map()
    for item in list(example):
        if item in alph.values():
            II = 0
            for value in alph.values():
                if alph[II] == item:
                    data.append(II)
                II += 1
    print data
    return data


def show_input_menu():
    print '[1] plain-text'
    print '[2] text-file'
    return int(input('Enter a selection: '))


def usage():
    print 'Incorrect Usage! Ex:'
    print 'python experiment.py -in'
    print 'python experiment.py -read'


def read_and_count(fname, map):
    # First make the bins
    bins = {}
    for item in map.keys():
        bins[map[item]] = 0
    # Now fill them with the characters found reading file
    content = swap(fname, False)
    for element in content:
        for character in list(element):
            try:
                bins[str(character).replace("'",'')] += 1
            except KeyError:
                bins['error'] += 1
                pass
    # Make Bar Chart of the Results
    # print str(bins[' '])+" Spaces in "+fname
    # print str(bins['#'])+" #s in " + fname
    plt.bar(range(len(bins)),list(bins.values()), align='center')
    plt.xticks(range(len(bins)), list(bins.keys()))
    plt.show()

    return bins

def main():
    # example = 'testing testing 123'
    # count_letters(example)

    types = {0: 'plaintext', 1: 'textfile'}

    if len(sys.argv) > 1:
        if '-in' in sys.argv[1]:
            opt = show_input_menu()
            if opt not in types.keys():
                usage()
            else:
                if opt == 0:
                    basic = count_letters(input('Enter text: '))
                if opt == 1:
                    text = swap(input('Enter the name of the text file: '), False)
                    for line in text:
                        numbersline = count_letters(line)
        if '-read' in sys.argv:
            symbols = simple_alpha_map()
            print str(len(symbols.keys())) + " elements in Symbol Map"
            if len(sys.argv)>2:
                fname = sys.argv[2]
                read_and_count(fname, symbols)


if __name__ == '__main__':
    main()