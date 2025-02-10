# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# def scrape_google_jobs(url):
#     # Set up Selenium with headless Chrome
#     options = Options()
#     options.add_argument("--headless")  # Run in headless mode
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")

#     driver = webdriver.Chrome(options=options)

#     try:
#         driver.get(url)
#         time.sleep(5)  # Allow JavaScript to load

#         # Wait for Google Jobs container to appear
#         try:
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "BjJfJf"))
#             )
#         except:
#             print("Google Jobs section not found.")
#             print(driver.page_source)  # Print HTML for debugging
#             return []

#         # Locate job postings
#         job_cards = driver.find_elements(By.CLASS_NAME, "BjJfJf")

#         jobs = []
#         for card in job_cards:
#             try:
#                 title = card.find_element(By.CLASS_NAME, "mCBkyc").text
#                 company = card.find_element(By.CLASS_NAME, "vNEEBe").text
#                 location = card.find_element(By.CLASS_NAME, "Qk80Jf").text
#                 job_link = card.find_element(By.TAG_NAME, "a").get_attribute("href")

#                 jobs.append({"title": title, "company": company, "location": location, "link": job_link})
#             except Exception as e:
#                 print("Error extracting a job:", e)

#         return jobs
#     finally:
#         driver.quit()

# # Google Jobs search URL (modify as needed)
# url = "https://www.google.com/search?q=software%20engineering%20jobs&oq=software%20engineering%20jobs&gs_lcrp"
# job_data = scrape_google_jobs(url)

# for job in job_data:
#     print(job)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time

def scrape_google_jobs(url):
    # Generate a random User-Agent
    ua = UserAgent()
    user_agent = ua.random

    # Set up Selenium with headless Chrome and fake User-Agent
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(f"user-agent={user_agent}")  # Set random User-Agent

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(5)  # Allow JavaScript to load

        # Wait for Google Jobs container to appear
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "BjJfJf"))
            )
        except:
            print("Google Jobs section not found. Possible CAPTCHA block.")
            print(driver.page_source)  # Print HTML for debugging
            return []

        # Locate job postings
        job_cards = driver.find_elements(By.CLASS_NAME, "BjJfJf")

        jobs = []
        for card in job_cards:
            try:
                title = card.find_element(By.CLASS_NAME, "mCBkyc").text
                company = card.find_element(By.CLASS_NAME, "vNEEBe").text
                location = card.find_element(By.CLASS_NAME, "Qk80Jf").text
                job_link = card.find_element(By.TAG_NAME, "a").get_attribute("href")

                jobs.append({"title": title, "company": company, "location": location, "link": job_link})
            except Exception as e:
                print("Error extracting a job:", e)

        return jobs
    finally:
        driver.quit()

# Google Jobs search URL
url = "https://www.google.com/search?q=software%20engineering%20jobs&oq=software%20engineering%20jobs&gs_lcrp"
job_data = scrape_google_jobs(url)

for job in job_data:
    print(job)
