# -*- coding:utf-8 -*-  
"""
--------------------------------
    @Author: Dyson
    @Contact: Weaver1990@163.com
    @file: requests_method.py
    @time: 2017/10/20 10:31
--------------------------------
"""
import sys
import os

import bs4

sys.path.append(sys.prefix + "\\Lib\\MyWheels")
reload(sys)
sys.setdefaultencoding('utf8')
import requests_manager
requests_manager = requests_manager.requests_manager()

url_func = lambda url, s, s0, b:url + s.replace(s0,'') if b else s

class requests_method(object):
    def __init__(self):
        pass

    def catalog_requests_1(self, item, url, args):
        print "准备分析目录页: ", url
        # 根据
        html = requests_manager.get_html(url)
        bs_obj = bs4.BeautifulSoup(html, 'html.parser')
        e_table = bs_obj.find_all(args["e_table"]["tag"], attrs=args["e_table"]["attrs"])
        job_title = ''
        for e_table0 in e_table:
            for e in e_table0.childGenerator():
                if isinstance(e, bs4.NavigableString):
                    continue
                if e.name == "p": # 这里职称单独写在一行
                     job_title = e.get_text(strip=True)
                elif e.name == 'table':
                    e_as = e.find_all('a')
                    for e_a in e_as:
                        item["职称"] = job_title

                        item["detail_url"] = url_func("http://math.ahu.edu.cn/", e_a.get("href"), "http:", True)
                        item["教师姓名"] = e_a.get_text(strip=True)
                        item["课程"] = e_a.find_next('td').get_text(strip=True)

                        yield item

    def catalog_requests_2(self, item, url, args):
        print "准备分析目录页: ", url
        # 根据
        html = requests_manager.get_html(url)
        bs_obj = bs4.BeautifulSoup(html, 'html.parser')
        e_table = bs_obj.find_all(args["e_table"]["tag"], attrs=args["e_table"]["attrs"])
        job_title = ''
        for e_table0 in e_table:
            for e in e_table0.childGenerator():
                if isinstance(e, bs4.NavigableString):
                    continue
                if e.name == "p": # 这里职称单独写在一行
                     job_title = e.get_text(strip=True)
                elif e.name == 'table':
                    e_as = e.find_all('a')
                    for e_a in e_as:
                        item["职称"] = job_title

                        item["detail_url"] = url_func("http://math.ahu.edu.cn/", e_a.get("href"), "http:", True)
                        item["教师姓名"] = e_a.get_text(strip=True)
                        item["课程"] = e_a.find_next('td').get_text(strip=True)

                        yield item

    def detail_requests_1(self, item, url, args):
        print "准备分析详情页页: ", url
        if "detail_url" in item:
            url = item["detail_url"]

        html = requests_manager.get_html(url)
        bs_obj = bs4.BeautifulSoup(html, 'html.parser')
        e_table = bs_obj.find(args["e_table"]["tag"], attrs=args["e_table"]["attrs"])
        item["详情"] = e_table.get_text()
        return item

if __name__ == '__main__':
    pass