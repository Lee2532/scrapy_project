# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "navernews"
    start_urls = [
        'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001',
    ]

    def start_requests(self):
        for i in range(10):
            target_url = f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001&date=20210915&page={i}'
            yield scrapy.Request(url=target_url, callback=self.parse)

    def parse(self, response):
        for data in response.css("#main_content > div.list_body.newsflash_body > ul.type06_headline > li"):
            target_url = data.css('dt:nth-child(2) > a::attr(href)').get()
            title = data.css(" dl > dd > span.lede::text").get()
            author = data.css("dl > dd > span.writing::text").get()
            preview = data.css("dt:nth-child(2) > a::text").get()


            yield scrapy.Request(target_url, callback=self.parse_post)

            # yield {
            #     'title': title,
            #     'author': author,
            #     'target_url' : target_url,
            #     'preview': preview.strip()
            # }

    def parse_post(self, response):
        print(response)
        pass