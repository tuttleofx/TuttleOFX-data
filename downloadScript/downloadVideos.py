#!/usr/bin/python

import urllib2
from os.path import basename
from urlparse import urlsplit

def url2name(url):
	return basename(urlsplit(url)[2])

def download(url, localFileName = None):
	localName = url2name(url)
	req = urllib2.Request(url)
	r = urllib2.urlopen(req)
	if r.info().has_key('Content-Disposition'):
		# If the response has Content-Disposition, we take file name from it
		localName = r.info()['Content-Disposition'].split('filename=')[1]
		if localName[0] == '"' or localName[0] == "'":
			localName = localName[1:-1]
	elif r.url != url: 
		# if we were redirected, the real file name we take from the final URL
		localName = url2name(r.url)
	if localFileName: 
		# we can force to save the file as specified name
		localName = localFileName
	f = open(localName, 'wb')
	f.write(r.read())
	f.close()

# from http://istec.colostate.edu/me/facil/dynamics/avis.htm
download( 'http://istec.colostate.edu/me/facil/dynamics/files/drop.avi' )
download( 'http://istec.colostate.edu/me/facil/dynamics/files/flame.avi' )
download( 'http://istec.colostate.edu/me/facil/dynamics/files/bird.avi' )
download( 'http://istec.colostate.edu/me/facil/dynamics/files/cbw3.avi' )

#from http://cinelerra.org/footage/
download( 'http://cinelerra.org/footage/bars_100.avi' )
download( 'http://cinelerra.org/footage/morgen-20030714.avi' )
download( 'http://cinelerra.org/footage/mars-20030905.avi' )