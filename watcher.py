from scrapy import signals, Spider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher

import json


class CLSpider(Spider):
    name = "cl-spider"
    start_urls = ["https://pittsburgh.craigslist.org/search/sss?query=klr%20650&sort=rel",
                  "https://philadelphia.craigslist.org/search/sss?query=klr%20650&sort=rel"]

    def parse(self, response):
        for cl in response.css(".result-row"):
            yield {
                "title": cl.css(".result-title.hdrlnk ::text").extract_first(),
                "hood": cl.css(".result-hood ::text").extract_first(),
                "price": int(cl.css(".result-price ::text").extract_first().replace("$", "")),
                "date": cl.css(".result-date ::attr(datetime)").extract_first(),
                "id": cl.css(".result-title.hdrlnk ::attr(data-id)").extract_first(),
                "href": cl.css(".result-title.hdrlnk ::attr(href)").extract_first(),
            }

        if response.css('button.next').extract_first():
            yield scrapy.Request(
                response.urljoin(response.css('button.next').extract_first()),
                callback=self.parse
            )

def clear_output_file():
    open("metadata.json", "w").write("")

def filter_results(results):
    ret = []
    for result in results:
        if result["price"] > 100:
            ret.append(result)
    return ret


def spider_results():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(get_project_settings())
    process.crawl(CLSpider)
    process.start()
    return results


if __name__ == "__main__":
    results = filter_results(spider_results())
    try:
        original_data = json.load(open("metadata.json", "r"))
    except FileNotFoundError:
        original_data = []
    
    if len(original_data) != 0:
        for result in results:
            id = result["id"]
            for original_result in original_data:
                original_id = original_result["id"]

                if id == original_id:
                    print("match")
    
    clear_output_file()
    with open("metadata.json", "a") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

