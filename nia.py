import requests
import time
import bs4 
from datetime import datetime
from datetime import timedelta
import os
import re 


today = datetime.now()
diff = timedelta(days=7)
base_date = today - diff

def slack_post_text(url, text):
    result = requests.post(url, json = {"text": text})
    # {"username": "new-bot-name"}
    return result

def clean_text(text):
    return " ".join(text.split())

def eliminate_not_essential(text):
    results = text.replace('첨부파일 있음', '')
    results = results.replace('new', '')
    return results
url = os.environ.get('SLACK_URL')

req = requests.get('https://www.nia.or.kr/site/nia_kor/ex/bbs/List.do?cbIdx=78336')
soup = bs4.BeautifulSoup(req.text, 'html.parser')


matches = []
titles = soup.select('span.subject.searchItem')
dates = soup.select('span.src em:nth-child(1)')

def date_preprocess(dates):    
    for date in dates:
        results = ''.join(date.text.replace('.', '-'))
    return results

# print(date_preprocess(dates))

for date, title in zip(dates, titles):

    date = datetime.strptime(date.text.replace('.', '-'), "%Y-%m-%d")
    if (date > base_date) and ('[입찰공고]' in title.text.strip() or '[추경]' in title.text.strip()):
            matches.append(f'{date.strftime("%Y-%m-%d")} : {clean_text(eliminate_not_essential(title.text.strip()))}')


if matches:
    contents = '------------------------------------------------------------------------ \n 최근 올라온 정보화진흥원 공고가 있습니다. \n\n'

    contents += '\n'.join(matches)
    print(contents)
    slack_post_text(url, contents)