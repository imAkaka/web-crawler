# -*- coding: utf-8 -*-

from selenium import webdriver

driver= webdriver.PhantomJS()
driver.get('https://www.jianshu.com/u/xxxxxxx')

lists = driver.find_elements_by_xpath('//div[@id="list-container"]//li/div')

articles = []
for _list in lists:
	title = _list.find_element_by_class_name('title')
	article = {
		"title": title.text,
		"link": title.get_attribute('href')
	}
	articles.append(article)


def get_jianshu_content(link):
	#url = url_jianshu + suburl selenium这个地方不需要拼接
	url = link
	driver.get(url)
	content = driver.find_element_by_class_name("show-content").text
	return content
	

for art in articles:
	content = get_jianshu_content(art['link'])
	print "title:",art["title"]
	print "content:", content
