import httpx
from parsel import Selector
from pprint import pprint


class MashinaKgCrawler:
    MAIN_URL = "https://www.mashina.kg/search/all/"
    BASE_URL = "https://www.mashina.kg"

    def get_mashina_kg(self):
        self.response = httpx.get(MashinaKgCrawler.MAIN_URL)
        # print(self.response.status_code)
        # print(self.response.text[:250])

    def get_page_title(self):
        selector = Selector(self.response.text)
        title = selector.css("title::text").get()
        # print(title),

    def get_car_links(self):
        selector = Selector(self.response.text)
        cars = selector.css("div.list-item a::attr(href)").getall()
        cars = [f"{MashinaKgCrawler.BASE_URL}{car}" for car in cars]
        return cars[:1]

if __name__ == "__main__":
    crawler = MashinaKgCrawler()
    crawler.get_mashina_kg()
    crawler.get_page_title()
    cars = crawler.get_car_links()
    pprint(cars)