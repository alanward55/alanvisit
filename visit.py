# -*- coding: utf-8 -*-
import urllib2, urllib, sys, time, random, re, os, traceback

os.system("clear")
#Warna
B = '\033[1m' #Bold
R = '\033[31m' #Red
G = '\033[32m' #Green
Y = '\033[33m' #Yellow
BL = '\033[34m' #Blue
P = '\033[35m' #Purple
W = '\033[37m' #White
U = '\033[2m' #Underline
N = '\033[0m' #Normal

proxy_list = "proxylist.txt"
server = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
		   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
		   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
		   'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
		   'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
		   'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
		   'Microsoft Internet Explorer/4.0b1 (Windows 95)',
		   'Opera/8.00 (Windows NT 5.1; U; en)',
		   'amaya/9.51 libwww/5.4.0',
		   'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
		   'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
		   'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
		   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
		   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
		   'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']

site = ['http://google.com','http://bing.com','http://facebook.com','http://twitter.com','http://yahoo.com']

print G+'''
  █████╗ ██╗      █████╗ ███╗   ██╗██╗   ██╗██╗███████╗██╗████████╗
 ██╔══██╗██║     ██╔══██╗████╗  ██║██║   ██║██║██╔════╝██║╚══██╔══╝
 ███████║██║     ███████║██╔██╗ ██║██║   ██║██║███████╗██║   ██║   
 ██╔══██║██║     ██╔══██║██║╚██╗██║╚██╗ ██╔╝██║╚════██║██║   ██║   
 ██║  ██║███████╗██║  ██║██║ ╚████║ ╚████╔╝ ██║███████║██║   ██║   
 ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝╚══════╝╚═╝   ╚═╝   '''
print R+'=========================Copyright © 2021=========================='
print G+'   +-----------------------------------------------------------+'
print G+'   |Script ini dibuat oleh alanward55 pada tanggal 10 Juni 2021|'
print G+'   +-----+-------------------------+---------------------+-----+'
print G+'         |Email: ondeuli@gmail.com |Phone: +6285326728933|'
print G+'         +-------------------------+---------------------+'
print G+'\n'

print "Tekan Ctrl+c untuk menghentikan"
time.sleep(0.3)
ini_url = raw_input (B+BL+"[+] Masukan Link Postingan : ")
time.sleep(3)

def Autoclicker(proxy1):
    try:
	proxy = proxy1.split(":")
        print BL+"[+] Proxy", proxy1, "berjalan"
        time.sleep(1)
	proxy_set = urllib2.ProxyHandler({"http" : "%s:%d" % (proxy[0], int(proxy[1]))})
	opener = urllib2.build_opener(proxy_set, urllib2.HTTPHandler)
	opener.addheaders = [('User-agent', random.choice(server)),
						('Refferer', random.choice(site))]
	urllib2.install_opener(opener)
	f = urllib2.urlopen(ini_url)

	if "google.com" in f.read():
	   print G+"[*] Postingan dikunjungi oleh visitor\n"
	else:
	   print R+"[*] Link Gagal Di Kunjungi !\n"
           print R+"[!] Koneksi Gagal\n"
    except :
           print R+"Terimakasih telah menggunakan script ini\nCopyright © 2021\n"
           time.sleep(2)
           os.system('clear')
           sys.exit()
           pass

def loadproxy():
    try:
	get_file = open(proxy_list, "r")
	proxylist = get_file.readlines()
	count = 0
        proxy = []
	while count < len(proxylist):
	      proxy.append(proxylist[count].strip())
	      count += 1
        for i in proxy:
            Autoclicker(i)
    except IOError:
	print B+W+"\n[-] Error : Proxy List Tidak Ada\n"+N
	sys.exit(1)

def main():
   print """
"""+N
   loadproxy()
if __name__ == '__main__':
    main()
os.system('clear')
