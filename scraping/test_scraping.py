import requests
from bs4 import BeautifulSoup

#print(requests.utils.default_headers())
# URL of the page to scrape
url = "https://www.imdb.com/find/?q=spider man"

# Define the headers with a custom User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Find the <ul> with class 'ipc-metadata-list'
ul = soup.find("ul", class_="ipc-metadata-list")

if ul:
    search_match = []
    # Loop through all/parent only <li> elements within the <ul>
    for li in ul.find_all("li", recursive=False): # recursive=False ensures child <li> within the root <li> are not returned
        movie_info = {}

        # get posture src
        img = li.find('img')
        #src = img.get('src') # src have low resolution image so get img url from 'srcset'
        img_url = img.get('srcset').split(' ')[-2]
        movie_info['img_url'] = img_url

        # get title
        element_a = li.find("a", class_='ipc-metadata-list-summary-item__t')
        title = element_a.text
        movie_info['title'] = title

        # get link for the movie detail
        detail_link = element_a.get('href')
        movie_info['detail_url'] = detail_link

        # get release time and actors name
        #time_and_stars = li.find_all("li", class_="ipc-inline-list__item")
        time_and_stars = [_li.text for _li in li.find_all("li", class_="ipc-inline-list__item")]
        release_date = time_and_stars[0]
        stars = time_and_stars[-1]
        movie_info['release_date'] = release_date
        movie_info['stars'] = stars
        
        search_match.append(movie_info)

    print(search_match)
else:
    print("Could not find the <ul> with the specified class.")