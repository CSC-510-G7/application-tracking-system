# import requests
# from fake_useragent import UserAgent

# user_agent = UserAgent()
# headers = {"User-Agent":
#                    user_agent.random,
#                    "Referrer": "https://www.monster.com/"
#                    }

# stuff = requests.get(url="https://www.monster.com/jobs/search?q=software&where=&page=1&so=m.h.s", headers=headers)
# print(stuff.content)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# def scrape_monster_jobs(url):
#     # Set up Selenium with headless Chrome
#     options = Options()
#     options.add_argument("--headless")  # Run in headless mode (no UI)
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")

#     # Initialize WebDriver
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(options=options)

#     try:
#         # Open the Monster job listings page
#         driver.get(url)
#         time.sleep(5)  # Allow JavaScript to load

#         # Find job postings
#         job_cards = driver.find_elements(By.CLASS_NAME, "job-cardstyle__JobCardComponent-sc-1mbmxes-0")

#         jobs = []
#         for card in job_cards:
#             try:
#                 title = card.find_element(By.CLASS_NAME, "job-cardstyle__JobTitle-sc-1mbmxes-2").text
#                 company = card.find_element(By.CLASS_NAME, "company-name").text
#                 location = card.find_element(By.CLASS_NAME, "job-cardstyle__Location-sc-1mbmxes-6").text
#                 job_link = card.find_element(By.TAG_NAME, "a").get_attribute("href")

#                 jobs.append({"title": title, "company": company, "location": location, "link": job_link})
#             except Exception as e:
#                 print("Error extracting a job:", e)

#         return jobs
#     finally:
#         driver.quit()

# # URL to scrape
# url = "https://www.monster.com/jobs/search?q=software&where=&page=2&so=m.h.s"
# job_data = scrape_monster_jobs(url)

# # Print results
# for job in job_data:
#     print(job)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_monster_jobs(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(5)  # Allow initial load

        # Take a screenshot to check if job postings are visible
        driver.get_screenshot_as_file("monster_screenshot.png")

        # Wait for job listings to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "job-cardstyle__JobCardComponent-sc-1mbmxes-0"))
            )
        except:
            print("Job listings not found. Monster may be blocking the bot.")
            print(driver.page_source)  # Print page source for debugging
            return []

        job_cards = driver.find_elements(By.CLASS_NAME, "job-cardstyle__JobCardComponent-sc-1mbmxes-0")

        jobs = []
        for card in job_cards:
            try:
                title = card.find_element(By.CLASS_NAME, "job-cardstyle__JobTitle-sc-1mbmxes-2").text
                company = card.find_element(By.CLASS_NAME, "company-name").text
                location = card.find_element(By.CLASS_NAME, "job-cardstyle__Location-sc-1mbmxes-6").text
                job_link = card.find_element(By.TAG_NAME, "a").get_attribute("href")

                jobs.append({"title": title, "company": company, "location": location, "link": job_link})
            except Exception as e:
                print("Error extracting a job:", e)

        return jobs
    finally:
        driver.quit()

url = "https://www.monster.com/jobs/search?q=software&where=&page=2&so=m.h.s"
job_data = scrape_monster_jobs(url)

for job in job_data:
    print(job)
