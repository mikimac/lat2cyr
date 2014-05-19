#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import sys
import os


class Lat2Cyr(object):

    LAT_TO_CYR = {
        # Golemi bukvi
        u'A': u'А',
        u'S': u'С',
        u'D': u'Д',
        u'F': u'Ф',
        u'G': u'Г',
        u'H': u'Х',
        u'J': u'Ј',
        u'K': u'К',
        u'L': u'Л',
        u'Č': u'Ч',
        u'Ć': u'Ћ',
        u'Ž': u'Ж',
        u'Lj': u'Љ',
        u'Nj': u'Њ',
        u'E': u'Е',
        u'R': u'Р',
        u'T': u'Т',
        u'Z': u'З',
        u'U': u'У',
        u'I': u'И',
        u'O': u'О',
        u'P': u'П',
        u'Š': u'Ш',
        u'Đ': u'Ђ',
        u'Dž': u'Џ',
        u'C': u'Ц',
        u'V': u'В',
        u'B': u'Б',
        u'N': u'Н',
        u'M': u'М',
        u'Dz': u'Ѕ',
        # mali bukvi
        u'a': u'а',
        u's': u'с',
        u'd': u'д',
        u'f': u'ф',
        u'g': u'г',
        u'h': u'х',
        u'j': u'ј',
        u'k': u'к',
        u'l': u'л',
        u'č': u'ч',
        u'ć': u'ћ',
        u'ž': u'ж',
        u'lj': u'љ',
        u'nj': u'њ',
        u'e': u'е',
        u'r': u'р',
        u't': u'т',
        u'z': u'з',
        u'u': u'у',
        u'i': u'и',
        u'o': u'о',
        u'p': u'п',
        u'š': u'ш',
        u'đ': u'ђ',
        u'dž': u'џ',
        u'c': u'ц',
        u'v': u'в',
        u'b': u'б',
        u'n': u'н',
        u'm': u'м',
        u'dz': u'ѕ'
    }

    CYR_TO_LAT = {
        # Golemi bukvi
        u'А': u'A',
        u'С': u'S',
        u'Д': u'D',
        u'Ф': u'F',
        u'Г': u'G',
        u'Х': u'H',
        u'Ј': u'J',
        u'К': u'K',
        u'Л': u'L',
        u'Ч': u'Č',
        u'Ћ': u'Ć',
        u'Ж': u'Ž',
        u'Љ': u'Lj',
        u'Њ': u'Nj',
        u'Е': u'E',
        u'Р': u'R',
        u'Т': u'T',
        u'З': u'Z',
        u'У': u'U',
        u'И': u'I',
        u'О': u'O',
        u'П': u'P',
        u'Ш': u'Š',
        u'Ђ': u'Đ',
        u'Џ': u'Dž',
        u'Ц': u'C',
        u'В': u'V',
        u'Б': u'B',
        u'Н': u'N',
        u'М': u'M',
        u'Ѕ': u'Dz',
        # mali bukvi
        u'а': u'a',
        u'с': u's',
        u'д': u'd',
        u'ф': u'f',
        u'г': u'g',
        u'х': u'h',
        u'ј': u'j',
        u'к': u'k',
        u'л': u'l',
        u'ч': u'č',
        u'ћ': u'ć',
        u'ж': u'ž',
        u'љ': u'lj',
        u'њ': u'nj',
        u'е': u'e',
        u'р': u'r',
        u'т': u't',
        u'з': u'z',
        u'у': u'u',
        u'и': u'i',
        u'о': u'o',
        u'п': u'p',
        u'ш': u'š',
        u'ђ': u'đ',
        u'џ': u'dž',
        u'ц': u'c',
        u'в': u'v',
        u'б': u'b',
        u'н': u'n',
        u'м': u'm',
        u'ѕ': u'dz'
    }
    dupli = {
        # Golemi bukvi
        u'Lj': u'Љ',
        u'Nj': u'Њ',
        u'Dž': u'Џ',
        u'Dz': u'Ѕ',
        # Mali bukvi
        u'lj': u'љ',
        u'nj': u'њ',
        u'dž': u'џ',
        u'dz': u'ѕ'
    }

    def lat2cyr(self, txt, encoding='cp1250'):
        if not txt:
            return txt
        if not isinstance(txt, unicode):
            print 'Dekodiram'
            lat = txt.decode(encoding)  # copy & force unicode
        else:
            lat = txt[:]  # copy
        for c, l in self.dupli.items():
            lat = lat.replace(c, l)
        for c, l in self.LAT_TO_CYR.items():
            lat = lat.replace(c, l)
        for c, l in self.CYR_TO_LAT.items():
            lat = lat.replace('<'+c+'>', '<'+l+'>')
            lat = lat.replace('</'+c+'>', '</'+l+'>')
        return lat

    def convert(self, inputFile):
        if inputFile:
            extension = os.path.splitext(inputFile)[1][1:]
            ime = os.path.splitext(inputFile)[0][0:]
            file = codecs.open(inputFile, encoding='cp1250')
            f = codecs.open(ime + '.cyr.' + extension, 'w', 'cp1251')
            for line in file:
                f.write(self.lat2cyr(line))
                # print(lat2cyr(line))
            f.close()
            file.close()

    def otvori(self):
        [filename] = sys.argv[1:]
        extension = os.path.splitext(filename)[1][1:]
        ime = os.path.splitext(filename)[0][0:]
        file = codecs.open(filename, encoding='cp1250')
        f = codecs.open(ime + '.cyr.' + extension, 'w', 'cp1251')
        for line in file:
            f.write(self.lat2cyr(line))
            # print(lat2cyr(line))
        f.close()
        file.close()
