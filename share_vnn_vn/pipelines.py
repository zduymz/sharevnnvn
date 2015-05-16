# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from models import ShareVnnVn, db_connect, create_sharevnnvn_table

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ShareVnnVnPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_sharevnnvn_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        sharevnnvn = ShareVnnVn(**item)
        session.add(sharevnnvn)
        session.commit()
        return item
