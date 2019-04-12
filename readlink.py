from BeautifulSoup import BeautifulSoup
import urllib2
import re
links = ['http://rji.augurlabs.io/20170909_MuSc/1q','http://rji.augurlabs.io/20170909_MuSc/2q/','http://rji.augurlabs.io/20170909_MuSc/3q/','http://rji.augurlabs.io/20170909_MuSc/4q/','http://rji.augurlabs.io/20170902_MuMsu/1q/','http://rji.augurlabs.io/20170902_MuMsu/2q/','http://rji.augurlabs.io/20170902_MuMsu/3q/','http://rji.augurlabs.io/20170902_MuMsu/4q/','http://rji.augurlabs.io/Other_stuff/20170119_uglyproduce_LB/','http://rji.augurlabs.io/Other_stuff/20170118_Shooting_EA/']
for i in range(len(links)):
    html_page = urllib2.urlopen(links[i])
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        url = links[i] +'/' +link.get('href')
        if url.endswith('../'):
            pass
        else:
            print url
            filedata = urllib2.urlopen(url)
            datatowrite = filedata.read()

            with open('photos/'+link.get('href'),'wb') as f:
                f.write(datatowrite)
