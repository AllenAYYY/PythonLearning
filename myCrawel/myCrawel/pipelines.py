# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
# pipeline文件中定义对数据的操作
# 这个文件就是我们常说的数据管道，当item在spider中被收集之后，会被传递到item pipeline
# 这些管道组件会按照定义的顺序处理item。每个管道都实现了简单方法的类，比如决定保存数据还是丢弃
class MycrawelPipeline:
    def __init__(self):
        self.file = open('./data123.csv', 'w', newline='',encoding='utf-8_sig')
        self.writer = csv.writer(self.file)
        # 写入CSV文件的标题行
        self.writer.writerow(['name', 'project', 'url'])

    def process_item(self, item, spider):
        # 将item对象强制转为字典
        item = dict(item)

        # 提取数据字段
        field1 = item['name']
        field2 = item['project']
        field3 = item['href']

        # 将数据写入CSV文件
        self.writer.writerow([field1, field2, field3])

        return item

    def close_spider(self, spider):
        self.file.close()
