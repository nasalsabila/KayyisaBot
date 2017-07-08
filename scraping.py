import urllib2, re
from bs4 import BeautifulSoup
import json
import os
import urllib

url = 'http://www.duaandazkar.com/chapter-4-daily-essential-duas/'

req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen(req)
soup = BeautifulSoup(con, 'html.parser')
entry=soup.find('div', class_='entry-content')
isi = entry.get_text()
y = re.sub("\s+"," ",isi)
carabaca = re.findall(r'Pronunciation(.*?)Translation',y)
baca = [x.encode('ascii','ignore') for x in carabaca]
pronun = [x.encode('utf-8') for x in baca]

arti = re.findall(r'Translation(.*?)Hadith/Benefit',y)
a = [x.encode('ascii','ignore') for x in arti]
ar = [x.encode('utf-8') for x in a]


hadith = re.findall(r'Hadith/Benefit(.*?)Dua [0-9]*',y)
ha = [x.encode('ascii','ignore') for x in hadith]
h = [x.encode('utf-8') for x in ha]


nama = re.findall(r'Dua [0-9]*(.*?)Arabic',y)
n = [x.encode('ascii','ignore') for x in nama]
nm = [x.encode('utf-8') for x in n]


refer = re.findall(r'Reference(.*?)Pronunciation',y)
r = [x.encode('ascii','ignore') for x in refer]
ref = [x.encode('utf-8') for x in r]

# hasil scrap ditulis scraping.json
file = open("scraping.json", "w")
output = {'dua': nm,
	'reference': ref,
	'pronunciation': pronun,
	'translation': ar,
	'hadith': h}
json.dump(output, file)
file.close()

# scraping gambar
links = entry.find_all('img', src=True)
for link in links:
    	link = link["src"].split("src=")[-1]
	imagefile = open(os.path.basename(link), 'wb')
	l = urllib2.Request(link, headers={'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"}) 
	imagefile.write(urllib2.urlopen(l).read())
	imagefile.close()

