import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


def parse_colors():
    url = 'https://www.computerhope.com'
    response = requests.get(url + '/htmcolor.htm')
    resp_body = BeautifulSoup(response.content, 'html.parser')
    colors_table = resp_body.find('table', {'class': 'nobreak'}).find_all('tr', {'class': 'tcw'})
    colors = {}
    for color in colors_table:
        hex_color = ''
        rgb = ''
        rgb_deep = ''
        rgba = ''
        shadow_rgb = ''
        title_color = color.find('a').text
        if color.find('td', {'class': 'wt'}):
            text_color = color.find('td', {'class': 'wt'}).text
        else:
            text_color = color.find('td', {'class': 'dt'}).text
        if re.search(r'\s', text_color):
            text_color = '-'.join(x.lower() for x in text_color.split(' '))
        else:
            text_color = text_color.lower()
        rgb_numbers = ', '.join(str(x) for x in hex_to_rgb(title_color))
        # rgb_deep_numbers = ', '.join(str(x - 20) if x >= 20 else '0' for x in hex_to_rgb(title_color))
        # hex_color += f'--{text_color.lower()}-hex: {title_color}; \n'
        # rgb += f'--{text_color.lower()}-rgb: rgb({rgb_numbers}); \n'
        # rgb_deep += f'--{text_color.lower()}-rgb-deep: rgb({rgb_deep_numbers}); \n'
        # rgba += f'--{text_color.lower()}-rgba: rgba({rgb_numbers}, .7); \n'
        shadow_rgb += f'--{text_color.lower()}-shadow: 1px 1px 2px rgb({rgb_numbers}); \n'
        with open('hex.csv', 'a') as hex_csv, \
             open('rgb.csv', 'a') as rgb_csv, \
             open('rgb_deep.csv', 'a') as rgb_deep_csv, \
             open('rgba.csv', 'a') as rgba_csv, \
             open('shadows_rgb.csv', 'a') as shadows_rgb_csv:
            # hex_csv.writelines(hex_color)
            # rgb_csv.writelines(rgb)
            # rgb_deep_csv.writelines(rgb_deep)
            # rgba_csv.writelines(rgba)
            shadows_rgb_csv.writelines(shadow_rgb)


def hex_to_rgb(hex_color: str) -> tuple:
    numbers_hex = hex_color.lstrip('#')
    rgb = tuple(int(numbers_hex[i:i + 2], 16) for i in (0, 2, 4))
    return rgb


print(hex_to_rgb('#203730'))
