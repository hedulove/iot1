#https://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search/28487500#28487500
#Python - Download Images from google Image search?
#RUNS WITH PYTHON3

from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os
import http.cookiejar
import json

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

counterx = 0
query = input("Enter the topic to download images > ")# you can change the query for the image  here
image_type="ActiOn"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print (url)
print ("Downloading images, please wait ...")
#add the directory for your image here
DIR="Pictures"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print  ("There are total" , len(ActualImages),"images")

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
###print images
for i , (img , Type) in enumerate( ActualImages):
    try:
        #print("1")
        req = urllib.request.Request(img, headers={'User-Agent' : header})
        #print(req)
        #print("2")
        #raw_img = urllib.request.urlopen(str(req)).read()
        counterx = counterx + 1
        print("Image ", str(counterx) ," of ", len(ActualImages))
        print("                  Reading..." + str(img))
        raw_img = urllib.request.urlopen(str(img)).read()
        #print("3")
        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        #print("4")		
        #print (str(cntr))
        #print("5")
        if len(Type)==0:
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
        else :
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')

        #print("6")
        f.write(raw_img)
        #print("7")		
        f.close()
    except Exception as e:
        print ("******************Could not load : "+str(img))
        print (e)

Print ("End")