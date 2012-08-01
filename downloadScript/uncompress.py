#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import tarfile
import zipfile

def uncompress( filename, ext ):
	print ('uncompress : %s' % ( filename ) )
	
	if ext == '.tar.gz' :
		tar = tarfile.open( filename, 'r:*')
		folder = '.'
		tar.extractall( folder )

	if ext == '.tar.bz2' :
		tar = tarfile.open( filename, 'r:*')
		folder = '.'
		tar.extractall( folder )

	if ext == '.tgz' :
		tar = tarfile.open( filename, 'r:*')
		folder = '.'
		tar.extractall( folder )

	if ext == '.zip' :
		zip = zipfile.ZipFile( filename, 'r' )
		
		listing=[]

		for f in zip.namelist() :
			if not os.path.exists( f ) :
				listing.append( f )
				print f


		folder = '.'
		print listing
		zip.extractall( folder, listing )

for filename in os.listdir("."):
	file, ext = os.path.splitext(filename)
	ext = ext.lower()
	if ( ext == '.zip' ) or ( ext == '.tgz' ) or ( ext == '.tar.bz2' ) or ( ext == '.tar.gz' ) :
		uncompress( filename, ext )

