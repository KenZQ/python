#coding=utf-8


from selenium import webdriver
import scrapy


class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        driver = webdriver.Chrome()
        driver.get(request.url)
        html = driver.page_source

        driver.quit()

        return scrapy.http.HtmlResponse(url=request.url, body=html, encoding="utf-8", request=request)
