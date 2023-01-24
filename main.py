import functions
import schedule, time
from replit import db



def combined_function():
    functions.web_crawler()

schedule.every(60).seconds.do(combined_function)

while True:
    schedule.run_pending()
    time.sleep(1)
