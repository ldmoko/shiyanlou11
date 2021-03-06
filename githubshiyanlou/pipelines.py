# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from githubshiyanlou.models import Repository, engine
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GithubshiyanlouPipeline(object):
    def process_item(self, item, spider):
        # self.session.add(Repository(name=item['name'], update_time=item['update_time']))
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
    	self.session = sessionmaker(bind=engine)()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
