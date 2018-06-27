#coding=utf-8  
from lxml import etree
import urllib.request
import csv
import xlwt

first_url = 'http://www.csres.com'
#def get_url(url,headers):
#获得工标网首页html
html = urllib.request.urlopen(first_url)
response = html.read().decode('gbk')
#将首页转换成etree格式
page = etree.HTML(response)
#在首页中找到'分类'、'新标准'、'标准公告'、'标准动态'、'论坛'、'文档'的URL
second_urls = page.xpath('//a[@class="a_top_blue"]/@href')
full_second_urls = []
for url_2 in second_urls[0:5]:
    second_url = first_url + str(url_2)
    full_second_urls.append(second_url)
full_second_urls.append(second_urls[5])
#解析'分类'、'新标准'、'标准公告'、'标准动态'、'论坛'、'文档'的html,将其转换为etree格式
classify_html = urllib.request.urlopen(full_second_urls[0])
classify_page = etree.HTML(classify_html.read().decode('gbk'))
#获得'分类'页面下的所有url
full_third_urls = []
third_urls = classify_page.xpath('//a[@class="sh14lian"]/@href')
#获得'分类'页面下的各url的文本
third_urls_text = classify_page.xpath('//a[@class="sh14lian"]/text()')
#循环获取url
for url_3 in third_urls:
    third_url = first_url + str(url_3)
    full_third_urls.append(third_url)
    #print(url_3)
#循环获取url的文本
full_third_urls_text = [] 
for url_3_text in third_urls_text:
    full_third_urls_text.append(url_3_text)
    #print(url_3_text)
del full_third_urls[23:25]
#得到第三个页面的url与text的对应关系，即字典
dic_third_page = dict(zip(full_third_urls_text,full_third_urls))
#print(dic_third_page)
#获得'A综合'下的url及各url的文本
A_html = urllib.request.urlopen(full_third_urls[0])
A_page = etree.HTML(A_html.read().decode('gbk'))
#获得'A综合'页面下的所有url
full_A_urls = []
A_urls = A_page.xpath('//a[@class="sh14lian"]/@href')
#获得'A综合'页面下的各url的文本
A_urls_text = A_page.xpath('//a[@class="sh14lian"]/text()')
#循环获取url
for url_A in A_urls:
    url_A = first_url + str(url_A)
    full_A_urls.append(url_A)
    #print(url_A)
#print(len(full_A_urls))
#循环获取url的文本
#del full_A_urls[29,43,44,49,50,56,64,65,70,71]
#print(len(full_A_urls))
full_A_urls_text = [] 
for url_A_text in A_urls_text:
    full_A_urls_text.append(url_A_text)
    #print(url_A_text)
#print(len(full_A_urls_text))
#del full_third_urls[23:25]
#得到'A综合'页面的url与text的对应关系，即字典
'''dic_A_page = dict(zip(full_A_urls_text,full_A_urls))
dic_A_page.pop('\xa0')'''

#print(dic_A_page)
#print(len(dic_A_page))
#获得标准列表的url
finally_html = urllib.request.urlopen(full_A_urls[0])
finally_page = etree.HTML(finally_html.read().decode('gbk'))
#获得标准列表的表头
list_head = []
list_heads = finally_page.xpath('//thead[@class="th1"]/tr/th/text()')
for item in list_heads:
    list_head.append(item)
#print(item)
#获得标准的标准编号、标准名称、ICS分类、发布部门、发布日期、实施日期
standard_list = []
standard_nums = finally_page.xpath('//thead/tr[@bgcolor="#FFFFFF"]/@title')
for standard_num in standard_nums:
    standard_list.append(standard_num)
#print(len(standard_list))
print(len(standard_list[0]))
#print(standard_list[0][115:125])
#print(standard_list)
#获得标准的标准状态

state_list = []
states = finally_page.xpath('//thead/tr[@bgcolor="#FFFFFF"]/td[last()]/font/text()')
for state in states:
    state_list.append(state)
    #print(state)
print(len(state_list))
#print(full_third_urls_text)
#print(len(full_third_urls_text))
#print(full_third_urls)
#print(len(full_third_urls))
#print(full_second_urls)
    #str(standard_list[0][3:19])

#将数据写入excel文件
workbook=xlwt.Workbook(encoding='utf-8')  
booksheet=workbook.add_sheet('标准', cell_overwrite_ok=True)  

DATAS = (('编号','标题','ICS分类','发布部门','发布日期','实施日期','状态'),
         ('DB21/T 2457-2015',standard_list[0][24:36],standard_list[0][54:63],standard_list[0][83:93],standard_list[0][99:110],standard_list[0][115:125],state_list[0]))
for i,row in enumerate(DATAS):  
    for j,col in enumerate(row):  
        booksheet.write(i,j,col)  
workbook.save('grade.xls')


