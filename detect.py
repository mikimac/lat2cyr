#!/usr/bin/python
# -*- coding: utf-8 -*-

import cchardet
import sys


if len(sys.argv) == 2:
    infile = sys.argv[1]
    rawdata = open(infile, "r").read()
    result = cchardet.detect(rawdata)
    charenc = result['encoding']
    print result
