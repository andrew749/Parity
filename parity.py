import json
import pdb
from urllib.parse import urlencode
from urllib.request import urlopen
import webbrowser
userinput = "placeholder"
muzik_url = "http://muzik-api.herokuapp.com/search?%s"
while( not userinput == ""):
        songname = input("Enter the name of the song to download: ")
        data = urlencode({'songname':songname})
        url = muzik_url % data
        print(url)
        results = urlopen(url).read().decode('utf-8')
        jsonresults = json.loads(results)
        count = 0
        songArray = []
        for result in jsonresults["url"]:
            for key,value in  result.items():
                print ('{}.  Name: {}'.format(count,key))
                print ('      URL: {}'.format(value))
                print('\n')
                songArray.append((key,value))
            count+=1
        userinput_2 = int(input('Select a song to try'))
        while(not userinput_2 == ''):
            webbrowser.open(songArray[userinput_2][1])
            confirmation_input = input('Would you like to save this song?')
            if (confirmation_input == 'yes'):
                f = open(songArray[userinput_2][0], 'w')
                f.write(urlopen(songArray[userinput_2][1]))
                break
            userinput_2 = int(input('Select a song to try'))

