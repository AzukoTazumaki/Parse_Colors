import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.computerhope.com'
response = requests.get(url + '/htmcolor.htm')

resp_body = BeautifulSoup(response.content, 'html.parser')
colors_table = resp_body.find('table', {'class': 'nobreak'}).find_all('tr', {'class': 'tcw'})

colors = {}

for color in colors_table:
    color_line = ''
    color_shadow = ''
    title_color = color.find('a').text
    if color.find('td', {'class': 'wt'}):
        text_color = color.find('td', {'class': 'wt'}).text
    else:
        text_color = color.find('td', {'class': 'dt'}).text
    if re.search(r'\s', text_color):
        text_color = '-'.join(x.lower() for x in text_color.split(' '))
    else:
        text_color = text_color.lower()
    color_line += f'--{text_color.lower()}: {title_color}; \n'
    color_shadow += f'--{text_color.lower()}-shadow: 1px 1px 3px {title_color}; \n'
    with open('colors.csv', 'a') as fd:
        fd.writelines(color_line)
    with open('colors_shadow.csv', 'a') as fd:
        fd.writelines(color_shadow)
