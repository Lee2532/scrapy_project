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


from dataclasses import dataclass, field

# @dataclass
# class CustomItem:
#     title: str
#     target_url: str


class CustomItem(scrapy.Item):
    title = scrapy.Field()
    target_url =scrapy.Field()


from typing import Optional

# @dataclass
# class InventoryItem:
#     title: Optional[str] = field(default=None)
#     target_url: Optional[str] = field(default=None)
