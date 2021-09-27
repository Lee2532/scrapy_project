# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
from sqlalchemy import create_engine
from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter, is_item

class NavercrawlerPipeline:

    collection_name = 'scarpy_naver_news'

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = '0000'
        database = 'postgres'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()


    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    async def process_item(self, item, spider):
        '''
        item 필드에서 가져오지 못하는 데이터가 있을 경우 raise DropItem을 통한 삭제
        또는 else문에 해당 없는 데이터값 지정 가능
        해당 기능을 사용하기 위해 임시적으로 dataclass 미사용.
        기타 데이터 정제 로직 작성하는 필드.
        item class name을 통해 특정 로직으로 구분
        '''

        if item.__class__.__name__ == 'NavercrawlerItem':
            pass
        else:
            pass
            # database save
        # self.cur.execute("insert into test(title,target_url) values(%s,%s)",(item['title'],item['target_url']))
        # self.connection.commit()


        if item['title']: # 만약 타이틀이 null, 못가져온다면
            pass
        else:
            item['title'] = 'Missing title'
            # raise DropItem("Missing title") # 해당 item 삭제
        return item

    # def process_item(self, item, spider):
    #     self.cur.execute("insert into quotes_content(content,author) values(%s,%s)",(item['content'],item['author']))
    #     self.connection.commit()
    #     return item

class JsonPipeline(object):
    def __init__(self):
        self.file = open("crawler_data.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        return item
