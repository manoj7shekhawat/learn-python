import requests as req
from bs4 import BeautifulSoup
from spotify import SpotifyClient

date = input("In which year you want to travel. Please enter in YYYY-MM-DD: ")
response = req.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")

soup = BeautifulSoup(response.text, 'html.parser')

title_list = [item.getText().strip() for item in
              soup.find_all("h3", id='title-of-a-story', attrs={"class": "lrv-u-font-size-16"})]

sc = SpotifyClient()
json_response = sc.get_user()
print(f"{json_response}")

year = date.split("-")[0]
print(f"{year}")

p_id = sc.create_playlist(date)

print(f"{len(title_list)}")

for item in title_list:
    print(f"{item}")
    uris = sc.get_song_uri_api(item, year)
    if uris:
        snapshot_id = sc.add_song_to_playlist(p_id, uris)
        print(f"{snapshot_id}")
    else:
        print("Song missing in Spotify")

print("Done, Verify your playlist in spotify.")