import requests
from bs4 import BeautifulSoup

js =requests.get("https://rubnongkaomai.com/pages-manifest-07f52c14a655550e2770.js")
js= js.text
baan_ls = []
while js.find("/baan/") >0 :
    l = js.find("/baan/")
    r= js[l:].find('"')+ l
    baan_url = js[l:r]
    if(len(baan_url) > len("/baan/")):
        baan_ls.append(baan_url)
    js = js[r:]
webbase_url = "https://rubnongkaomai.com"

for path in baan_ls:
    print(webbase_url+path)
    url = requests.get(webbase_url+path)
    soup = BeautifulSoup(url.content, "html.parser")
    selector="dev.baan-info-module--text-wrapper--uuYTz"
    print(soup.select_one(selector))