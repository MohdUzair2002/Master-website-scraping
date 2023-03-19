import requests      
di_codes1=[330,279,281,282,108,331,329]
id=0
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
            f'https://search.prtl.co/2018-07-23/?q=en-703|mh-face2face,blended|di-330|ci-82|lv-master|uc-129|tc-EUR&size=20&start=100',
            headers=headers,
        )
        #https://search.prtl.co/2018-07-23/?q=en-3877|mh-face2face,blended|di-45|ci-82|lv-master|uc-129|tc-EUR&size=20&start=0
json_data=response.json()
print(response)
print(json_data)
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
            # id_l.append(id)
            # state_l.append(state)
            # program_l.append(program)
            # university_name_l.append(university_name)
            # city_l.append(city)
            # fulltime_l.append(fulltime)
            # parttime_l.append(parttime)
            print(id,state,program,university_name,city,fulltime,parttime)
            id=id+1
            print(id)