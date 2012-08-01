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

# from http://www.fileformat.info

download( 'http://www.fileformat.info/format/jpeg/sample/35e126905ffc400c881e8c0ffe035927/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/54a3985c8247414292af453c1a29160f/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/d4ade189a4a04b5d892e5c96d0c2cd24/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/ffe8869cda8748559f0780765c3ba9d8/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/fcdecb6276104eb3af10133c20518ac5/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/afc3b98f5bc345388ccbff50ebd9c574/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/a9b73af6740343c1b7e1e516945f202d/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/d984ce472b7a4feda8d73daa114da0d0/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/fee1b66ee33f4a2fbe43dec44af0569f/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/0f26f062766b414080017101f1e69aab/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/d1a55066566242fd92b3bca40663949f/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/a4c0e04be5444be39ea67b9f9bd8c841/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/8dc7e10fceba41528cb97e6d4f1db223/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/63d87d819f6e4c198fe1a7b61cd0c4de/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/1efc14a54d5d403fa95693863a801586/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/a0e71fb198aa485da6f7fd2a49951b29/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/6de5aa422dd04ce19e5dcfdc3829b87d/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/fbf1566849f14630b33682d7abca548f/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/8a0b6373cfbc45e0bf3ca50c682e56ab/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/59b7baeccc544017b2d5901bc8ce8c48/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/1a41b987f5104223a28ce4c1f1458386/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/cb3175688bd44e008293a59ad885221c/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/fffcea1cc2e9403eb398a2447a20f169/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/3fdb8243598c400db059ef8c1251a780/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/2da9006f07b3492b89322fcae11fe441/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/0c047d42fdfb419e86c594f0f7ad3ce1/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/67742eb459c24b94b582cf44216c7133/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/1c1ac1e4c0314cb8b66bd9ec72ec9f80/download' )
download( 'http://www.fileformat.info/format/jpeg/sample/f37c22bb17f54d738db47cb2d4b6c68a/download' )

# from http://www.w3.org/MarkUp/Test/xhtml-print/20050519/tests/A_2_1-BF-01.htm

download( 'http://www.w3.org/MarkUp/Test/xhtml-print/20050519/tests/jpeg444.jpg' )
download( 'http://www.w3.org/MarkUp/Test/xhtml-print/20050519/tests/jpeg400jfif.jpg' )
download( 'http://www.w3.org/MarkUp/Test/xhtml-print/20050519/tests/jpeg422jfif.jpg' )
download( 'http://www.w3.org/MarkUp/Test/xhtml-print/20050519/tests/jpeg420exif.jpg' )
