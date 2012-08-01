#!/usr/bin/python

import urllib2
from os.path import basename
from urlparse import urlsplit

def url2name(url):
	return basename(urlsplit(url)[2])

def download(url, localFileName = None):
	print('download : ' + url )
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

# from ftp://ftp.graphicsmagick.org/pub/dpx/README.txt

download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-1920x1080-RGB-8.dpx' )
download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-1920x1080-RGB-10.dpx' )
download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-1920x1080-RGB-10-packed.dpx' )
download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-1920x1080-RGB-12.dpx' )
download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-1920x1080-RGB-12-packed.dpx' )
download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-1920x1080-RGB-16.dpx' )

download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-1920x1080-LinearLuma-10.dpx' )
download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-720x486-LinearLuma-10.dpx' )

download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-1920x1080-Rec709Luma-10.dpx' )
download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-720x486-Rec601Luma-10.dpx' )

download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-1920x1080-Rec709YCbCr-4:4:4-10.dpx' )

download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-1920x1080-Rec709YCbCr-4:2:2-10.dpx' )
download( 'ftp://ftp.graphicsmagick.org/pub/dpx/flowers-720x486-Rec601YCbCr-4:2:2-10.dpx' )


