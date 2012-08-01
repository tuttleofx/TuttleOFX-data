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

# from http://www.microimages.com/gallery/jp2
download( 'http://www.microimages.com/gallery/jp2/1.jp2' )

# from http://www.fnordware.com/j2k/jp2samples.html
download( 'http://www.fnordware.com/j2k/relax.jp2' )

# from http://www.openjpeg.org/index.php?menu=samples
download( 'http://www.openjpeg.org/samples/Bretagne1.j2k' )
download( 'http://www.openjpeg.org/samples/Bretagne2.j2k' )
download( 'http://www.openjpeg.org/samples/Cevennes1.j2k' )
download( 'http://www.openjpeg.org/samples/Cevennes2.jp2' )
download( 'http://www.openjpeg.org/samples/Rome.jp2' )
download( 'http://www.openjpeg.org/samples/Speedway.mj2' )
download( 'http://www.openjpeg.org/samples/Facade.j2k' )


