import itertools as its
# import string
import time


start_time = time.time() 

class DictMaker(object):

    def __init__(self):
        self.s = "aA1234567890" # string.ascii_lowercase + "1234567890@"
        self.pwd_producter = its.product(self.s, repeat=8)
        self.file = open("pwd_2.txt", "a+")
        self.content_num = 0

    def start_program(self):
        print("start \n")
        for i in self.pwd_producter:
            self._pwd_cheacker(i)
        print("ok\n")
        

    def _text_writer(self, content):
        content = "".join(content) + "\n"
        self.file.write(content)
        self.content_num += 1
        if self.content_num >= 10000:
            self.file.flush()
            self.content_num = 0
        

    def _pwd_cheacker(self, myStr):
        try:    
            myStr = "".join(myStr)
            
            if myStr.count(max(self.s, key=myStr.count)) > 2:
                return

            # print("%s\n" %myStr)
            self._text_writer(myStr)

        except Exception as e:
            print("%s\n" %e)


    def __del__(self):
        self.file.close()
        print("this program cost %d second" % time.time() - start.time)

def main():
    d = DictMaker()
    d.start_program()



if __name__ == '__main__':
    main()

