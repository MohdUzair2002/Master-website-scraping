import requests

cookies = {
    'StudyPortals-trck': '%7B%22ip%22%3A%2243.246.226.56%22%2C%22uuid%22%3A%22cdc06398-70a3-4e58-8048-c7bb91d47b6b%22%2C%22lang%22%3A%22en-GB%22%2C%22origin%22%3A129%2C%22origin_iso%22%3A%22pk%22%2C%22search%22%3Anull%2C%22tap_groups%22%3Anull%2C%22previousPage%22%3A%22https%3A%2F%2Fwww.mastersportal.com%2Fstudies%2F224401%2Finformation-systems.html%3Fref%3Dsearch_card%22%7D',
    'user_nationality_id': '129',
    'user_nationality_iso': 'PK',
    '_sp_ses.b9dd': '*',
    '_sp_id.b9dd': '39da1a32-d42b-4ae1-bebb-f90a73866074.1670051173.1.1670056099.1670051173.9dea7cb9-cf53-46aa-ae51-83f75c79b983',
    'studyportals-cookie': '93b591b4-ff92-413b-9454-edc95fe9b1bc',
    '_fbp': 'fb.1.1670051178918.1665586137',
    '_ga': 'GA1.2.1447504763.1670051182',
    '_gid': 'GA1.2.1515978797.1670051182',
    'recordID': '1f087bde-4305-4f14-a05f-e8f8b6698184',
    '_hjSessionUser_69598': 'eyJpZCI6ImFjZGUwZGZlLTA4ZGEtNTZmNi1hNTMyLTUyMDhkMzY4ZTk5ZCIsImNyZWF0ZWQiOjE2NzAwNTEzMjQ4NjQsImV4aXN0aW5nIjp0cnVlfQ==',
    'g_state': '{"i_p":1670058526141,"i_l":1}',
    '_hjSession_69598': 'eyJpZCI6IjcxMGQ4YzlkLTY0MjItNGRkMi1iYjU3LTYxYzJmYzc1OWM0OCIsImNyZWF0ZWQiOjE2NzAwNTM0MjI1ODMsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '__cf_bm': 'M3HOt4hpFJTvsJ4QUaRCcDLfsyzrqTGlOWMtf1dRvyg-1670056040-0-AYrIPkE04qIdUc5jQk+xj9FE6NExbXqEbny0Zoi3bwt51joR7V/jZwGXIb29sXCdYhXYXfNH7rOOpxckyNQjJO2d0zJnnwr0bLnlZmjBVPipMpDL2fpOrdpRHsH/fVxbZNHNoE89gr6jlX46azyz0hd+9IUcoJRQCrcHtOeLxa10YUMG6G2Vkd8McIp98R68mw==',
    'dmSessionID': 'f0e7878f-6c07-4bbd-a124-f1234426fa43',
    '__gads': 'ID=695b58c0be049b8e:T=1670053768:S=ALNI_MZ92cnOoHMOVYm8ME2lHx7zZQ1OHQ',
    '__gpi': 'UID=00000b88ab48d83c:T=1670053768:RT=1670053768:S=ALNI_Ma_qpxjZX7U3X70Krr7VIYhLiQMSg',
    '_hjIncludedInPageviewSample': '1',
    '_hjIncludedInSessionSample': '0',
    '_hjDonePolls': '837889',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.mastersportal.com/search/master/business-information-systems/united-states?mh=face2face,blended&page=9',
    'Alt-Used': 'www.mastersportal.com',
    'Connection': 'keep-alive',
    'Cookie': 'StudyPortals-trck=%7B%22ip%22%3A%2243.246.226.56%22%2C%22uuid%22%3A%22cdc06398-70a3-4e58-8048-c7bb91d47b6b%22%2C%22lang%22%3A%22en-GB%22%2C%22origin%22%3A129%2C%22origin_iso%22%3A%22pk%22%2C%22search%22%3Anull%2C%22tap_groups%22%3Anull%2C%22previousPage%22%3A%22https%3A%2F%2Fwww.mastersportal.com%2Fstudies%2F224401%2Finformation-systems.html%3Fref%3Dsearch_card%22%7D; user_nationality_id=129; user_nationality_iso=PK; _sp_ses.b9dd=*; _sp_id.b9dd=39da1a32-d42b-4ae1-bebb-f90a73866074.1670051173.1.1670056099.1670051173.9dea7cb9-cf53-46aa-ae51-83f75c79b983; studyportals-cookie=93b591b4-ff92-413b-9454-edc95fe9b1bc; _fbp=fb.1.1670051178918.1665586137; _ga=GA1.2.1447504763.1670051182; _gid=GA1.2.1515978797.1670051182; recordID=1f087bde-4305-4f14-a05f-e8f8b6698184; _hjSessionUser_69598=eyJpZCI6ImFjZGUwZGZlLTA4ZGEtNTZmNi1hNTMyLTUyMDhkMzY4ZTk5ZCIsImNyZWF0ZWQiOjE2NzAwNTEzMjQ4NjQsImV4aXN0aW5nIjp0cnVlfQ==; g_state={"i_p":1670058526141,"i_l":1}; _hjSession_69598=eyJpZCI6IjcxMGQ4YzlkLTY0MjItNGRkMi1iYjU3LTYxYzJmYzc1OWM0OCIsImNyZWF0ZWQiOjE2NzAwNTM0MjI1ODMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __cf_bm=M3HOt4hpFJTvsJ4QUaRCcDLfsyzrqTGlOWMtf1dRvyg-1670056040-0-AYrIPkE04qIdUc5jQk+xj9FE6NExbXqEbny0Zoi3bwt51joR7V/jZwGXIb29sXCdYhXYXfNH7rOOpxckyNQjJO2d0zJnnwr0bLnlZmjBVPipMpDL2fpOrdpRHsH/fVxbZNHNoE89gr6jlX46azyz0hd+9IUcoJRQCrcHtOeLxa10YUMG6G2Vkd8McIp98R68mw==; dmSessionID=f0e7878f-6c07-4bbd-a124-f1234426fa43; __gads=ID=695b58c0be049b8e:T=1670053768:S=ALNI_MZ92cnOoHMOVYm8ME2lHx7zZQ1OHQ; __gpi=UID=00000b88ab48d83c:T=1670053768:RT=1670053768:S=ALNI_Ma_qpxjZX7U3X70Krr7VIYhLiQMSg; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample=0; _hjDonePolls=837889',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'If-Modified-Since': 'Sat, 03 Dec 2022 08:17:08 GMT',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'ref': 'search_card',
}

response = requests.get(
    'https://www.mastersportal.com/studies/224401/information-systems.html',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.json())
