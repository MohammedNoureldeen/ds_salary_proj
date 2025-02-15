from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service


PATH = 'C:/Users/3007m/Documents/ds_salary_proj/chromedriver.exe'


l=list()
o={}

target_url = "https://www.glassdoor.com/Job/united-states-data-scientist-jobs-SRCH_IL.0,13_IN1_KO14,28.htm"

service = Service(PATH)

driver=webdriver.Chrome(service=service)

driver.get(target_url)

driver.maximize_window()
time.sleep(2)

resp = driver.page_source
driver.close()

soup=BeautifulSoup(resp,'html.parser')

allJobsContainer = soup.find("ul",{"class":"JobsList_jobsList__lqjTr"})

allJobs = allJobsContainer.find_all("li")

for job in allJobs:
    try:
        o["name-of-company"]=job.find("div",{"class":"EmployerProfile_profileContainer__VjVBX"}).text
    except:
        o["name-of-company"]=None

    try:
        o["name-of-job"]=job.find("a",{"class":"JobCard_jobTitle___7I6y"}).text
    except:
        o["name-of-job"]=None


    try:
        o["location"]=job.find("div",{"class":"JobCard_location__rCz3x"}).text
    except:
        o["location"]=None


    try:
        o["salary"]=job.find("div",{"class":"JobCard_salaryEstimate__arV5J"}).text
    except:
        o["salary"]=None

    l.append(o)

    o={}

print(l)

df = pd.DataFrame(l)
df.to_csv('jobs.csv', index=False, encoding='utf-8')