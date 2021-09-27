# -*- coding: utf-8 -*-
import scrapy
from navercrawler.items import NavercrawlerItem, CustomItem

class NaverNewsCrawler(scrapy.Spider):
    name = "navernews"
    start_urls = [
        'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001',
    ]

    def start_requests(self):
        for i in range(1):
            target_url = f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001&date=20210915&page={i}'
            yield scrapy.Request(url=target_url, callback=self.parse)

    def parse(self, response):
        for data in response.css("#main_content > div.list_body.newsflash_body > ul.type06_headline > li"):
            item = NavercrawlerItem()
            target_url = data.css('dt:nth-child(2) > a::attr(href)').get()
            title = data.css(" dl > dd > span.lede::text").get()
            author = data.css("dl > dd > span.writing::text").get()
            preview = data.css("dt:nth-child(2) > a::text").get()

            item['title'] = title
            item['author'] = author
            item['preview'] = preview
            item['target_url'] = target_url

            yield item
            yield scrapy.Request(target_url, callback=self.parse_post)

    ## use dataclass
    # def parse_post(self, response):
    #     title = response.css('h3#articleTitle::text').get()
    #     target_url = response.url
    #
    #     yield CustomItem(title, target_url)

    def parse_post(self, response):
        customItem= CustomItem()
        title = response.css('h3#articleTitle::text').get()
        target_url = response.url
        customItem['title'] = title
        customItem['target_url'] = target_url
        yield customItem
        self.third_parser('테스트')
        # yield scrapy.Request(target_url, callback=self.third_parser, cb_kwargs=dict(test=1))



    def third_parser(self, test):
        print(test)
