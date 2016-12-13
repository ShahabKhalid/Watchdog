import sys,urllib2,re,time
from socket import error as SocketError
from time import gmtime, strftime
print("Insta Crawler Started")
print("Crawling `"+sys.argv[1]+"` for new bios")
f = open(sys.argv[1]+".bios","a+")
bio = ""
while True:
	try:
		response = urllib2.urlopen('https://www.instagram.com/'+sys.argv[1])
		html = response.readlines()
		for line in html:
			#print(line)
			m = re.match(r'(.*)(<meta property="og:description" content=")(.*)(" />)', line)
			if m:
				newbio = m.group(3)
				#print(newbio)
				if newbio != bio:
					print("Bio Updated["+strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())+"]: "+newbio)
					f.write("["+strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())+"] "+newbio+"\n")
					bio = newbio
		time.sleep(5)
	except KeyboardInterrupt:
		print("Bye bye Sir")
		f.close()
		exit(0)
	except SocketError as e:
		pass
	except Exception:
		pass
