# -*- coding: utf-8 -*-
import urllib2
url = "http://uxmilk.jp/12691"
htmldata = urllib2.urlopen(url)
print unicode(htmldata.read(), 'utf-8')
htmldata.close()
