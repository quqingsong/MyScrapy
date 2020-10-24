# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['51job.com']
    start_urls = ['https://www.51job.com/']
    url="https://i.51job.com/userset/my_51job.php"

    def parse(self, response):
        scrapy.FormRequest(response,formdata={"loginname":"13277996533","password":"qqs201911."},callback=self.parseindex)
    def parseindex(self,response):
        yield scrapy.Request(url=self.url,callback=self.showpage)


    def showpage(self,reponse):
        pass
        # with open("1.txt","w")as file:
        #     file.write(reponse.body)