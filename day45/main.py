import requests as req
from bs4 import BeautifulSoup

# with open(file="website.html", mode="r") as fh:
#     contents = fh.read()
#
#
# print(f"{contents}")

response = req.get(url="https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, 'html.parser')

all_a_tags = soup.find_all('a', class_='titlelink')

all_up_votes_tags = [int(s.getText().split(" ")[0]) for s in soup.find_all('span', class_='score')]

max_index = all_up_votes_tags.index(max(all_up_votes_tags))

print(f"Title: {all_a_tags[max_index].text}\nHREF: {all_a_tags[max_index].get('href')}\nScore: {all_up_votes_tags[max_index]}")


# TODO: top 100 movies
response = req.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, 'html.parser')

all_title_tags = soup.find_all('h3', class_='title')

titles = []
for x in range(len(all_title_tags)-1, -1, -1):
    titles.append(all_title_tags[x].getText())


# write to file
with open(file="top_100_movie_titles.txt", mode="w") as fh:
    for x in range(len(titles)):
        fh.write(f"{titles[x]}\n")


print(f"Done :-0)")