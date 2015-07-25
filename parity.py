import json
import pdb
from urllib.parse import urlencode
from urllib.request import urlopen
userinput = "placeholder"
muzik_url = "http://muzik-api.herokuapp.com/search?%s"
while( not userinput == ""):
        songname = input("Enter the name of the song to download: ")
        data = urlencode({'songname':songname})
        data = data.encode('utf-8')
        url = muzik_url % data
        results = urlopen(url).read()
        jsonresults = json.loads(results)
        pdb.set_trace()
