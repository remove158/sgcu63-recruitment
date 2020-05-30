import requests
from bs4 import BeautifulSoup
import codecs

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
detail= []
for path in baan_ls:
    url = requests.get(webbase_url+path)
    soup = BeautifulSoup(url.content, "html.parser")
    
    detail.append([soup.find("h1").text,soup.find("h3").text])
    print("added url : " + webbase_url+path )



f = codecs.open("table.html", "w", "utf-8")
message = '''<html>
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">         
  <table class="table table-hover">
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>

      </tr>
    </thead> <tbody>'''

for a,b in detail:
    message+= '<tr><td>' + a + '</td><td>' + b + "</td></tr>"
    
    
message += '''</tbody>
  </table>
</div>

</body>
</html>'''

f.write(message)
f.close()
