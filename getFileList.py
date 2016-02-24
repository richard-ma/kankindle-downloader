#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2, re
import csv

lastPageNumber = 52 

for i in range(24, lastPageNumber+1):
    url = "http://kankindle.com/simple/page/" + str(i)
    html = urllib2.urlopen(url).read()
    books = re.findall(r'(http://kankindle.com/view/[0-9]*.html)" title="(.*)"', html)

    writer = csv.writer(file(str(i)+'.csv', 'wb'))
    for book in books:
        writer.writerow(book)

    sys.stderr.write('.')
