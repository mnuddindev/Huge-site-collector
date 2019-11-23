import requests as r
from bs4 import BeautifulSoup
import os
import socket

class tcolor:
    green = '\33[32m'
    red = '\33[31m'

list = open("list.txt", "a+")
ip = open("ip.txt", "a+")
iprang = open("iprange.txt", "a+")
fr = open("Final_Result.txt", "a+")

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }


def collect():
    print("[+] Started Successfully")
    page = 1
    dork = input(" |  Enter Your Dork: ")
    paged = int(input(" |  Enter Page number: "))

    for k in range(0, paged):
        url = "https://www.bing.com/search?q="+dork+"&first="+str(page)+"&FORM=PORE"
        page += 10

        print(" |  Searching with Your details")

        print(" |  Testing is Search Engine Result Page is Online")

        test = r.get(url, headers=headers)
        soup = BeautifulSoup(test.text, 'html.parser')


        fr = soup.find("ol", {
            "id": "b_results"
            })

        fl = fr.find_all('li', {
            "class": "b_algo"
            })

        print(" |  Finding the Site\'s URL from the source")

        fa = []

        for links in fl:
            h_link = links.find('a').attrs['href']
            fa.append(h_link)

        for domains in fa:
            domains = domains.split('/')
            domains = domains[0]+'//'+domains[2]
            list.write(domains+'\n')
            print("[>] "+domains)

    ########list.close()
def domainToip():
    list.seek(0)
    m = list.read()
    sitelist = m.split('\n')
    print("[+] Reading Lsit.txt to get all the domain")
    for dname in sitelist:
        if(dname == ""):
            continue
        dm = dname.split('/')
        print("[!] Getting Ip\'s and trying to print...")
        try:
            data = socket.gethostbyname(dm[2])
        except socket.gaierror:
            pass
        else:
            address = repr(data)
            addr = address.replace("'", "")
            ip.write(addr+"\n")
            print(" |  "+dm[2]+"==>"+addr)

def iprange():
    ip.seek(0)
    b = ip.read()
    print("[+] Reading ip\'s to generate Ip Range")
    for ipr in b:
        if (ipr == ""):
            continue
        ips = b.split(".")
        ipc = ips[0]+"."+ips[1]+"."+ips[2]+"."
        for q in range(0, 256):
            ipm = ipc+str(q)
            iprange = str(ipm)
            iprang.write(iprange+"\n")


def ril():
    iprang.seek(0)
    z = iprang.read()
    m = z.split('\n')
    for sit in m:
        if(sit == ""):
            continue
        url1 = "http://reverseip.domaintools.com/search/?q="+sit
        htm = r.get(url1, headers=headers).text

        sop = BeautifulSoup(htm, 'html.parser')
        c = sop.find_all('span', attrs={'title': sit})
   
        for y in c:
            sname = y.get_text()
            fr.write("http://"+sname+"\n")


def mass():
    collect()
    domainToip()
    iprange()
    ril()
    print("[—————–] Script Finished Successfully.Check list.txt")

mass()
