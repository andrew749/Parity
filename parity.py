import json
import pdb
from urllib.parse import urlencode
from urllib.request import urlopen
userinput = "placeholder"
muzik_url = "http://muzik-api.herokuapp.com/search?%s"
while( not userinput == ""):
        songname = input("Enter the name of the song to download: ")
        data = urlencode({'songname':songname})
        url = muzik_url % data
        print(url)
        results = urlopen(url).read().decode('utf-8')
        pdb.set_trace()
        jsonresults = json.loads(results)
        pdb.set_trace()
