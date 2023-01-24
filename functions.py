import requests
from bs4 import BeautifulSoup
import schedule, time, os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from replit import db

#there is no error handling included


def email_sending(title, date):
        
    password = os.environ['app_password']
    username = os.environ['email']
    
    email = f"ALERT! New event at Replit. {title} will happen on {date}! Check webpage for further info. Code long and prosper!"
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
    print("Email has been sent")
    del message

        

def save_new_item_in_database(title, date):

    #Note that possibility of using same event name on different date has been ignored in this code
    
    keys = db.keys()
    if title not in keys:
        db[title] = {"date": date}
        email_sending(title, date)
    else:
        print("Not a new event. (I should tell the time as well)")



def web_crawler():
    print("Crawling started")
    print()
    URL = "https://replit.com/community-hub"
    
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    
    #cards picks up the part of the page code where wanted titles and dates are
    #titles and dates alone also pick other announcements
    cards = soup.find("div", {"class":"css-nghpcj"})
    titles = cards.find_all("span", {"class":"css-19l40in"})
    dates = cards.find_all("span", {"class":"css-1jm4vlb"})

    
    counter = 0
    for title in titles:
        
        #Note that this is still printing in console and might not be necessary later
        
        print(title.text)
        for date in dates[counter]:
            print(date.text)
            counter += 1
        save_new_item_in_database(title.text, date.text)
        print()
