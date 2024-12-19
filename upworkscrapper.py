# import requests
# from bs4 import BeautifulSoup
# # from upworkstore import 
# search_term=input("What do you want to search job for\n").lower()
# url = f'https://www.upwork.com/nx/search/talent/?nbs=1&q={search_term}'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(response.content)
# jobs=[]
# job_listing=soup.find_all('section',class_="flex-1 section")
# print(len(job_listing))

import requests
from bs4 import BeautifulSoup
from upworkstore import insert_job_data
search_term = input("Enter job search term: ").lower()
url = f'https://www.upwork.com/nx/search/jobs/?nbs=1&q={search_term}'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
job_listings = soup.find_all('section', class_='flex-1 section')
if len(job_listings)<1:
  print(f"No jobs found for {search_term}")

fetched_job=[]

for job in job_listings:
  job_title_elem = job.find('article', class_='job-titlecursor-pointer px-md-4 air3-card-list px-4x visited')
  job_title = job_title_elem.text.strip() if job_title_elem else "No title"

  location_elem = job.find('li')
  location = location_elem.text.strip() if location_elem else "location"

  job_duration_elem = job_duration.find('div',class_='air3-icon md')
  job_duration = job_duration_elem.text.strip() if job_duration_elem else "Not available"

  salary_elem = job.find('p',class_='m-0')
  salary = salary_elem.text.strip() if salary_elem else "Not available"

  experience_elem=job.find('div',class_='air3-icon md')
  experience=experience_elem.text.strip() if experience_elem else "No experience required."
  
  data={"Job_title":job_title,"Location":location,"Duration":job_duration,"Salary":salary}
  insert_job_data(job_title, experience, job_duration, salary, location)

# data={"Job_title":job_title}
# insert_job_data(job_title)