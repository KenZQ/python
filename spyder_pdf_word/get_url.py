import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from cStringIO import StringIO
import docx
import subprocess
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

import os
import urllib
import requests
from lxml import etree


# //div[@class='biao']//a/@href @title    1497
# //tr[@class='hang td1| td2']//a    //tr[contains(@class,'hang')]//a   @href text()

#     download

def deal_doc(filename, link):
    subprocess.call(['soffice', '--headless', '--convert-to', 'docx', filename])
    doc = docx.Document(filename[:-4] + ".docx")
    for para in doc.paragraphs:
        print (para.text)


def deal_pdf(file_name, url):

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()

    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    path = file_name
    with open(path, 'rb') as fp:
        for page in PDFPage.get_pages(fp, set()):
            interpreter.process_page(page)
        text = retstr.getvalue()

    device.close()
    retstr.close()
    with open(path[:(path.index('.'))] + '.text', 'w') as f:
        f.write(text)


def download_resource(file_name, link):
    urllib.urlretrieve(link, file_name)
    if file_name.endswith('.doc'):
        deal_doc(file_name, link)
    elif file_name.endswith('.pdf'):
        deal_pdf(file_name, link)


def fun():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /Chrome/62.0.3202.75 Safari/537.36'
    }
    start_url = 'http://www.zikao365.com/web/lnst/'
    response = requests.get(start_url, headers=headers)
    # html = response.text
    html = response.content
    html_obj = etree.HTML(html)

    subject_list = html_obj.xpath("//div[@class='biao']//a")
    for i, subject in enumerate(subject_list):
        link = subject.xpath('@href')
        text = subject.xpath('text()')
        subject_title = text.decode('utf-8').encode('utf-8')
        if not os.path.exists(subject_title):
            os.mkdir(subject_title)

            # for link in subject_href:
        response = requests.get(link, headers=headers)
        html = response.content
        html_obj = etree.HTML(html)
        page_list = html_obj.xpath("//tr[contains(@class,'hang')]//a")
        for i, page in enumerate(page_list):
            examination_title = page.xpath("text()")

            page_link = page.xpath("@href")
            response = requests.get(page_link, headers=headers)
            html = response.content
            html_obj = etree.HTML(html)
            download_link = html_obj.xpath("//div[6]/a[1]/@href")
            type = download_link[download_link.rfind('.'):]
            os.path.abspath()
            filename = os.path.join(subject_title, examination_title + type)
            # if not os.path.exists(filename):
            #     os.path
            download_resource(filename, download_link)

            if i == 1:
                break

        if i == 1:
            break


def main():
    fun()


if __name__ == "__main__":
    main()
