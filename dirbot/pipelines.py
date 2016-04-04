# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import codecs
from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""
    def __init__(self):
		self.file = codecs.open("article.json", "wb", encoding="utf-8")

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        """
        for word in self.words_to_filter:
            if word in unicode(item['description']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item
        """
        if item['date']:
            if item['creator']:
                line = json.dumps(dict(item), ensure_ascii=False) + "\n"
                self.file.write(line)
                return item
        else:
            raise DropItem("Empty word")