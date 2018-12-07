# -*- coding:utf-8 -*-

import json
import urllib
import urllib2




class Urllib_urllib2(object):
    '''
    this is  a simple example
    send post request
    '''


    def send_request(self, url, data, headers):
    

        
        url = url
        data = data
        data = urllib.urlencode(data)
        headers = headers
        
        ret = ""
        req = urllib2.Request(url=url, data=data,headers=headers) 
        
        try:
        
            response = urllib2.urlopen(req)
            ret = response.read()
            print ret
        except urllib2.URLError, e:
            print e.reason

        return ret


def main():
    s = Urllib_urllib2()
    headers = {}
    data = {}
    url = ""
    print s.send_request()


if __name__ == "__main__":
    main()
