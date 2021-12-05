from urllib.parse import urljoin

import requests
import re


class Parser():

    def __init__(self, url):
        self.url = url

    def get_response_text(self):
        headers = {
            'User-Agent': 'Marinka'
        }
        params = {
            "format": ["mm", "ms"],
            "category": "fruit"
        }
        response = requests.get(self.url, headers=headers, params=params)
        return response.text

    def get_promo_links(self, pagetext):
        pattern = re.compile(r'<a.+href=\"(.[promo]+[^\"]+)\"')
        links = re.findall(pattern, pagetext)
        return links
        #for link in re.findall(pattern, pagetext):
        #    url = urljoin(self.url, link)
         #   print(url)