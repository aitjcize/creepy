#!/usr/bin/env python

from creepy import Crawler
from threading import Lock

class TestCrawler(Crawler):
    def __init__(self):
        super(TestCrawler, self).__init__()
        self.process_lock = Lock()

    def process_document(self, doc):
        self.process_lock.acquire()
        print 'GET', doc.status, doc.url
        self.process_lock.release()

c = TestCrawler()
c.crawl('http://aborigine.moc.gov.tw')
