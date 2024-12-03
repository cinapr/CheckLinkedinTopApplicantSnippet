#THIS ONE SHOULD WORK BY DIRECTLY CALL THE PAGE INSTEAD OF SAVE FIRST WITH CHROME, BUT IT WON'T SUPPORT DUE TO LOGIN PROMPT OWNED BY LINKEDIN

#pip install selenium
 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configure WebDriver
driver_path = "path/to/chromedriver"  # Replace with the path to your WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open LinkedIn Top Applicant Jobs page
url = "https://www.linkedin.com/jobs/collections/top-applicant"
driver.get(url)

# Wait for the page to load (adjust timeout as necessary)
time.sleep(5)  # Can be replaced with explicit waits for better stability

# Extract all li elements with IDs like 'ember...'
ul_element = driver.find_element(By.TAG_NAME, "ul")
li_elements = ul_element.find_elements(By.TAG_NAME, "li")

# Loop through and extract content from each blurred job card
for li in li_elements:
    try:
        # Check if the li contains a blurred job card
        job_card = li.find_element(By.CLASS_NAME, "blurred-job-card")
        
        # Extract job posting title
        job_posting_title = job_card.find_element(By.CLASS_NAME, "blurred-job-card__job-posting-title").text
        
        # Extract primary description
        primary_description = job_card.find_element(By.CLASS_NAME, "blurred-job-card__primary-description").text
        
        # Extract secondary description
        secondary_description = job_card.find_element(By.CLASS_NAME, "blurred-job-card__secondary-description").text
        
        # Print the details
        print("Job Posting Title:", job_posting_title)
        print("Primary Description:", primary_description)
        print("Secondary Description:", secondary_description)
        print("-" * 50)
    except Exception as e:
        # If no blurred job card is found, skip
        continue

# Close the driver
driver.quit()
