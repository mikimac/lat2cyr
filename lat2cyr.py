#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import codecs
import cchardet
from lat2cyrLib import Lat2Cyr
from termcolor import colored

__VERSION__ = '0.3.2'
__AUTHOR__ = 'Mihail Cvetkoski'
__ProgramName__ = 'Lat2Cyr'
__package__ = 'org.mihail.lat2cyr'


def detectEncoding(string):
    encodinsList = ['utf8', 'cp1250']
    errors = 'strict'
    if isinstance(string, unicode):
        return 'unicode'
    else:
        for enc in encodinsList:
            try:
                string = string.decode(enc, errors)
                return enc
            except UnicodeError:
                continue
        raise UnicodeError('Failed to convert %r' % string)


def getEncoding(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    enc_tryouts = []
    encoding = ''
    for line in lines:
        enc_tryouts.append(detectEncoding(line))
    for enc in enc_tryouts:
        if enc == 'utf8' and (encoding == '' or encoding == 'utf8'):
            encoding = 'utf8'
        else:
            if enc != 'utf8':
                encoding = enc
    return encoding


def detectEncoding2(infile):
    rawdata = open(infile, "r").read()
    res = cchardet.detect(rawdata)
    enc = res['encoding']
    if enc == 'WINDOWS-1250':
        enc = 'cp1250'
    elif enc == 'WINDOWS-1251':
        enc = 'cp1251'
    elif enc == 'ISO-8859-2':
        enc = 'cp1250'
    elif enc == 'UTF-8':
        enc = 'utf8'
    return enc


def percentage(part, whole):
        return 100 * float(part) / float(whole)


def openFile(filename, encoding=None):
    print """
%s convert text files or subtitles from latin to cyrillic characters.
Version: %s
Author: %s
""" % (colored(__ProgramName__, 'blue', attrs=['bold']),
       colored(__VERSION__, 'red', attrs=['bold']),
       colored(__AUTHOR__, 'red', attrs=['bold']))
    lat = Lat2Cyr()
    if os.path.isfile(filename):
        if not encoding:
            print 'Detecting encoding'
            encoding = detectEncoding2(filename)
            print 'Found encoding type: {0}\n' \
                  .format(colored(encoding, 'cyan'))
            # sys.exit()
        extension = (os.path.splitext(filename)[1])
        ime = (os.path.splitext(filename)[0])
        fileIn = codecs.open(filename, 'r', encoding)
        fileInLines = fileIn.readlines()
        fileIn.close()
        fileOut2 = False
        if encoding == 'cp1251':
            fileOut = codecs.open(ime + '.cyr.utf8' + extension, 'w', 'utf8')
            i = 1
            for line in fileInLines:
                sys.stdout.write('\r')
                percent = percentage(i, len(fileInLines))
                print 'Convreting: %.0f%%' % percent,
                sys.stdout.flush()
                fileOut.write(line)
                i += 1
            fileOut.close()
            print '\n\nConversation process finished'
            print 'File %s%s%s was converted' \
                  % (colored(ime, 'red'),
                  colored('.cyr.utf8', 'red'),
                  colored(extension, 'red')) + \
                  ' to utf8 encoding'
        else:
            if encoding == 'utf8':
                fileOut = codecs.open(ime + '.cyr' + extension, 'w', 'utf8')
            else:
                fileOut = codecs.open(ime + '.cyr' + extension, 'w', 'cp1251')
                fileOut2 = codecs.open(ime + '.cyr.utf8' + extension,
                                       'w', 'utf8')
            i = 1
            for line in fileInLines:
                sys.stdout.write('\r')
                percent = percentage(i, len(fileInLines))
                print 'Convreting: %.0f%%' % percent,
                sys.stdout.flush()
                out = lat.lat2cyr(line)
                fileOut.write(out)
                if fileOut2:
                    fileOut2.write(out)
                i += 1

            fileOut.close()
            print '\n\nConversation process finished'
            if fileOut2:
                fileOut2.close()
                print 'File %s%s%s was saved' \
                      % (colored(ime, 'red'),
                         colored('.cyr.utf8', 'red'),
                         colored(extension, 'red')) + \
                      ' with utf8 encoding'
                print 'File %s%s%s was saved' \
                      % (colored(ime, 'red'),
                         colored('.cyr', 'red'),
                         colored(extension, 'red')) + \
                      ' with cp1251 (Cyrillic) encoding'
            else:
                print 'File %s%s%s was saved' \
                      % (colored(ime, 'red'),
                         colored('.cyr', 'red'),
                         colored(extension, 'red')) + \
                      ' with utf8 encoding'


def about():
    print """
{0} convert text files or subtitles from latin to cyrillic characters.
If input file is CP1251 (Windows-1251) encoding program will make utf8
output file.
Program will try to autodetect encoding type of file
between UTF-8 and CP1250 (Windows-1250)

Version: {1}
Author: {2}

Usage:
    {3} [{4}] [{5}]

Encodings:
    {6}
    {7} - Central European

Examples:
    {3} {8}
    {3} {7} {9}

Program create file with results named {10}
    """.format(colored(__ProgramName__, 'blue', attrs=['bold']),
               colored(__VERSION__, 'red', attrs=['bold']),
               colored(__AUTHOR__, 'red', attrs=['bold']),
               colored('lat2cyr', 'blue', attrs=['bold']),
               colored('encoding', 'cyan'),
               colored('FileName', 'red'),
               colored('utf8', 'cyan'),
               colored('cp1250', 'cyan'),
               colored('name_of_file.srt', 'red'),
               colored('name_of_file.txt', 'red'),
               colored('name_of_file.cyr.txt', 'red'))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        openFile(filename)
    elif len(sys.argv) == 3:
        encodinsList = ['utf8', 'cp1250']
        encoding = sys.argv[1]
        filename = sys.argv[2]
        if not encoding in encodinsList:
            print 'Unknown encoding'
            encoding = None
        if not encoding:
            openFile(filename)
        else:
            openFile(filename, encoding)
    else:
        about()

if __name__ == '__main__':
    main()
