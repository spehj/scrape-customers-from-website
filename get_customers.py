import sys

from scraper import Scraper

if __name__ == "__main__":
    try:
        json_filename = sys.argv[1]
        if not ".json" in json_filename:
            raise Exception("JSON file is not specified.")

    except IndexError:
        print("Usage of the script: python get_customers.py <json filename>")
        sys.exit(1)

    scraper = Scraper("https://scale.com/")
    # scraper.get_homepage()
    customers_url = scraper.get_customers()
    result = scraper.parse_customers(customers_url)
    scraper.generate_json(result=result, filename=json_filename)
