#!/usr/bin/python

import urllib2
from os.path import basename
from urlparse import urlsplit

def url2name(url):
	return basename(urlsplit(url)[2])

def download(url, localFileName = None):
	print( 'download : ' + url )
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

# http://www.colorwiki.com/wiki/Test_Images

# from http://www.brucelindbloom.com/index.html?ReferenceImages.html
#download( 'http://www.brucelindbloom.com/downloads/DeltaE_16bit_gamma1.0.tif.zip' )
download( 'http://www.brucelindbloom.com/downloads/DeltaE_16bit_gamma2.2.tif.zip' )
download( 'http://www.brucelindbloom.com/downloads/DeltaE_8bit_gamma1.0.tif.zip' )
download( 'http://www.brucelindbloom.com/downloads/DeltaE_8bit_gamma2.2.tif.zip' )

#from http://www.brucelindbloom.com/index.html?RGB16Million.html
download( 'http://www.brucelindbloom.com/downloads/RGB16Million.tif.zip' )
download( 'http://www.brucelindbloom.com/downloads/RGB16Million.png' )

# from http://www.chromix.com/downloadarea/testimages/frontier_color57s.jpg
download( 'http://www.chromix.com/downloadarea/testimages/frontier_color57s.jpg' )


# from http://www.northlight-images.co.uk/downloadable_1/DL_page.html
download( 'http://www.northlight-images.co.uk/downloadable_2/media_check.tif' )
download( 'http://www.northlight-images.co.uk/downloadable_2/test-ramp_2.zip' )
download( 'http://www.northlight-images.co.uk/downloadable_2/matrixlarge_2.zip' )

# from http://www.colormanagement.org/en/testimages.html
download( 'http://www.colormanagement.org/download_files/ColorSolutions_Monitortestbilder_v3.zip' )
download( 'http://www.colormanagement.org/download_files/Universal_SmoothnessTest-en.zip' )
download( 'http://www.colormanagement.org/download_files/TestingSeparations_ChannelAllocation-en.zip' )
download( 'http://www.colormanagement.org/download_files/Testing_ToneValueDifferentiation-en.zip' )
download( 'http://www.colormanagement.org/download_files/SmoothnessCheck_RG_radial-en.zip' )
download( 'http://www.colormanagement.org/download_files/Test_Out-of-Gamut_colors-en.zip' )
download( 'http://www.colormanagement.org/download_files/SourceProfileTest_CMYK_5percent-en.zip' )
download( 'http://www.colormanagement.org/download_files/Colorful_Night-en.zip' )


# from http://www.hutchcolor.com/Images_and_targets.html
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/P2P_Package.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/G7_press_bar.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/GrayRails.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/GrayBoat.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/TAC_04.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/MicroCMYK.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/GrayFinder.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/paints.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/graycal_03.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/Lab_Ramp_03.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/HCProof_Qualifier.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/Proof_Qualifier_RGB_03.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/White_Balance_RGB.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/CMYK_Peeker.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/CMS_30_128.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/HC_Screen_Test3.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/RGBXPLORER8.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/MicroGrayTest.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/RGB_Curve_Guide.zip' )
download( 'http://www.hutchcolor.com/Targets_&_images_to_go/HC2052F_Beta.zip' )

# from http://www.colour-science.com/quality%20test%20tools/test%20files/test%20files%20overview.htm' )
download( 'http://www.colour-science.com/quality%20test%20tools/test%20files/Reference%20Print%20monitor%20900x600pixel.jpg' )
download( 'http://www.colour-science.com/quality%20test%20tools/test%20files/Reference%20Print%20printer%202362x3543pixel.jpg' )

# from http://www.andrewdarlow.com/calib.html
download( 'http://www.andrewdarlow.com/calib/ctest_RGBfromCYMK.jpg' )
download( 'http://www.andrewdarlow.com/calib/ctest_clrmatchRGB.jpg' )
download( 'http://www.andrewdarlow.com/calib/ctest_adobergb.jpg' )

# from http://www.normankoren.com/printer_calibration.html
download( 'http://www.digitaldog.net/files/Printer_Test_file.jpg.zip' )

# from http://www.bealecorner.org/red/test-patterns/
download( 'http://www.bealecorner.org/red/test-patterns/Zone720-sine-g22-A.png' )
download( 'http://www.bealecorner.org/red/test-patterns/Zone720-sine-g22-b.png' )
download( 'http://www.bealecorner.org/red/test-patterns/Zone720-hardedge-A.png' )
download( 'http://www.bealecorner.org/red/test-patterns/Zone720-hardedge-B.png' )
download( 'http://www.bealecorner.org/red/test-patterns/star-chart-sine144-720dpi.png' )
download( 'http://www.bealecorner.org/red/test-patterns/star-chart-bars144-600dpi.png' )
download( 'http://www.bealecorner.org/red/test-patterns/star-chart-bars-full-600dpi.png' )
download( 'http://www.bealecorner.org/red/test-patterns/Linear-ZonePlate.png ' )
download( 'http://www.bealecorner.org/red/test-patterns/Gradient-16bit.png' )
download( 'http://www.bealecorner.org/red/test-patterns/Gradient-16bit.tif' )
download( 'http://www.bealecorner.org/red/test-patterns/Gradient-8bit.png' )

# from http://www.bealecorner.com/trv900/respat/
download( 'http://www.bealecorner.com/trv900/respat/eia1956-small.jpg' )
download( 'http://www.bealecorner.com/trv900/respat/color-chart.png' )
