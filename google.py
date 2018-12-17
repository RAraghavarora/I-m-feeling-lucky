#! /usr/bin/python3
import sys, webbrowser, bs4, requests

if len(sys.argv)>1:
	address = ''+'https://google.com/search?q='+'+'.join(sys.argv[1:])
else:
	print("Provide some command line argument corresponding to the google search")
	exit()

#Open the google search page
webbrowser.open(address)

response = requests.get(address)
#Check if the url is valid
try:
	response.raise_for_status()
except:
	print("Sorry, Invalid URL")
bs = bs4.BeautifulSoup(response.text)
links = bs.select('div cite')
count = 0
for link in links:
	count+=1
	webbrowser.open(link.getText())
	if count==5:
		break