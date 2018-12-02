import os, sys
from scipy.io import wavfile


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def simple_alpha_map():
    alphas = ['a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x',
              'y', 'z']
    specials = [' ', '`', '!', '@', '#',
                '$', '^', '&', '*', '(',
                ')', '-', '_', '=', '+',
                '[', '{', '}', ']', '\\',
                '|', ':', ';', '"', ',',
                '<', '>', ',', '.', '/',
                '?']

    mapping = {}
    invmaps = {}
    ii = 0
    for letter in alphas:
        mapping[ii] = letter
        invmaps[letter] = ii
        ii += 1
    for let in alphas:
        mapping[ii] = let.upper()
        invmaps[let.upper()] = ii
        ii += 1
    for i in range(9):
        mapping[ii] = i
        invmaps[i] = ii
        ii += 1
    for character in specials:
        mapping[ii] = character
        invmaps[character] = ii
        ii += 1
    # Also adding extra bin for unknown characters
    mapping[ii] = 'error'
    invmaps['error'] = ii
    return mapping, invmaps


def yes_or_no():
    ANSWER = {1:True,2:False}
    print "[1] YES"
    print "[2] NO"
    return ANSWER[int(input('Enter a Selection: '))]


# ################################## POLY ################################## #


class Poly:
    # Mappings for actual information bits [characters/symbols <-> Numbers]
    LUT = {}
    Chars = {}
    # Where to stream in the data FROM
    source = ''
    # Where data is streaming TO
    dest = ''
    # Verbosity
    isVerbose = False

    isMP3source = False

    def __init__(self, symbols, mapping, verbosity):
        self.LUT = mapping
        self.Chars = symbols
        self.isVerbose = verbosity

    def set_data_input_stream(self, source_def, output_def):
        self.source = source_def
        self.dest = output_def
        if self.isVerbose:
            print "INPUT SOURCE_DEF: "+source_def
            print "OUTPUT SOURCE_DEF: "+output_def
        if '.mp3' in source_def:
            self.isMP3source = True
            if self.isVerbose:
                print "Source Def is MP3"

    @staticmethod
    def seek_cover(isLinux):
        if isLinux:
            cmd_mp3 = 'p=$PWD; cd /; find -name *.mp3 | cut -b 2- >> $p/mp3.txt; cd $p'
            os.system(cmd_mp3)
            mp3s = swap('mp3.txt', True)
            print str(len(mp3s)) + " MP3s Found"
            cmd_wav = 'p=$PWD; cd /; find -name *.wav | cut -b 2- >> $p/wav.txt; cd $p'
            os.system(cmd_wav)
            wavs = swap('wav.txt', True)
            print str(len(wavs)) + " WAVs Found"
            return mp3s, wavs

    def check_source_file(self):
        # If the source file is already an mp3, then
        # It needs to be converted to a wave first for manipulation
        # and then repackaged as an mp3
        if self.isMP3source:
            fname_out = self.source.split('.mp3')[0] + '.wav'
            cmd = 'ffmpeg -i '+self.source+' '+fname_out+'; mv '+fname_out+' $PWD;clear;ls'
            print cmd
            os.system(cmd)

        else:
            cmd = 'cp '+self.source+' $PWD;ls'
            os.system(cmd)
        os.system('find -name *.wav | cut -b 3- >> fname.txt')
        fname_out = swap('fname.txt', True).pop()


        fs, data = wavfile.read(fname_out)
        print fs.bit_length()
        print len(data)
# ################################## POLY ################################## #


def main():
    isVerbose = False
    isLinux = False

    target_file = ''

    symbols, mapping = simple_alpha_map()

    if '-linux' in sys.argv or '-Linux' in sys.argv:
        isLinux = True

    # Find files to muddle
    mp3list, wavlist = Poly.seek_cover(isLinux)

    if '-t_wav' in sys.argv:
        target_file = wavlist.pop(int(sys.argv[4]))
    if '-t_mp3' in sys.argv:
        target_file = mp3list.pop(int(sys.argv[4]))

    """     Specify an input file for manipulation [Either a WAV or MP3]    """
    if '-v' in sys.argv:
        isVerbose = True
        print str(len(symbols.keys())) + " Character Symbols Mapped"
        if target_file == '':
            print "Do you want to select an MP3?"
            if yes_or_no():
                ii = 0
                for mp3 in mp3list:
                    print str(ii) + " " + mp3
                    ii += 1
                try:
                    target_file = mp3list.pop(int(input('Enter A Selection: ')))
                except KeyError:
                    print "Invalid Selection!"
                    exit(0)
            print "Do you want to select a WAV?"
            if yes_or_no():
                II = 0
                for wav in wavlist:
                    print str(II) + " " + wav
                    II += 1
                try:
                    target_file = wavlist.pop(int(input('Enter a Selection: ')))
                except KeyError:
                    print "Invalid Selection!"
                    exit(0)
            if isLinux:
                os.system('clear')
            if target_file != '':
                print "Target File Selected: \n" + target_file
            else:
                print "No Target File Selected!"

    ''' Start Building the Polyglot '''
    pglot = Poly(symbols, mapping, isVerbose)
    pglot.set_data_input_stream(target_file,'spoofed.mp3')

    pglot.check_source_file()


if __name__ == '__main__':
    main()
