#setting up files and tasks

import requests
from bs4 import BeautifulSoup

URL = "https://replit.com/community-hub"

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")

cards = soup.find("div", {"class":"css-nghpcj"})


titles = cards.find_all("span", {"class":"css-19l40in"})
dates = cards.find_all("span", {"class":"css-1jm4vlb"})

counter = 0
for title in titles:
    print(title.text)
    for date in dates[counter]:
        print(date.text)
        counter += 1
    print()
    



#TASKS
# 1 Scrape the Replit Community Hub for events and put them into a list.
    #Using BeautifulSoup
    #save to database
# 2 Filter the events by topics that interest you (remember how we filtered news articles from hacker news?)
# 3 Schedule the scrape for every 6 hours.
    #Using Scheduling
# 4 If an event of interest is scraped, email yourself (or a friend) with a hyperlink to the event.
    #Using Gmail
# 5 Only email any new events.