import requests
import json
import os
from bs4 import BeautifulSoup

req = requests.get('https://maple.gg/u/Chamdarae')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

level = soup.select('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)')[0].string
level = level.split('(')[0]
popular = soup.select('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(4) > span:nth-child(2)')[0].string
mureung_floor = soup.select('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(1) > section > div > div > div > h1')[0].string
mureung_time = soup.select('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(1) > section > div > div > div > small')[0].string
guild = soup.select('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div:nth-child(1) > a')[0].string
ranking = soup.select('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div:nth-child(2) > span')[0].string
rank_world = soup.select('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div:nth-child(3) > span')[0].string
rank_world_job = soup.select('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div:nth-child(4) > span')[0].string
rank_job = soup.select('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div:nth-child(5) > span')[0].string
union_tier = soup.select('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div > div')[0].string
union_level = soup.select('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div > span')[0].string

data = {
    "level" : level,
    "popular" : popular,
    "guild" : guild,
    "mureung_floor" : mureung_floor,
    "mureung_time" : mureung_time,
    "rank_world" : rank_world,
    "rank_world_job" : rank_world_job,
    "rank_job" : rank_job,
    "union_tier" :union_tier,
    "union_level" :union_level
}

try:
    os.remove('data.json')
except:
    print('파일 없음')

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)