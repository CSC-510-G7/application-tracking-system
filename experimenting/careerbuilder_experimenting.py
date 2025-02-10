# import requests
# from fake_useragent import UserAgent

# user_agent = UserAgent()
# headers = {"User-Agent": user_agent.random,
#            "Referrer": "https://www.careerbuilder.com/"
#            }

# stuff = requests.get(url="https://www.careerbuilder.com/jobs?company_request=false&company_name=&company_id=&keywords=software+engineer&location=Chicago%2C+IL", headers=headers)
# print(stuff.content)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
import time

def scrape_careerbuilder_jobs(url):
    # Generate a random User-Agent to evade bot detection
    ua = UserAgent()
    user_agent = ua.random

    # Set up Selenium with headless Chrome
    options = Options()
    options.add_argument("--headless")  # Run headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(f"user-agent={user_agent}")  # Fake User-Agent

    driver = webdriver.Chrome(options=options)

    
    driver.get(url)
    time.sleep(5)  # Allow JavaScript to load

    # Wait for job postings to load
    WebDriverWait(driver, 10)
    print(driver.page_source)
    driver.quit()

# CareerBuilder jobs search URL
url = "https://www.careerbuilder.com/jobs?company_request=false&company_name=&company_id=&keywords=software+engineer&location=Chicago%2C+IL"
scrape_careerbuilder_jobs(url)
