# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class QuotestutorialPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="scrapy_quotes"
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        sql = "INSERT INTO quotes (title, author, tags) VALUES (%s, %s, %s)"
        val = (item['title'][0], item['author'][0], ', '.join(item['tags']))
        self.cursor.execute(sql, val)
        self.conn.commit()
