# -*- coding:utf-8 -*-  
"""
--------------------------------
    @Author: Dyson
    @Contact: Weaver1990@163.com
    @file: crawler.py.py
    @time: 2017/10/20 10:21
--------------------------------
"""
import sys
import os
import json
import phantomjs_method
import requests_method
import pandas as pd
import traceback

sys.path.append(sys.prefix + "\\Lib\\MyWheels")
reload(sys)
sys.setdefaultencoding('utf8')
import set_log  # log_obj.debug(文本)  "\x1B[1;32;41m (文本)\x1B[0m"

log_obj = set_log.Logger('crawler.py.log', set_log.logging.WARNING,
                         set_log.logging.DEBUG)
log_obj.cleanup('crawler.py.log', if_cleanup=True)  # 是否需要在每次运行程序前清空Log文件

with open(r'spider_args.json', 'r') as f:
    spider_args = json.load(f)

class crawler(object):

    def __init__(self):
        self.phantomjs_method = phantomjs_method.phantomjs_method()
        self.requests_method = requests_method.requests_method()

    def main(self):
        # 运行爬虫的主程序
        for id0 in spider_args:
            args0 = spider_args[id0]
            print "Crawling id:%s, title:%s" %(id0, args0["_comment"])
            item = {}

            # 目录页
            try:
                method_file = getattr(self,args0["url_args"]["method_file1"])
                item_generator = getattr(method_file,args0["url_args"]["method1"])(item, args0['url'], args0["url_args"]["args1"]) # 目录页
            except:
                log_obj.error("解析目录页时 %s 出现错误" %args0['url'])
                log_obj.error(traceback.format_exc())
                continue

            for item in item_generator:
                # 详情页
                try:
                    method_file = getattr(self, args0["detail_args"]["method_file1"])
                    item = getattr(method_file,args0["detail_args"]["method1"])(item, item['detail_url'], args0["detail_args"]["args1"]) # 详情页

                    df = pd.DataFrame(item, index=[0,])

                    df.to_csv('text.csv', mode='a', encoding='utf_8_sig')
                except:
                    log_obj.error("解析详情页时 %s 出现错误" % item['detail_url'])
                    log_obj.error(traceback.format_exc())
                    continue





if __name__ == '__main__':
    crawler = crawler()
    crawler.main()
