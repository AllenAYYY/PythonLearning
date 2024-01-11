import scrapy
from ..items import MycrawelItem

class BlogcrawelSpider(scrapy.Spider):
    count = 1
    name = "blogCrawel"
    # 允许爬虫的域名
    allowed_domains = ["github.com"]
    # 设置起始的URL
    start_urls = ["https://github.com/search?q=%E4%B8%AD%E5%B1%B1%E5%A4%A7%E5%AD%A6&type=repositories"]
    # 数据提取的方法，接收中间件传过来的response，定义对网站的相关操作
    def parse(self, response):
        list = response.xpath('//div[@class="Box-sc-g0xbh4-0 hKtuLA"]')
        print(f"第{self.count}页，查找条数{len(list)}")
        self.count +=1
        item = MycrawelItem()
        for info in list:
            item['name'] = ''.join(info.xpath('.//div/div/h3//text()').extract())
            item['project'] = ''.join(info.xpath('string(.//div/div/div[@class="Box-sc-g0xbh4-0 LjnbQ"])').extract())
            item['href'] = "https://github.com/" + ''.join(info.xpath('.//div/div/h3//a/@href').extract())
            # yield 返回数据
            yield item
        nextHref = response.xpath('//a[@rel="next"]/@href').extract_first()
        if nextHref is not None:
            next_page_url = response.urljoin(nextHref)
            # 指定回调函数是self.parse，意味着发现下一页就重新执行parse函数
            yield scrapy.Request(next_page_url, callback=self.parse)

