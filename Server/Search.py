import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import logging
import re
#logging.basicConfig(level=logging.DEBUG)
reChinese = re.compile(r'[^\x00-\x7f]')

meaninglessCode = '#include<stdio.h> int main(){ printf("Hello world!");} '

def search(onlinejudge, problem, index = 0):
	logging.debug("search:")
	data = {
		'wd': 'site:blog.csdn.net' + ' ' + onlinejudge + ' ' + problem,
		'tn': 'baidurt'
	}
	url = 'http://www.baidu.com/s?' + urllib.parse.urlencode(data)
	request = urllib.request.Request(url)
	html = urllib.request.urlopen(request).read()
	
	soup = BeautifulSoup(html, 'lxml')
	tag_f = soup.find_all(class_ = 'f')[index]
	url = tag_f.h3.a['href']

	html = urllib.request.urlopen(url).read()
	#logging.debug("html:")
	#logging.debug(html)
	soup = BeautifulSoup(html, 'lxml')
	#code_list = soup.find_all('pre', class_ = ['cpp', 'prettyprint'])
	code_list = soup.find_all('code')#, class_ = ['cpp', 'prettyprint', 'language-cpp', 'language-plain', 'language-objc'])

	#logging.debug("code_list:")
	#logging.debug(code_list)
	code = ''
	for code_item in code_list:
		test_code = code_item.get_text()
		if len(test_code) > len(code):
			code = test_code
	
	data = {
		'url': url,
		'code': reChinese.sub('', code)
	}
	logging.debug("data:")
	logging.debug(data)

	if data['code'] == '':
		data['code'] = meaninglessCode
	return data

if __name__ == '__main__':
	code = search('HDU', '1000')
	print(code)