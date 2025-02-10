import requests
from bs4 import BeautifulSoup

#print(requests.utils.default_headers())
# URL of the page to scrape
url = "https://www.imdb.com/title/tt7321322/?ref_=fn_all_ttl_4"

# Define the headers with a custom User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

plot = soup.find("span", class_="sc-42125d72-0 gKbnVu")

print(plot.text)

#credits = soup.find("div", class_="sc-70a366cc-3")

# Extract Director
director = soup.select_one('[data-testid="title-pc-principal-credit"] a').text

# Extract Writers
writers = [a.text for a in soup.select('[href*="/fullcredits/?ref_=tt_ov_wr#writer"] ~ div a')]

# Extract Stars
stars = [a.text for a in soup.select('[href*="/fullcredits/?ref_=tt_ov_st#cast"] ~ div a')]


# Print the results
print("Director:", director)
print("Writers:", writers)
print("Stars:", stars)
