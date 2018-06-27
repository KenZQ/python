#-*- coding=utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from AQI.items import AqiItem

class AqiSpider(CrawlSpider):
    name = "aqi_crawlspider"
    allowed_domains = ["aqistudy.cn"]
    # 程序的入口，提取每个城市的链接，并发送请求
    start_urls = ["https://www.aqistudy.cn/historydata/"]

    rules = (
        # 提取每个月的链接
        Rule(LinkExtractor(allow=r"monthdata\.php\?city=")),
        # 提取每一天的链接
        Rule(LinkExtractor(allow=r"daydata\.php\?city="), callback = "parse_day")
    )

    # 处理每一天的数据
    def parse_day(self, response):
        node_list = response.xpath("//tr")
        node_list.pop(0)
        city = response.xpath("//h2[@id='title']/text()").extract()[0]

        for node in node_list:
            item = AqiItem()
            item['city'] = city[8:-11]
            item['date'] = node.xpath("./td[1]/text()")
            item['aqi'] = node.xpath("./td[2]/text()")
            item['level'] = node.xpath("./td[3]/span/text()")
            item['pm2_5'] = node.xpath("./td[4]/text()")
            item['pm10'] = node.xpath("./td[5]/text()")
            item['so2'] = node.xpath("./td[6]/text()")
            item['co'] = node.xpath("./td[7]/text()")
            item['no2'] = node.xpath("./td[8]/text()")
            item['o3'] = node.xpath("./td[9]/text()")

            yield item




