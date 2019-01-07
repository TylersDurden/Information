from itertools import combinations, permutations
import sys, os, utility

nums = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a','b','c','d','e','f',
           'g','h','i','j','k','l',
           'm','n','o','p','q','r',
           's','t','u','v','w','x',
           'y','z']

special = ['`','~','!','@','#','$',
           '%','^','&','*','(',')',
           '-','_','=','+','[','{',
           ']','}','\\','|',';',':',
           "'",',','<','.','>','/',
           '?',' ']

alphas = []

for letter in letters:
    alphas.append(letter.upper())


def initialize():
    characters = {}
    hexed = {}
    ii = 1
    for num in nums:
        characters[ii] = num
        hexed[ii] = ord(num)
        ii += 1
    for let in letters:
        characters[ii] = let
        hexed[ii] = ord(let)
        ii += 1
    for alpha in alphas:
        characters[ii] = alpha
        hexed[ii] = ord(alpha)
        ii += 1
    for spec in special:
        characters[ii] = spec
        hexed[ii] = ord(spec)
        ii += 1

    return characters, hexed


def display_text_table(text_chars, hex_chars, show):
    line = ''
    r = 1
    mapping = {}
    for i in text_chars.keys():
        line += str(text_chars[i]) + '\t0x' + str(hex_chars[i]) + '\t'
        if r > 0 and r % 3 == 0:
            line += '\n'
            r = 0
        r += 1
        mapping[str(text_chars[i])] = str(hex_chars[i])
    if show:
        print "Text | Hex \t Text | Hex"
        print line
    return mapping


def str2shellcode(text,mapping):
    lines = ''
    n = 0
    i = 1
    for character in list(text):
        lines += '\\x'+mapping[character]
    return lines


def main():
    text_chars, hex_chars = initialize()

    if '-shell' in sys.argv:
        mapping = display_text_table(text_chars, hex_chars, False)
        ex_text = str(input('Enter some text (enclosed in quotes):'))
        print str2shellcode(ex_text, mapping)
    if '-show_hex' in sys.argv:
        mapping = display_text_table(text_chars, hex_chars, True)
    else:
        mapping = display_text_table(text_chars, hex_chars, False)

    if '-hexit' in sys.argv:
        hex_data = utility.hexdump_reader(sys.argv[2], show=True)


if __name__ == '__main__':
    main()
