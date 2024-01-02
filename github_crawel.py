# -*- encoding: utf-8 -*-
"""

@File    :   github_crawel.py
@Modify Time : 2024/1/1 21:20 
@Author  :  Allen.Yang  
@Contact :   MC36514@um.edu.mo        
@Description  : github网站爬取示例代码

"""
# import package begin
import os
import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv
# import package end


url_github = "https://github.com/"  # github网页home page
# 检索URL
url_filter = "https://github.com/search?q=%E4%B8%AD%E5%B1%B1%E5%A4%A7%E5%AD%A6&type=repositories"
# Json格式封装请求头
request_headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

# 显示句柄指定headers使用上面封装好的request_headers
response = requests.get(url_filter,headers=request_headers)

# 检查响应状态 200 代表OK
response_statusCode = response.status_code
print(f"状态码为：{response_statusCode}")

# 获取响应文本
response_text = response.text
#print(response_text)

# bs4库进行解析HTML文本
soup = BeautifulSoup(response_text,"html.parser")
#print(soup.find("h1").text)

# 将soup获取的html文档转成etree形式
tree = etree.HTML(str(soup))


# xpath查找方式，返回的内容是一个列表，即便单返回值，也会被封装在列表里
# 我们可以用形式如   标签名[@属性名=“匹配内容”]来找到匹配的信息
items_form = tree.xpath('//div[@class="Box-sc-g0xbh4-0 hKtuLA"]')
print(f"查找信息长度:{len(items_form)}")

# 创建CSV文件，将爬取到的内容写道CSV文件中
with open('./data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # 写入表头
    writer.writerow(['User Name', 'Project Name', 'Project Href'])

    # 遍历数据列表，并将每一行写入CSV文件
    for item in items_form:
        # 带.表示从当前节点开始寻找，不带.则视为从根目录开始寻找
        # //表示查找所有的子孙level     /表示只查找直接子level
        user_name = item.xpath('string(.//div/div/h3//text())')
        project_name = item.xpath('string(.//div/div/div[@class="Box-sc-g0xbh4-0 LjnbQ"])')
        project_href = "https://github.com/" + item.xpath('string(.//div/div/h3//a/@href)')
        print(user_name,project_name,project_href)

        # 将数据写入CSV文件
        writer.writerow([user_name, project_name, project_href])


# Waht about next page
element_page_bottom = tree.xpath('//div[@class="Box-sc-g0xbh4-0 gukfho TablePaginationSteps"]')[0]
href_next_page = None
print(len(element_page_bottom))

# 存在下一页
if(len(element_page_bottom)>0 and element_page_bottom != None):
    # 获取href值用@href
    href_next_page = element_page_bottom.xpath('.//a[@rel="next"]/@href')[0]
    print(f"下一页地址:{href_next_page}")

# 显示句柄指定headers使用上面封装好的request_headers
response = requests.get(href_next_page,headers=request_headers)

# 检查响应状态 200 代表OK
response_statusCode = response.status_code
print(response_statusCode)

if __name__ == '__main__':
    pass