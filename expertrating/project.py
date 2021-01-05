import bs4 as bs
import urllib.request
import pandas as pd
import csv

sauce=urllib.request.urlopen('https://www.antutu.com/en/ranking/rank1.htm').read()
#https://www.antutu.com/en/ranking/rank1.htm
#https://www.antutu.com/en/ranking/ios1.htm
#https://smartphonesrevealed.com/the-best-smartphones/?showall=true
#https://www.dxomark.com/category/mobile-reviews/
soup =bs.BeautifulSoup(sauce,'lxml')
#print(soup.get_text())
#print(soup.find_all('p'))
#print(soup.p)
body=soup.body
flist = []
fin=[]
#
#for paragraph in body.find_all('li'):
#    print (paragraph.text)
#for div in body.find_all('ul', class_="list-unstyled newrank-b"):
#    print(div.text)
##table=soup.table
##print (table)
uls = soup.find_all('ul', class_='list-unstyled newrank-b')
for ul in uls:
    newsoup = bs.BeautifulSoup(str(ul), 'html.parser')
    lis = newsoup.find_all('li')
    for li in lis:
        flist.append(li.text)
for i in range(0,len(flist),6):
   fin.append(flist[i:i+6])
   
with open('android.csv', 'a') as outcsv:
#configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(['Phone', 'CPU','GPU', 'MEM','UX','Total'])
    for item in fin:
    #Write item to outcsv
        writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5]])
    
    sauce=urllib.request.urlopen('https://www.antutu.com/en/ranking/ios1.htm').read()
    #https://www.antutu.com/en/ranking/rank1.htm done
    #https://www.antutu.com/en/ranking/ios1.htm done
    #https://smartphonesrevealed.com/the-best-smartphones/?showall=true
    #https://www.dxomark.com/category/mobile-reviews/ done
    soup =bs.BeautifulSoup(sauce,'lxml')
    #print(soup.get_text())
    #print(soup.find_all('p'))
    #print(soup.p)
    body=soup.body
    flist = []
    fin=[]
    #
    #for paragraph in body.find_all('li'):
    #    print (paragraph.text)W
    #for div in body.find_all('ul', class_="list-unstyled newrank-b"):
    #    print(div.text)
    ##table=soup.table
    ##print (table)
    uls = soup.find_all('ul', class_='list-unstyled newrank-b')
    for ul in uls:
        newsoup = bs.BeautifulSoup(str(ul), 'html.parser')
        lis = newsoup.find_all('li')
        for li in lis:
            flist.append(li.text)
    for i in range(0,len(flist),6):
       fin.append(flist[i:i+6])
       
    with open('ios.csv', 'a') as outcsv:
    #configure writer to write standard csv file
        writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['Phone', 'CPU','GPU', 'MEM','UX','Total'])
        for item in fin:
        #Write item to outcsv
            writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5]])

