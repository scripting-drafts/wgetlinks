import os
import re
#import subprocess
from bs4 import BeautifulSoup
import requests
import time
from time import sleep

url = "http://govtslaves.info/2012/11/11/100-free-survival-downloads/"
page_response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"})
page_content = BeautifulSoup(page_response.content, "html.parser")
names = ""
#cnt = 1
#lastBook = 170

for link in page_content.find_all('p'):
	for linkA in link.find_all('a'):
		hreflinks = linkA.get('href')
		stringLinks = str(hreflinks)
		links = re.findall(r'https\://docs\.google\.com/open\?id\=.+', stringLinks, re.IGNORECASE)
		if len(links) == 1:
#			subprocess.Popen('wget ' + links[0] + ' -O /home/pi/Downloads/' + names, stdin=None, stderr=None, shell=True, universal_newlines=False)
#			communicate()
#			print("wget.download(" + links[0] + "," + '/home/pi/Downloads/' + names + '")')
			print(names)
			print(links[0])
#			sleep(5)
	names = link.get_text()
#	cnt += 1
