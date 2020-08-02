import csv
import requests
from bs4 import BeautifulSoup

def format_date(date):
    return str(date) if date > 9 else '0'+str(date)

def extract_temperatures_into_csv_file():
    """Scrape the website to get the temperatures for the last 10 years
        and put it into a csv file"""

    URL = 'https://www.historique-meteo.net/france/aquitaine/bordeaux/'
    days = range(1, 32)
    months = range(1, 13)
    years = range(2009, 2020)
    temperatures = {}

    for year in years:
        for month in months:
            for day in days:
                if month in [1, 3, 5, 7, 9, 11]:
                    if day == 31:
                        pass
                if month == 2:
                    if day >= 28:
                        pass
                
                date = str(year) + '/' + format_date(month) + '/' + format_date(day)
                query_url = URL + date

                html_body = requests.get(query_url).text
                scrapper = BeautifulSoup(html_body, 'html.parser')
                css_selector = '#content table tr:nth-child(1) > td.text-center.bg-primary > b'

                element = scrapper.select_one(css_selector)

                if element is not None:
                    value = element.text
                    temperature = int(value[0:len(value) - 1])
                    temperatures[date] = temperature
        
    with open('files/data/temperatures-bordeaux-2009-2019.csv', 'w') as file:
        fieldnames = ['date', 'temperature']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for date, temperature in temperatures.items():
            writer.writerow({'date': date, 'temperature': str(temperature)})        

