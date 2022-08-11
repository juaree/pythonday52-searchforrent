from bs4 import BeautifulSoup
import requests

housing_keys = {"price", "address", "link"}

class GetData:

    def __init__(self, zillow_link):
        self.ZILLOW_URL = zillow_link
        self.DOMAIN_NAME = "https://www.zillow.com"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36",
            "accept-language": "en-US,en;q=0.9"
        }
        self.response = requests.get(f"{self.ZILLOW_URL}", headers=self.headers)
        self.zillow_web_page = self.response.text
        self.soup = BeautifulSoup(self.zillow_web_page, "html.parser")
        self.info = []

    def get_info(self):
        prices = self.soup.find_all(name="div", class_="list-card-price")
        addresses = self.soup.find_all(name="address", class_="list-card-addr")
        links = self.soup.find_all(name="a", class_="list-card-link")
        links = [link.get('href') for link in links if len(link.getText()) > 0]

        prices = [price.getText().split("/")[0].split("+")[0] for price in prices]
        addresses = [address.getText() for address in addresses]
        links = [f"{self.DOMAIN_NAME}{link}" if 'https' not in link else link for link in links]

        info = list(zip(prices, addresses, links))
        return info













