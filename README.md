# Check LinkedIn Top Applicant Snippets
Python script to check in which job you are top applicant. 
Usually it is hidden in : [LinkedIn Top Applicant Jobs](https://www.linkedin.com/jobs/collections/top-applicant)

This script processes a LinkedIn job collection HTML file to extract job posting details such as the job title, company name, and location.


## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/cinapr/CheckLinkedinTopApplicantSnippet.git
   ```
   
2. **Install Required Library**:
   ```bash
  pip install beautifulsoup4
   
  

  

## Get the Top Applicant File from LinkedIn
1. Open this link with Chrome: [LinkedIn Top Applicant Jobs](https://www.linkedin.com/jobs/collections/top-applicant)
2. Log in to your LinkedIn account, if prompted.
3. Save the page:
  1. Use the shortcut Ctrl+S in Chrome to save the webpage.
  2. You will get two files: one folder and one HTML file.
4. Ignore the folder; you can delete it. The script only requires the HTML file.

  

## Get the Top Applicant File from LinkedIn
1. Run the Script to Get the List
2. Place the saved HTML file into the folder of the cloned repository.
3. Run the script:
  ```bash
  python checkTopApplicantHTML.py
