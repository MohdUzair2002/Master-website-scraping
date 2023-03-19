import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import csv
main_data=[]
pre_main_data=[]
di_codes1=[330,279,281,282,108,331,329]
length_computer_sci=[1001,647,3436,1658,2008,898,1404]
di_codes2=[45,1234]
length_business_adminstration=[4814,1358]
id_l=[]
program_l=[]
university_name_l=[]
state_l=[]
city_l=[]
fulltime_l=[]
parttime_l=[]
on_campus_l=[]
tution_l=[]
online_l=[]
duration_l=[]
apply_date_l=[]
start_date_l=[]
about_l=[]
i=0
while(i<len(di_codes1)):
    limit=((length_computer_sci[i])/20)+1
  
    j=0
    f=0
    while(j<limit):
        # j+=1
        headers= {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://www.mastersportal.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.mastersportal.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            # 'If-None-Match': 'W/"3b00-BOSSGp6FMbeK/YCkCFPACO4iFIM"',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }
       
        response = requests.get(
            f'https://search.prtl.co/2018-07-23/?q=en-703|mh-face2face,blended|di-{di_codes1[i]}|ci-82|lv-master|uc-129|tc-EUR&size=20&start={f}',
            headers=headers,
        )
        #https://search.prtl.co/2018-07-23/?q=en-3877|mh-face2face,blended|di-45|ci-82|lv-master|uc-129|tc-EUR&size=20&start=0
        json_data=response.json()
        for data in json_data:
            id=data['id']
            program=data['title']
            try:
             university_name=data['organisation']
            except:
                university_name="NA"
            state=data['venues'][0]['area']
            city=data['venues'][0]['city']
            fulltime=data['density']['fulltime']
            parttime=data['density']['parttime']
            id_l.append(id)
            state_l.append(state)
            program_l.append(program)
            university_name_l.append(university_name)
            city_l.append(city)
            fulltime_l.append(fulltime)
            parttime_l.append(parttime)
            print(id,state,program,university_name,city,fulltime,parttime)
           
        j+=1
        f+=20
        print(j)
    i+=1
    print(i)
i=0
while(i<length_business_adminstration):
    j=0
    limit=((length_business_adminstration[i])/20)+1
    f=0
    while(j<limit):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://www.mastersportal.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.mastersportal.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'If-None-Match': 'W/4bcf-+7kTszv5KjIqLQbFUspf31F4kcE',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        response = requests.get(
            f'https://search.prtl.co/2018-07-23/?q=en-3877|mh-face2face,blended|di-{di_codes2[i]}|ci-82|lv-master|uc-129|tc-EUR&size=20&start={f}',
            headers=headers,
        )
        # print(response)
        json_data1=response.json()
        for data1 in json_data1:
            id1=data1['id']
            program1=data1['title']
            try:
             university_name1=data1['organisation']
            except:
                university_name1='NA'
            state1=data1['venues'][0]['area']
            city1=data1['venues'][0]['city']
            fulltime1=data1['density']['fulltime']
            parttime1=data1['density']['parttime']
            id_l.append(id1)
            state_l.append(state1)
            program_l.append(program1)
            university_name_l.append(university_name1)
            city_l.append(city1)
            fulltime_l.append(fulltime1)
            parttime_l.append(parttime1)
            print(id1,state1,program1,university_name1,city1,fulltime1,parttime1)
        j+=1
        f+=20
    i+=1
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)
i=0
while(i<len(id_l)):
    url=f'https://www.mastersportal.com/studies/{id_l[i]}/{program_l[i]}.html?ref=search_card'
    driver.get(url)
    on_campus = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='Tag']")))
    on_campus=driver.find_elements(By.XPATH,"//span[@class='Tag']")[1]
    print(on_campus.text)
    on_campus_l.append(on_campus.text)
    online=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='Tag']")))
    online=driver.find_elements(By.XPATH,"//span[@class='Tag']")[2]
    print(online.text)
    online_l.append(online.text)
    duration=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='js-duration']")))
    duration=driver.find_element(By.XPATH,"//span[@class='js-duration']")
    print(duration.text)
    duration_l.append(duration.text)
    tution=driver.find_element(By.XPATH,"//div[@class='TuitionFeeContainer']")
    print(tution.text)
    tution_l.append(tution.text)
    apply_date=driver.find_elements(By.XPATH,"//div[@class='TimingContainer']")[0]
    print(apply_date.text)
    apply_date_l.append(apply_date.text)
    start_date=driver.find_elements(By.XPATH,"//div[@class='TimingContainer']")[1]
    print(start_date.text)
    start_date_l.append(start_date.text)
    about=wait.until(EC.element_to_be_clickable((By.XPATH,"//section[@id='StudySummary']")))
    about=driver.find_element(By.XPATH,"//section[@id='StudySummary']")
    about_l.append(about.text)
    i=i+1
g=0
while(g<len(id_l)):
    pre_main_data.append(university_name(g))
    pre_main_data.append(program_l(g))
    pre_main_data.append(state_l(g))
    pre_main_data.append(city_l(g))
    pre_main_data.append(on_campus_l(g))
    pre_main_data.append(online_l(g))
    pre_main_data.append(fulltime_l(g))
    pre_main_data.append(parttime_l(g))
    pre_main_data.append(duration_l(g))
    pre_main_data.append(tution_l(g))
    pre_main_data.append(apply_date_l(g))
    pre_main_data.append(start_date_l(g))
    pre_main_data.append(about_l(g))
    main_data.append(pre_main_data)
    g+=1
header = ['University Name',' Program','State','City','Oncampus','Online','Full time','Part time','Duration','Tution Fee','Apply Date','Start Date','About/Overview']
with open(f'{data}.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(main_data)   

# id_l=[]
# program_l=[]
# university_name_l=[]
# state_l=[]
# city_l=[]
# fulltime_l=[]
# parttime_l=[]
# on_campus_l=[]
# tution_l=[]
# online_l=[]
# duration_l=[]
# apply_date_l=[]
# start_date_l=[]