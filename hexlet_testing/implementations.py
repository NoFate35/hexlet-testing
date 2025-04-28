import requests
from bs4 import BeautifulSoup
import os


class NewsParser:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def parse_headlines(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        headlines = soup.find_all('h2', class_='news-title')
        return [headline.text.strip() for headline in headlines]

    def save_headlines(self, headlines, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for headline in headlines:
                f.write(f"{headline}\n")

    def process(self, output_file):
        html = self.fetch_html()
        headlines = self.parse_headlines(html)
        self.save_headlines(headlines, output_file)


class IncorrectNewsParser1:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def parse_headlines(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        headlines = soup.find_all('h2', class_='news-title')
        return [headline.text.strip() for headline in headlines]

    def save_headlines(self, headlines, filename):
        # Ничего не сохраняет
        pass

    def process(self, output_file):
        html = self.fetch_html()
        headlines = self.parse_headlines(html)
        self.save_headlines(headlines, output_file)


class IncorrectNewsParser2:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def parse_headlines(self, html):
        # Игнорирует входной HTML и всегда возвращает фиксированный список
        return ["Новость 1", "Новость 2"]

    def save_headlines(self, headlines, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for headline in headlines:
                f.write(f"{headline}\n")

    def process(self, output_file):
        html = self.fetch_html()
        headlines = self.parse_headlines(html)
        self.save_headlines(headlines, output_file)


class IncorrectNewsParser3:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text

    def parse_headlines(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        headlines = soup.find_all('h2', class_='news-title')
        return [headline.text.strip() for headline in headlines]

    def save_headlines(self, headlines, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for headline in headlines:
                f.write(f"{headline}\n")

    def process(self, output_file):
        # Не корректно работает весь пайплайн
        html = self.fetch_html()
        self.parse_headlines(html)


classes = {
    "right": NewsParser,
    "fail1": IncorrectNewsParser1,
    "fail2": IncorrectNewsParser2,
    "fail3": IncorrectNewsParser3,
}


def get_class():
    name = os.environ['CLASS_VERSION']
    return classes[name]
