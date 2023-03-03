# How to run this project

Install all requirements.

```bash
pip install -r requirements.txt
```

Run **get_customers.py** with argument for JSON filename. This JSON file contains name of the customer and link to customer's logo.

Example

```bash
python get_customers.py customers.json
```

File **scraper.py** contains object an methods for scraping a randomly chosen website.

Result is in a file **customers.json**.
