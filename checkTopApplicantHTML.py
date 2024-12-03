# pip install beautifulsoup4

from bs4 import BeautifulSoup

# Load the HTML file
html_file = "TopApplicant.html"  # Replace with the correct path if needed

with open(html_file, "r", encoding="utf-8") as file:
    content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Find all `li` elements with IDs like 'ember...'
li_elements = soup.find_all("li", id=lambda x: x and x.startswith("ember"))

# Loop through each `li` to extract job card content
for li in li_elements:
    try:
        # Check if the `li` contains a blurred job card
        job_card = li.find(class_="blurred-job-card")
        if not job_card:
            continue

        # Extract job posting title
        job_posting_title = job_card.find(class_="blurred-job-card__job-posting-title").get_text(strip=True)

        # Extract primary description
        primary_description = job_card.find(class_="blurred-job-card__primary-description").get_text(strip=True)

        # Extract secondary description
        secondary_description = job_card.find(class_="blurred-job-card__secondary-description").get_text(strip=True)

        # Print the details
        print("Job Posting Title:", job_posting_title)
        print("Primary Description:", primary_description)
        print("Secondary Description:", secondary_description)
        print("-" * 50)
    except AttributeError:
        # Handle cases where expected elements are not found
        continue
