import requests
from bs4 import BeautifulSoup
import time

def retry(func):
    def _wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            time.sleep(0.25)
            func(*args, **kwargs)
    return _wrapper

class ConvecterCurrency():
    """
    Это класс Миксина для множественного наследования.
    Будет использоваться для преобразования зарплаты из
    других валют в рубли.

    В данном случае используем парсинг html страницы.
    """

    # CurrencyUSDRUB = 0
    # CurrencyEURRUB = 0
    __headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.2.625 Yowser/2.5 Safari/537.36'

    def __init__(self):
        self.CurrencyUSDRUB = 0
        self.CurrencyEURRUB = 0

    @retry
    # @property
    def get_USDRUB(self) -> float:

        if self.CurrencyUSDRUB == 0:
            dollar_rub = 'https://www.banki.ru/products/currency/usd/'
            full_page = requests.get(dollar_rub, self.__headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')
            convert = soup.findAll('div', {'data-test': "text", 'class': "Text__sc-j452t5-0 rXahS"})
            temp = convert[0].text.replace(' ₽', '')
            temp = temp.replace(',', '.')
            temp = float(temp)
            # print(temp)
            self.CurrencyUSDRUB = temp
            return float(self.CurrencyUSDRUB)
        else:
            return float(self.CurrencyUSDRUB)

    @retry
    # @property
    def get_EURRUB(self) -> float:

        if self.CurrencyEURRUB == 0:
            dollar_rub = 'https://www.banki.ru/products/currency/eur/'
            full_page = requests.get(dollar_rub, self.__headers)
            soup = BeautifulSoup(full_page.content, 'html.parser')
            convert = soup.findAll('div', {'data-test': "text", 'class': "Text__sc-j452t5-0 rXahS"})
            temp = convert[0].text.replace(' ₽', '')
            temp = temp.replace(',', '.')
            temp = float(temp)
            # print(temp)
            self.CurrencyEURRUB = temp
            return self.CurrencyEURRUB
        else:
            return self.CurrencyEURRUB

