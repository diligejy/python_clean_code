import requests
import time
import bs4 
from datetime import datetime
from datetime import timedelta
import os


today = datetime.now()
diff = timedelta(days=7)
base_date = today - diff

def slack_post_text(url, text):
    result = requests.post(url, json = {"text": text})
    # {"username": "new-bot-name"}
    return result

def clean_text(text):
    text = text.replace('새글','')
    return " ".join(text.split())

url = os.environ.get('SLACK_URL')

req = requests.get('https://www.nipa.kr/main/selectBbsNttList.do?bbsNo=2&key=122')
soup = bs4.BeautifulSoup(req.text, 'html.parser')



matches = []
elems = soup.select('td.p-subject a')
# elems = driver.find_elements_by_xpath("//td[@class='p-subject']/a")

dates = soup.select('#contents div table tbody tr td time')

# dates = driver.find_elements_by_xpath('//*[@id="contents"]/div/table/tbody/tr/td/time')


for date, elem in zip(dates, elems):
    d = datetime.strptime(date["datetime"], "%Y-%m-%d")
    if d > base_date:
        matches.append(f'{date.text.strip()} : {clean_text(elem.text.strip())}')


if matches:
    contents = '최근 올라온 정보통신산업진흥원 공고가 있습니다. \n\n'

    contents += '\n'.join(matches)
    print(contents)
    #slack_post_text(url, contents)