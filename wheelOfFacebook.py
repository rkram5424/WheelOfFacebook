#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wheelOfFacebook.py
#  
#  Copyright 2013 ryan <ryan@porta-penguin>
#  Last edit: 06/21/13 
#

import random, urllib2, httplib, webbrowser
from urlparse import urlparse

def main():
	findValid()
	return 0

def findValid():
	valid = False
	idNum = 000000000
	while valid == False:
		idNum = randomize()
		if validate(idNum) == True:
			valid = True
		else:
			valid = False
	return idNum
	
def randomize():
	idNum = ''
	for i in range(0,9):
		randy = random.randint(0,9)
		idNum += str(randy)
	return idNum

def validate(idNum):
	fullUrl = 'http://graph.facebook.com/' + idNum + '/picture?type=large'
	reUrl = get_redirected_url(fullUrl)
	profile = 'http://facebook.com/' + idNum
	if not(reUrl.endswith('.gif')):
		webbrowser.open(profile)
		#print(profile)
		return True
	else:
		return False
		
def get_redirected_url(url):
	opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
	request = opener.open(url)
	return request.url
		
#def getName(idNum):
	#name = ''
	#idUrl = 'http://facebook.com/' + idNum
	#response = urllib2.urlopen(idUrl)
	#pageSource = response.read()
	#name = pageSource.split('"id="pageTitle">"', 1)[0]
	#print pageSource
	#return name

if __name__ == '__main__':
	main()
