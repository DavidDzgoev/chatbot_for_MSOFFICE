import requests
from bs4 import BeautifulSoup


def get_current_dollar():
    forex_dollar = requests.get('https://www.finam.ru/quote/forex/usd-rub/')
    dollar_soup = BeautifulSoup(forex_dollar.text, 'html.parser')
    current_dollar = dollar_soup.find("span", class_="PriceInformation__price--26G").text
    return f'1 USD = {current_dollar} RUB'


def get_current_euro():
    forex_euro = requests.get('https://www.finam.ru/quote/forex/eur-rub/')
    euro_soup = BeautifulSoup(forex_euro.text, 'html.parser')
    current_euro = euro_soup.find("span", class_="PriceInformation__price--26G").text
    return f'1 EUR = {current_euro} RUB'