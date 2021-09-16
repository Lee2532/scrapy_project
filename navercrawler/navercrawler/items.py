# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NavercrawlerItem(scrapy.Item):
    title = scrapy.Field() #기사 제목
    preview = scrapy.Field() # 미리보기
    author = scrapy.Field() #언론사
    target_url = scrapy.Field() # 기사링크


from dataclasses import dataclass

@dataclass
class CustomItem:
    title: str
    target_url: str