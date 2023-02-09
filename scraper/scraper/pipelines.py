# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from crm.quotes.models import Quotes
from crm.blog.models import Blog

import logging, coloredlogs
logger = logging.getLogger(__name__)
coloredlogs.install(level="WARN", logger=logger)


class ScraperPipeline:


    def process_item(self, item, spider):
        try:



            Blog.objects.create(title=item['title'], detail=item['detail'], author_id=1)
            print("\n")
            logger.warn("Loaded quote {}".format(item['title']))
            # print(item)
        except Exception as e:
            print("\n")
            logger.error("\nFailed to load quote, Reason For Failure:{}".format(e))
            # print(item)
        return item
