lat2cyr
=======

Lat2Cyr convert text files or subtitles from latin to cyrillic characters.
If input file is CP1251 (Windows-1251) encoding program will make utf8
output file.
Program will try to autodetect encoding type of file
between UTF-8 and CP1250 (Windows-1250)

Requrements
    termcolor, cchardet

Version: 0.3.2

Usage:
    lat2cyr [encoding] [FileName]

Encodings:
    utf8
    cp1250 - Central European

Examples:
    lat2cyr name_of_file.srt
    lat2cyr cp1250 name_of_file.txt

Program create file with results named name_of_file.cyr.txt and name_of_file.cyr.utf8.txt

termcolor and cchardet can be installd with pip or easy_install
pip install termcolor
pip install cchardet
