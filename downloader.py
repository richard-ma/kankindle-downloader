#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
import urllib2, cookielib

download_log = []
with open('download.log', 'r') as download_log_file:
    for line in download_log_file.readlines():
        download_log.append(line.replace('\n', ''))
print download_log

with open('books-sorted.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        url, name = row
        print url
        if (url in download_log):
            print url + ' is downloaded. [skipped]'
            continue
        name = name.decode('utf-8')
        print name

        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        r = opener.open(url)
        download_url = url.replace('view', 'simple/down').replace('.html', '')
        print download_url

        f = opener.open(download_url)
        fileName = name + '.mobi'
        with open(fileName, 'w') as code:
            code.write(f.read())
        print fileName + ' downloaded'

        with open('download.log', 'a') as download_log_file:
            download_log_file.write(url + '\n')
        download_log.append(url)
