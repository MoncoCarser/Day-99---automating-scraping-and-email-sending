#setting up files and tasks

    
import schedule, time

schedule.every(5).minutes.do(combined_function)

#TASKS
# 1 Scrape the Replit Community Hub for events and put them into a list. ok
    #Using BeautifulSoup ok
    #save to database
# 2 Filter the events by topics that interest you (remember how we filtered news articles from hacker news?)  pass
# 3 Schedule the scrape for every 6 hours. ok (5min for testing)
    #Using Scheduling ok
# 4 If an event of interest is scraped, email yourself (or a friend) with a hyperlink to the event.
    #Using Gmail ok
    #save password etc in Secrets ok
# 5 Only email any new events.