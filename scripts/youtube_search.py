import urllib.request
import urllib.parse
import re

search = "animated card"
youtube_url = "https://www.youtube.com/watch?v="
youtube_search = "https://www.youtube.com/kepowob/search?"
args = input("what ya want?")
params = urllib.parse.urlencode({'query': args}) 
search = f'{youtube_search}{params}'

html = urllib.request.urlopen(search)
content = html.read().decode()
video_ids = re.findall(r"watch\?v=(\S{11})", content)
print(video_ids)

for x in video_ids:
    print(f'{youtube_url}{x}')
