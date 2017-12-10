# -*- coding: utf-8 -*-

import requests
from lxml import html

url_jianshu = "http://www.jianshu.com/"

# 怡小乐主页
url_yixiaole = "u/49cc02f7f8c6" 



def crawl_content(link):
	url = url_jianshu + link
	response = requests.get(url)
	parsed_body = html.fromstring(response.text)

	content_eles = parsed_body.xpath('//div[@class="show-content"]')
	all_p = content_eles[0].findall("p")

	content_str = ''

	for p in all_p:
		# print url, p.text
		if p.text:
			content_str = content_str + p.text

	return content_str


def crawl_jianshu(url):
	response = requests.get(url)
	parsed_body = html.fromstring(response.text)

	lists = parsed_body.xpath('//div[@id="list-container"]//li/div')
	#print "lists", lists

	articles = []
	for item in lists:
		article = {
			"title":item.find('a[@class="title"]').text,
			"time":item.find('div/div/span').get("data-shared-at")
			
			# "content_short":item.findtext('p')

		}

		link = item.find('a').get('href')
		article["content"] = crawl_content(link)
		# print article
		articles.append(article)

	return articles

articles = crawl_jianshu(url_jianshu + url_yixiaole)

for art in articles:
	print "title:",art["title"], " time:", art["time"]
	print "content:",art["content"]



