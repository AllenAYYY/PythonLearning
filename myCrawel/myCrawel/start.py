# -*- encoding: utf-8 -*-
"""

@File    :   start.py  
@Modify Time : 2024/1/11 14:48 
@Author  :  Allen.Yang  
@Contact :   MC36514@um.edu.mo        
@Description  : scrapy框架启动接口

"""

from scrapy import cmdline
cmdline.execute('scrapy crawl blogCrawel'.split())