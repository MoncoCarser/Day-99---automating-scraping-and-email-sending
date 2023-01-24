import requests
from bs4 import BeautifulSoup
import schedule, time, os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEtext



def web_crawler():
    URL = "https://replit.com/community-hub"
    
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    
    #Cards picks up the part of the page code where wanted titles and dates are
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


def email_sending():
    
    password = os.environ['app_password']
    username = os.environ['email']
    
    email = pass # to be added - any new addition web crawler finds
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    message = MIMEMultipart()
    message["to"] = username
    message["from"] = "Monco C."
    message["subject"] = "New event"
    message.attach(MIMEText(email, "html"))

    s.send_message(message)
    del message


def combined_function()
    pass