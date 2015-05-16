import scrapy
from share_vnn_vn.items import ShareVnnVnItem


def genURLs():
    url_id = range(9999999)
    for i in url_id:
        yield "http://share.vnn.vn/tai-file-2{:07}".format(i)

class ShareVnnVnSpider(scrapy.Spider):
    name = "sharevnnvn"
    allowed_domains = ["share.vnn.vn"]
#    start_urls=[
#        "http://share.vnn.vn/tai-file-2{:07}".format(i) for i in xrange(1,9999)
#    ]
    def start_requests(self):
        for i in range(9999999):
            yield scrapy.http.Request(url="http://share.vnn.vn/tai-file-2{:07}".format(i))

    def parse(self, response):
        for sel in response.xpath('//div[@class="dl-file"]'):
            item = ShareVnnVnItem()
            item['ID'] =  response.url.split('-')[-1]
            item['NAME'] = sel.xpath('//h1/text()').extract()
            item['SIZE'] = sel.xpath('//p/text()').re(r'ng:\s*(.*) - L')
            yield item
