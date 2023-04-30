import requests
from bs4 import BeautifulSoup
import re
import random

def img_downloding(url):
    res = requests.get(url)
    beat =BeautifulSoup(res.text,"html.parser")
    links=beat.findAll("img",src=re.compile(".jpg"))
    for j in links:
        link = j.get("src")
        name=random.randrange(1,200)
        with requests.get(link,stream=True)as g:
          with open(str(name)+".jpg","wb") as f:
            for i in g.iter_content(chunk_size=1024):
                f.write(i)
img_downloding("https://music-fa.com/download")

#axhaye to ye site ro dar ovordim 