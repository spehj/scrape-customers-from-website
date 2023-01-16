import json

import requests
from bs4 import BeautifulSoup


class Scraper:
    """
    Scraper instance class.
    """

    def __init__(self, home_url) -> None:
        self.home_url = home_url

    def get_homepage(self):
        """Method to scrape website we want."""
        result = requests.get(self.home_url)
        home_doc = BeautifulSoup(result.text, "html.parser")
        print(home_doc.prettify())

    def get_customers(self):
        """Method to get the customers page."""
        home_result = requests.get(self.home_url)
        home_document = BeautifulSoup(home_result.text, "html.parser")
        # customers = home_document.find_all(text="Customers")
        # Find link to customers page
        customers_links = home_document.find_all("a", href=True, text="Customers")
        customers_url = self.home_url + customers_links[0]["href"][1:]
        return customers_url

    def parse_customers(self, customers_url):
        """Method to parse customers from the site."""
        # Parse customers page
        customers_page = requests.get(customers_url)
        customers_doc = BeautifulSoup(customers_page.text, "html.parser")

        logo_images = customers_doc.find_all("img")

        result_dict = {}

        # Get all images with alt including "logo"
        for img in logo_images:
            if "logo" in img["alt"]:
                # Save result to dictionary in form of {"company name" : "logo cdn link"}
                result_dict[img["alt"][:-5]] = img["src"]

        return result_dict

    def generate_json(self, result: dict, filename: str):
        """Generate json file of customers and logo links.

        Args:
            result (dict): return from parse_customers method.
            filename (str): Filename of JSON.
        """
        with open(filename, "w") as fd:
            json.dump(result, fd)
