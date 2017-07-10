from urllib.request import *
from bs4 import BeautifulSoup
import mlab
from song import Song


mlab.connect()

url="http://mp3zing.mobi/playlist-bang-xep-hang/Au-My/IWZ9Z0BW.html"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding': 'none',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive'}

request = Request(url)

for key, value in hdr.items():
    request.add_header(key, value)

html_content = urlopen(request).read().decode("utf-8")

soup = BeautifulSoup(html_content, "html.parser")

# find, find_all
div_playlist = soup.find("div", "mediatec-cleanaudioplayer")

li_list = div_playlist.ul.find_all("li")

# Xóa dữ liệu cũ:
Song.drop_collection()

for li_song in li_list:
    title = li_song["data-title"]
    artist = li_song["data-artist"]
    url = li_song["data-url"]
    print("Saving ", title)
    song = Song(artist = artist,
                title = title,
                url = url)
    song.save()





