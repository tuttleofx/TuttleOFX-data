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

# from http://www.rawsamples.ch/index_de.php

# canon
download( 'http://www.rawsamples.ch/raws/canon/1dsm3/RAW_CANON_1DSM3.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/1dsm2/RAW_CANON_1DSM2.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/1ds/RAW_CANON_1DS.ZIP' )
download( 'http://www.rawsamples.ch/raws/canon/1dm3/RAW_CANON_1DMARK3.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/1dm2n/RAW_CANON_1DM2N.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/1dm2/RAW_CANON_1DM2.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/1d/RAW_CANON_1D_RAW.ZIP' )
download( 'http://www.rawsamples.ch/raws/canon/dcs1/RAW_CANON_DCS1.ZIP' )

download( 'http://www.rawsamples.ch/raws/canon/5dm2/RAW_CANON_5DMARK2_PREPROD.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/5d/RAW_CANON_5D_ARGB.CR2' )

download( 'http://www.rawsamples.ch/raws/canon/50d/RAW_CANON_50D.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/40d/RAW_CANON_40D_RAW_V336643C.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/40d/RAW_CANON_40D_RAW_V105.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/40d/RAW_CANON_40D_RAW_V104.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/40d/RAW_CANON_40D_SRAW_V103.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/40d/RAW_CANON_40D_RAW_V103.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/30d/RAW_CANON_30D.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/20d/RAW_CANON_20D.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/10d/RAW_CANON_10D.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/d60/RAW_CANON_D60_ARGB.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/d30/RAW_CANON_D30_SRGB.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/d30/RAW_CANON_D30_SRGB.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/d2000/RAW_CANON_D2000.ZIP' )

download( 'http://www.rawsamples.ch/raws/canon/450d/RAW_CANON_450D.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/400d/RAW_CANON_400D_ARGB.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/350d/RAW_CANON_350D.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/300d/RAW_CANON_300D.CRW' )

download( 'http://www.rawsamples.ch/raws/canon/pro1/RAW_CANON_PRO1_ARGB.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/pro70/RAW_CANON_PRO70_SRGB.CRW' )

download( 'http://www.rawsamples.ch/raws/canon/g10/RAW_CANON_G10.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/g9/RAW_CANON_G9.CR2' )
download( 'http://www.rawsamples.ch/raws/canon/g7/RAW_CANON_G7.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/g6/RAW_CANON_G6_SRGB.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/g5/RAW_CANON_G5_SRGB.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/g3/RAW_CANON_G3.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/g2/RAW_CANON_G2.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/g1/RAW_CANON_G1.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/s5is/RAW_CANON_S5IS.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/s3is/RAW_CANON_S3IS.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/s2is/RAW_CANON_S2IS.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/sd750/RAW_CANON_SD750.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/sd900/RAW_CANON_IXUS900TI_CHDK.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/sd950/RAW_CANON_SD950.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/s70/RAW_CANON_S70_SRGB.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/s60/RAW_CANON_S60_SRGB.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/s50/RAW_CANON_S50.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/s45/RAW_CANON_S45.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/s40/RAW_CANON_S40.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/s30/RAW_CANON_S30.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/a720is/RAW_CANON_A720IS.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/a710/RAW_CANON_A710.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/a620/RAW_CANON_A620.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/a610/RAW_CANON_A610.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/a570/RAW_CANON_A570IS.CRW' )
download( 'http://www.rawsamples.ch/raws/canon/a550/RAW_CANON_A550.CRW' )

# nikon
download( 'http://www.rawsamples.ch/raws/nikon/d3x/RAW_NIKON_D3X.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d3/RAW_NIKON_D3.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d2x/RAW_NIKON_D2X_SRGB.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d1x/RAW_NIKON_D1X.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d1/RAW_NIKON_D1.NEF' )

download( 'http://www.rawsamples.ch/raws/nikon/d700/RAW_NIKON_D700.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d300/RAW_NIKON_D300.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d200/RAW_NIKON_D200_SRGB.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d100/RAW_NIKON_D100.NEF' )

download( 'http://www.rawsamples.ch/raws/nikon/d90/RAW_NIKON_D90.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d80/RAW_NIKON_D80_SRGB.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d70/RAW_NIKON_D70.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d60/RAW_NIKON_D60.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d50/RAW_NIKON_D50.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/d40/RAW_NIKON_D40_SRGB.NEF' )

download( 'http://www.rawsamples.ch/raws/nikon/e5700/RAW_NIKON_E5700_SRGB.NEF' )
download( 'http://www.rawsamples.ch/raws/nikon/e5400/RAW_NIKON_E5400.NEF' )

download( 'http://www.rawsamples.ch/raws/nikon/p6000/RAW_NIKON_P6000_GPS.NRW' )


