import requests
from lxml import html
import json

class Yelp_Scraper:
    def __init__(self):
        self.data = []
        self.page = 1
        
    def get_reviews(self, tree):
        # Define the logic for extracting and processing reviews from the 'tree' parameter
        pass

    def check_reviews(self):

        while True:
            print(self.page)
            base_url = f"https://www.yelp.com/biz/the-brunch-house-temecula?start={self.page}"

            r = requests.get(base_url)

            tree = html.fromstring(r.text)
            names = tree.xpath('//div[contains(@class, "user-passport-info")]//a[contains(@class, "y-css-12ly5yx")]')

            if len(names) < 1:
                self.data = json.dumps(self.data)
                print(self.data)
                break
            else:
                self.get_reviews(tree)  # Call the get_reviews method using 'self'
                self.page += 9
            
    def get_reviews(self,tree):
        names = tree.xpath('//div[contains(@class, "user-passport-info")]//a[contains(@class, "y-css-12ly5yx")]')
        aria_labels = tree.xpath('//div[@class="y-css-9tnml4"]')
        comment = tree.xpath('//p[@class="comment__09f24__D0cxf y-css-h9c2fl"]//span[contains(@class,"raw__09f24__T4Ezm")]')
        review_date = tree.xpath('//div[@class="arrange-unit__09f24__rqHTg arrange-unit-fill__09f24__CUubG y-css-1iy1dwt"]//span[@class=" y-css-wfbtsu"]')
        for name, rating, review, date in zip(names, aria_labels, comment, review_date):
            # print(name.text)
            # print(rating.get('aria-label'))
            # print(review.text)
            # print(date.text)
            # print('')
            
            self.data.append({"name": name.text, "rating": rating.get('aria-label'), "review":review.text, "date":date.text})
        

ys = Yelp_Scraper().check_reviews()



